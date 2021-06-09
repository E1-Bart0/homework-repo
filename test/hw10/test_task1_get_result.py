from unittest.mock import call, patch

import pytest
from aiohttp import InvalidURL
from bs4 import BeautifulSoup

from All_home_works.hw10.task1_get_result import (
    CollectDataAboutCompany,
    fetch_response,
    get_current_course,
)


class MockResponse:
    def __init__(self, text, status):
        self.__text = text
        self.status = status

    async def text(self):
        return self.__text

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_get_result.aiohttp.ClientSession.get",
    return_value=MockResponse(status=200, text="<div>"),
)
async def test_fetch_response__works(get):
    url = "Fake URL"
    response = await fetch_response(url)
    assert response == "<div>"


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_get_result.aiohttp.ClientSession.get",
    side_effect=InvalidURL("Fake URL"),
)
async def test_fetch_response__bad_url(get):
    url = "Fake URL"
    with pytest.raises(InvalidURL, match="Fake"):
        await fetch_response(url)


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_get_result.fetch_response",
    return_value='<Valute ID="R01235"><Value>74,1373</Value></Valute>',
)
async def test_get_current_course__parse_current_course(get):
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    result = await get_current_course()
    get.assert_called_once_with(url)
    assert result == 74.1373


@pytest.mark.asyncio()
@patch("All_home_works.hw10.task1_get_result.CollectDataAboutCompany.URL", "url")
@patch("All_home_works.hw10.task1_get_result.fetch_response", return_value="response")
@patch("All_home_works.hw10.task1_get_result.get_current_course", return_value=2.0)
@patch(
    "All_home_works.hw10.task1_get_result.CollectDataAboutCompany.collect_html_for_company",
    return_value="html",
)
@patch(
    "All_home_works.hw10.task1_get_result.CollectDataAboutCompany.parse_company_url_annual_growth_from_main_table",
    return_value=iter(
        [("/company_page_content/1", 10.0), ("/company_page_content/2", -10.0)]
    ),
)
async def test_collect_companies_html_annual_growth(
    parse_companies_url, collect_html, get_course, get_response
):
    collector = CollectDataAboutCompany()
    result = await collector.collect_companies_html_annual_growth()
    get_response.assert_called_once_with("url")
    get_course.assert_called_once()
    parse_companies_url.assert_called_once_with(get_response.return_value)
    calls = collect_html.call_args_list
    assert calls == [call("/company_page_content/1"), call("/company_page_content/2")]
    assert list(result) == [("html", 10.0), ("html", -10.0)]
    assert collector.course == 2.0


@pytest.mark.asyncio()
@patch("All_home_works.hw10.task1_get_result.fetch_response", return_value="text")
@patch("All_home_works.hw10.task1_get_result.CollectDataAboutCompany.MAIN_URL", "url/")
async def test_collect_html_for_company(get_response):
    result = await CollectDataAboutCompany().collect_html_for_company("company/1")
    get_response.assert_called_once_with("url/company/1")
    assert result == "text"


@patch(
    "All_home_works.hw10.task1_get_result.CollectDataAboutCompany.find_p_e_ratio_and_profit",
    return_value=[1.11, 50.0],
)
def test_get_company_as_a_dict(
    mock_find,
):
    request = (
        '<div class="price-section__row">'
        "<span>3M Co.</span>"
        "<span> Stock<span>, MMM</span></span>"
        "<span>203.20</span>"
        "</div>"
    )
    collector = CollectDataAboutCompany()
    collector.course = 1
    annual_growth = -10.0
    result = collector.get_company_as_a_dict(request, annual_growth)
    expected = {
        "code": "MMM",
        "name": "3M Co.",
        "price": 203.2,
        "P/E": 1.11,
        "growth": -10.0,
        "potential profit": 50.0,
    }
    assert expected == result
    mock_find.assert_called_once()


def test_find_p_e_ratio_and_profit_is_ok():
    request = (
        '<div class="snapshot">'
        "<div>100"
        "<div>52 Week Low</div>"
        "</div>"
        "<div>200.0<div>52 Week High</div>"
        "</div>"
        "<div>19.9<div>P/E Ratio</div>"
        "</div>"
        "</div>"
    )
    soup = BeautifulSoup(request, features="html.parser")
    profit = 100.0
    result = CollectDataAboutCompany().find_p_e_ratio_and_profit(soup)
    expected = 19.9, profit
    assert result == expected


def test_find_p_e_ratio_and_profit__if_coma_in_value():
    request = (
        '<div class="snapshot">'
        "<div>1,000.00"
        "<div>52 Week Low</div>"
        "</div>"
        "<div>2,000.00<div>52 Week High</div>"
        "</div>"
        "<div>1,900.1<div>P/E Ratio</div>"
        "</div>"
        "</div>"
    )
    soup = BeautifulSoup(request, features="html.parser")
    result = CollectDataAboutCompany().find_p_e_ratio_and_profit(soup)
    assert result == (1900.1, 100.0)


def test_find_p_e_ratio_and_profit__if_week_low_and_week_high_is_none():
    request = '<div class="snapshot">' "<div>10.0<div>P/E Ratio</div>" "</div>" "</div>"
    soup = BeautifulSoup(request, features="html.parser")
    result = CollectDataAboutCompany().find_p_e_ratio_and_profit(soup)
    assert result == (10.0, None)


def test_find_p_e_ratio_and_profit__if_all_is_none():
    request = '<div class="snapshot">' "</div>"
    soup = BeautifulSoup(request, features="html.parser")
    result = CollectDataAboutCompany().find_p_e_ratio_and_profit(soup)
    assert result == (None, None)


def test_parse_company_url_annual_growth_from_main_table():
    response = (
        "<tr>"
        "<td><h1>NAME</h1></td>"
        "<td><h1>1 Year +/-%</h1></td>"
        "</tr>"
        "<tr></tr>"
        "<tr>"
        '<td><a href="/company/test"></a></td>'
        "<td><span>2%</span></td>"
        "<td><span>1%</span></td>"
        "</tr>"
    )
    result = CollectDataAboutCompany().parse_company_url_annual_growth_from_main_table(
        response
    )
    assert list(result) == [("/company/test", 1.0)]


@patch(
    "All_home_works.hw10.task1_get_result.CollectDataAboutCompany.collect_companies_html_annual_growth",
    return_value=[("html1", 1.0), ("html2", 2.0)],
)
@patch(
    "All_home_works.hw10.task1_get_result.CollectDataAboutCompany.get_company_as_a_dict",
    return_value={"company": "ok"},
)
@patch(
    "multiprocessing.pool.Pool.starmap",
    side_effect=lambda func, data: [func(d) for d in data],
)
def test_run_is_ok(pool, get_dict, collect):
    result = CollectDataAboutCompany().run()
    collect.assert_called_once()
    assert get_dict.call_args_list == [call(("html1", 1.0)), call(("html2", 2.0))]
    assert result == [{"company": "ok"}, {"company": "ok"}]
