"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

    Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
    Код компании (справа от названия компании на странице компании)
    P/E компании (информация находится справа от графика на странице компании)
    Годовой рост/падение компании в процентах (основная таблица)
    Высчитать какую прибыль принесли бы акции компании (в процентах),
     если бы они были куплены на уровне 52 Week Low
      и проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:

    Топ 10 компаний с самими дорогими акциями в рублях.
    Топ 10 компаний с самым низким показателем P/E.
    Топ 10 компаний, которые показали самый высокий рост за последний год
    Топ 10 комппаний, которые принесли бы наибольшую прибыль,
     если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
    Пример формата:

    [
    {
     "code": "MMM",
     "name": "3M CO.",
     "price" | "P/E" | "growth" | "potential profit" : value,
    },
    ...
    ]


    P.S. по-максимуму использовать возможности параллелизма и асинхронности.

    bs4
    aiohttp

"""
import asyncio
from multiprocessing import Pool

import aiohttp
from bs4 import BeautifulSoup


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_current_course():
    course_url = "https://www.cbr.ru/scripts/XML_daily.asp"

    def _parse_current_course(html):
        soup = BeautifulSoup(html, features="lxml")
        course = soup.find("valute", id="R01235").value.get_text(
            strip=True, separator=""
        )
        return float(course.replace(",", "."))

    response = await fetch_response(course_url)
    return _parse_current_course(response)


class CollectDataAboutCompany:
    URL = "https://markets.businessinsider.com/index/components/s&p_500"
    MAIN_URL = "https://markets.businessinsider.com/"

    def __init__(self):
        self.course = None

    async def collect_html_for_company(self, company_url):
        company_url = self.MAIN_URL + company_url
        return await fetch_response(company_url)

    async def collect_companies_html_annual_growth(self):
        main_table_html, course = await asyncio.gather(
            fetch_response(self.URL), get_current_course()
        )
        self.course = course
        list_companies_url_annual_growth = list(
            self.parse_company_url_annual_growth_from_main_table(main_table_html)
        )
        companies_html = await asyncio.gather(
            *map(
                self.collect_html_for_company,
                (url for url, _ in list_companies_url_annual_growth),
            )
        )
        return zip(
            companies_html, (growth for _, growth in list_companies_url_annual_growth)
        )

    def parse_company_url_annual_growth_from_main_table(self, main_table_html):
        soup = BeautifulSoup(main_table_html, features="html.parser")
        for row in soup.find_all("tr"):
            a_tag = row.find("a")
            if hasattr(a_tag, "href"):
                company_url = a_tag["href"]
                annual_growth_tag = next(reversed(row.find_all("span")))
                annual_growth = self.parse_float(annual_growth_tag.string)
                yield company_url, annual_growth

    def get_company_as_a_dict(self, company_html, annual_growth):
        soup = BeautifulSoup(company_html, features="html.parser")
        row = soup.find("div", class_="price-section__row")

        row = list(row.stripped_strings)
        company_name, company_code, current_value = row[0], row[2][2:], row[3]
        pe_ratio, profit = self.find_p_e_ratio_and_profit(soup)
        current_value = self.parse_float(current_value)
        price = round(current_value * self.course, 2)
        return {
            "code": company_code,
            "name": company_name,
            "price": price,
            "P/E": pe_ratio,
            "growth": annual_growth,
            "potential profit": profit,
        }

    def find_p_e_ratio_and_profit(self, soup):
        def get_values(soup, text):
            tag = soup.find("div", text=text)
            if tag is None:
                return None
            value = next(tag.parent.stripped_strings)
            return self.parse_float(value)

        table = soup.find("div", {"class": "snapshot"})
        p_e_ratio = get_values(table, "P/E Ratio")
        week_low = get_values(table, "52 Week Low")
        week_high = get_values(table, "52 Week High")
        if week_low is None or week_high is None:
            return p_e_ratio, None
        profit = round((week_high / week_low - 1) * 100, 2)
        return p_e_ratio, profit

    @staticmethod
    def parse_float(number: str):
        """
        >>> CollectDataAboutCompany.parse_float('-11%')
        -11.0

        >>> CollectDataAboutCompany.parse_float('10%')
        10.0

        >>> CollectDataAboutCompany.parse_float('-1,000.00%')
        -1000.0
        """
        number = number.rstrip("%")
        return float(number.replace(",", ""))

    def run(self):
        html_annual_growth_for_companies = asyncio.run(
            self.collect_companies_html_annual_growth()
        )
        with Pool() as pool:
            return pool.starmap(
                self.get_company_as_a_dict, html_annual_growth_for_companies
            )
