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
from itertools import repeat
from multiprocessing import Pool

import aiohttp
from bs4 import BeautifulSoup

MAIN_URL = "https://markets.businessinsider.com/"
URL_FOR_TABLE = "https://markets.businessinsider.com/index/components/s&p_500"


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_current_course():
    course_url = "https://www.cbr.ru/scripts/XML_daily.asp"

    def _parse_current_course(xml_text):
        soup = BeautifulSoup(xml_text, features="lxml")
        course = soup.find("valute", id="R01235").value.get_text(strip=True)
        return float(course.replace(",", "."))

    xml_with_course_data = await fetch_response(course_url)
    return _parse_current_course(xml_with_course_data)


async def collect_html_for_company(company_url):
    company_url = MAIN_URL + company_url
    return await fetch_response(company_url)


async def collect_html_annual_growth_for_companies__course():
    main_table_html, course = await asyncio.gather(
        fetch_response(URL_FOR_TABLE), get_current_course()
    )
    url_and_annual_growth_for_companies = (
        parse_company_url_annual_growth_from_main_table(main_table_html)
    )
    url_for_companies, annual_growth_for_companies = map(
        list, zip(*url_and_annual_growth_for_companies)
    )
    html_for_companies = await asyncio.gather(
        *map(
            collect_html_for_company,
            url_for_companies,
        )
    )
    return zip(
        html_for_companies,
        annual_growth_for_companies,
        repeat(course),
    )


def parse_company_url_annual_growth_from_main_table(main_table_html):
    soup = BeautifulSoup(main_table_html, features="html.parser")
    for row in soup.find_all("tr"):
        a_tag = row.find("a")
        if hasattr(a_tag, "href"):
            company_url = a_tag["href"]
            annual_growth_tag = next(reversed(row.find_all("span")))
            annual_growth = parse_float(annual_growth_tag.string)
            yield company_url, annual_growth


def get_company_as_a_dict(company_html, annual_growth, course):
    soup = BeautifulSoup(company_html, features="html.parser")
    row = soup.find("div", class_="price-section__row")

    row = list(row.stripped_strings)
    company_name, company_code, str_current_value = row[0], row[2][2:], row[3]
    pe_ratio, profit = find_p_e_ratio_and_profit(soup)
    current_value = parse_float(str_current_value)
    price = round(current_value * course, 2)
    return {
        "code": company_code,
        "name": company_name,
        "price": price,
        "P/E": pe_ratio,
        "growth": annual_growth,
        "potential profit": profit,
    }


def find_p_e_ratio_and_profit(soup):
    def get_values(definite_soup, text):
        tag = definite_soup.find("div", text=text)
        if tag is None:
            return None
        str_value = next(tag.parent.stripped_strings)
        return parse_float(str_value)

    table = soup.find("div", {"class": "snapshot"})
    p_e_ratio = get_values(table, "P/E Ratio")
    week_low = get_values(table, "52 Week Low")
    week_high = get_values(table, "52 Week High")
    if week_low is None or week_high is None:
        return p_e_ratio, None
    profit = round((week_high / week_low - 1) * 100, 2)
    return p_e_ratio, profit


def parse_float(str_number: str):
    """
    >>> parse_float('-11%')
    -11.0

    >>> parse_float('10%')
    10.0

    >>> parse_float('-1,000.00%')
    -1000.0
    """
    str_number = str_number.rstrip("%")
    return float(str_number.replace(",", ""))


def parse_html_to_get_companies_data():
    html_annual_growth_for_companies = asyncio.run(
        collect_html_annual_growth_for_companies__course()
    )
    with Pool() as pool:
        return pool.starmap(get_company_as_a_dict, html_annual_growth_for_companies)
