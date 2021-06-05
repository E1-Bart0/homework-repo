from unittest.mock import Mock, call, patch

import pytest

from All_home_works.hw10.task1_save_result import (
    save,
    save_to_file,
    top_fewest_pe_rating_companies,
    top_most_expensive_companies,
    top_most_growth_companies,
    top_most_profit_companies,
)


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_save_result.get_result", return_value=[{"company": 1}]
)
@patch("All_home_works.hw10.task1_save_result.save_to_file")
@patch("All_home_works.hw10.task1_save_result.top_most_expensive_companies")
@patch("All_home_works.hw10.task1_save_result.top_fewest_pe_rating_companies")
@patch("All_home_works.hw10.task1_save_result.top_most_growth_companies")
@patch("All_home_works.hw10.task1_save_result.top_most_profit_companies")
@patch(
    "multiprocessing.pool.Pool.starmap",
    side_effect=lambda func, data: [func(d) for d in data],
)
def test_save(
    pool,
    most_profit,
    most_growth,
    fewest_pe_e,
    most_expensive,
    save_to_file,
    get_result,
):
    save()
    calls = save_to_file.call_args_list
    expect = [
        call((most_expensive, [{"company": 1}])),
        call((fewest_pe_e, [{"company": 1}])),
        call((most_growth, [{"company": 1}])),
        call((most_profit, [{"company": 1}])),
    ]
    assert calls == expect


@patch("builtins.open")
@patch("All_home_works.hw10.task1_save_result.json.dump")
def test_save_to_file(dump, open_mock):
    data = []
    func = Mock(return_value="result")
    func.__name__ = "name"
    save_to_file(func, data)
    func.assert_called_once_with(data)
    dump.assert_called_once()


def test_top_most_expensive_companies():
    data = [
        {"price": 3},
        {"price": 1},
        {"price": 2},
    ]
    result = top_most_expensive_companies(data)
    assert result == [{"price": 3}, {"price": 2}, {"price": 1}]


def test_top_fewest_pe_rating_companies():
    data = [
        {"P/E": 3},
        {"P/E": 1},
        {"P/E": 2},
    ]
    result = top_fewest_pe_rating_companies(data)
    assert result == [{"P/E": 1}, {"P/E": 2}, {"P/E": 3}]


def test_top_fewest_pe_rating_companies_if_one_pe_is_none():
    data = [
        {"P/E": 3},
        {"P/E": None},
        {"P/E": 2},
    ]
    result = top_fewest_pe_rating_companies(data)
    assert result == [{"P/E": 2}, {"P/E": 3}, {"P/E": None}]


def test_top_most_growth_companies():
    data = [
        {"growth": 3},
        {"growth": 1},
        {"growth": 2},
    ]
    result = top_most_growth_companies(data)
    assert result == [{"growth": 3}, {"growth": 2}, {"growth": 1}]


def test_top_most_growth_companies_if_one_growth_is_none():
    data = [
        {"growth": 3},
        {"growth": None},
        {"growth": 2},
    ]
    result = top_most_growth_companies(data)
    assert result == [{"growth": 3}, {"growth": 2}, {"growth": None}]


def test_top_most_profit_companies():
    data = [
        {"potential profit": 3},
        {"potential profit": 1},
        {"potential profit": 2},
    ]
    result = top_most_profit_companies(data)
    assert result == [
        {"potential profit": 3},
        {"potential profit": 2},
        {"potential profit": 1},
    ]


def test_top_most_profit_companies_if_one_growth_is_none():
    data = [
        {"potential profit": 3},
        {"potential profit": None},
        {"potential profit": 2},
    ]
    result = top_most_profit_companies(data)
    assert result == [
        {"potential profit": 3},
        {"potential profit": 2},
        {"potential profit": None},
    ]
