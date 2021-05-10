from unittest.mock import call, patch

import pytest
from aiohttp import InvalidURL
from bs4 import BeautifulSoup

from All_home_works.hw10.task1_get_result import (
    _find_values_for_company,
    _get_additional_info_about_company,
    _get_result_from,
    fetch_response,
    get_company_url_from_main_table,
    get_current_course,
    get_full_info_about_company,
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
    return_value=MockResponse(status=404, text="<div>"),
)
async def test_fetch_response__status_not_200(get):
    url = "Fake URL"
    with pytest.raises(ValueError, match="Response should be 200, got:"):
        await fetch_response(url)


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
@patch("All_home_works.hw10.task1_get_result.time")
@patch(
    "All_home_works.hw10.task1_get_result.aiohttp.ClientSession.get",
    return_value=MockResponse(
        status=200, text='<Valute ID="R01235"><Value>74,1373</Value>=</Valute>'
    ),
)
async def test_get_current_course__parse_current_course__returns_correct_value(
    get, time
):
    time.strftime.return_value = "NOW"
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=NOW"
    result = await get_current_course()
    get.assert_called_once_with(url)
    assert result == 74.1373


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_get_result._find_values_for_company",
    return_value=iter([1.11, 2.00, 3.00]),
)
async def test_get_additional_info_about_company_returns_correct_value(  # noqa: PT019
    _find_values_for_company,
):
    request = (
        '<div class="price-section__row">'
        "<span>3M Co.</span>"
        "<span> Stock<span>, MMM</span></span>"
        "<span>203.20</span>"
        "</div>"
    )
    annual_growth = "-10%"
    course = 1
    result = await _get_additional_info_about_company(request, annual_growth, course)
    expected = {
        "code": "MMM",
        "name": "3M Co.",
        "price": 203.2,
        "P/E": 1.11,
        "growth": -10.0,
        "potential profit": 50.0,
    }
    assert expected == result


@pytest.mark.asyncio()
async def test_find_values_for_company_returns_correct_value():
    request = (
        '<div class="snapshot">'
        "<div>131.12"
        "<div>52 Week Low</div>"
        "</div>"
        "<div>203.87<div>52 Week High</div>"
        "</div>"
        "<div>19.9<div>P/E Ratio</div>"
        "</div>"
        "</div>"
    )
    soup = BeautifulSoup(request, features="html.parser")
    result = _find_values_for_company(soup)
    expected = [19.9, 131.12, 203.87]
    assert expected == list(result)


@pytest.mark.asyncio()
async def test_find_values_for_company_returns_correct_value_if_coma_in_value():
    request = (
        '<div class="snapshot">'
        "<div>1,000.12"
        "<div>52 Week Low</div>"
        "</div>"
        "<div>2,000.87<div>52 Week High</div>"
        "</div>"
        "<div>1,900.1<div>P/E Ratio</div>"
        "</div>"
        "</div>"
    )
    soup = BeautifulSoup(request, features="html.parser")
    result = _find_values_for_company(soup)
    expected = [1900.1, 1000.12, 2000.87]
    assert expected == list(result)


@pytest.mark.asyncio()
async def test_find_values_for_company_returns_correct_value_if_something_is_none():
    request = '<div class="snapshot">' "</div>"
    soup = BeautifulSoup(request, features="html.parser")
    result = _find_values_for_company(soup)
    expected = [None, None, None]
    assert expected == list(result)


@pytest.mark.asyncio()
@patch("All_home_works.hw10.task1_get_result.fetch_response", return_value="response")
@patch(
    "All_home_works.hw10.task1_get_result._get_additional_info_about_company",
    return_value="additional_info",
)
async def test_get_full_info_about_company_returns_correct_value(
    get_additional_info_about_company, fetch_response
):
    url = "test//main.test/add/info"
    company_url = "/company/1"
    annual_growth = "-10%"
    course = 1
    result = await get_full_info_about_company(url, company_url, annual_growth, 1)

    fetch_response.assert_called_once_with("test//main.test/company/1")
    get_additional_info_about_company.assert_called_once_with(
        "response", annual_growth, course
    )
    assert result == "additional_info"


@pytest.mark.asyncio()
async def test_get_company_url_from_main_table():
    response = (
        "<tr>"
        "<td><h1>NAME</h1></td>"
        "<td><h1>1 Year +/-%</h1></td>"
        "</tr>"
        "<tr></tr>"
        "<tr>"
        '<td><a href="/company/test"></a></td>'
        "<td><span>1%</span></td>"
        "</tr>"
    )
    result = get_company_url_from_main_table(response)
    assert [("/company/test", "1%")] == list(result)


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_get_result.get_company_url_from_main_table",
    return_value=iter([("/company/1", "10%"), ("company/2", "-10%")]),
)
@patch(
    "All_home_works.hw10.task1_get_result.get_full_info_about_company",
    return_value={"result": "OK"},
)
async def test_get_result_from(get_info_about_company, get_company_url_from_main_table):
    url = "test/url"
    response = "test/response"
    course = 1
    res = await _get_result_from(url, response, course)
    get_company_url_from_main_table.assert_called_once_with(response)
    assert get_info_about_company.call_args_list == [
        call("test/url", "/company/1", "10%", 1),
        call("test/url", "company/2", "-10%", 1),
    ]
    assert res == [{"result": "OK"}, {"result": "OK"}]
