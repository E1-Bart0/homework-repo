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
import concurrent.futures
import time

import aiohttp
from bs4 import BeautifulSoup


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise ValueError(f"Response should be 200, got: {response.status}")


def get_company_url_from_main_table(response):
    soup = BeautifulSoup(response, features="html.parser")
    for index, row in enumerate(soup.find_all("tr")):
        if index > 1:
            a_tag = row.find("a")
            annual_growth_tag = list(row.find_all("span"))[-1]
            company_url = a_tag["href"]
            annual_growth = annual_growth_tag.string
            yield company_url, annual_growth


async def get_full_info_about_company(url, company_url, annual_growth, course):
    main_url_list = url.split("/")[:3]
    main_url = "/".join(main_url_list)
    company_url = main_url + company_url
    response = await fetch_response(company_url)
    return await _get_additional_info_about_company(response, annual_growth, course)


async def _get_additional_info_about_company(response, annual_growth, course):
    soup = BeautifulSoup(response, features="html.parser")
    row = soup.find("div", {"class": "price-section__row"})
    row = list(row.stripped_strings)
    company_name, company_code, current_value = row[0], row[2][2:], row[3]
    pe_ratio, week_low, week_high = list(_find_values_for_company(soup))

    if week_high is not None and week_low is not None:
        profit = round((week_high / week_low - 1) * 100, 2)
    else:
        profit = None
    current_value = float(current_value.replace(",", ""))
    price = round(current_value * course, 2)

    return {
        "code": company_code,
        "name": company_name,
        "price": price,
        "P/E": pe_ratio,
        "growth": float(annual_growth[:-1]),
        "potential profit": profit,
    }


def _find_values_for_company(soup):
    table = soup.find("div", {"class": "snapshot"})
    for text in ("P/E Ratio", "52 Week Low", "52 Week High"):
        tag = table.find("div", text=text)
        if tag is None:
            yield None
        else:
            value = list(tag.parent.stripped_strings)[0]
            yield float(value.replace(",", ""))


async def get_current_course():
    now = time.strftime("%d/%m/%Y", time.localtime())
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + now
    response = await fetch_response(url)
    return await _parse_current_course(response)


async def _parse_current_course(response):
    soup = BeautifulSoup(response, features="html.parser")
    course = soup.find("valute", {"id": "R01235"}).find("value").string
    return float(course.replace(",", "."))


async def _get_result_from(url, response, course):
    features, results = [], []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for company_url, annual_growth in get_company_url_from_main_table(response):
            features.append(
                executor.submit(
                    asyncio.run,
                    get_full_info_about_company(
                        url, company_url, annual_growth, course
                    ),
                )
            )
        for features in concurrent.futures.as_completed(features):
            results.append(features.result())
    return results


async def get_result():
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    get_course_task = asyncio.create_task(get_current_course())
    response = await fetch_response(url)
    course = await get_course_task
    return await _get_result_from(url, response, course)
