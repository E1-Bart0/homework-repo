from unittest.mock import Mock, call, patch

import pytest

from All_home_works.hw10.task1_save_result import SaveDataAboutCompanies


@pytest.mark.asyncio()
@patch(
    "All_home_works.hw10.task1_save_result.CollectDataAboutCompany.run",
    return_value=[{"company": 1}],
)
@patch("All_home_works.hw10.task1_save_result.SaveDataAboutCompanies.save_to_file")
@patch(
    "All_home_works.hw10.task1_save_result.SaveDataAboutCompanies.top_most_expensive_companies"
)
@patch(
    "All_home_works.hw10.task1_save_result.SaveDataAboutCompanies.top_fewest_pe_rating_companies"
)
@patch(
    "All_home_works.hw10.task1_save_result.SaveDataAboutCompanies.top_most_growth_companies"
)
@patch(
    "All_home_works.hw10.task1_save_result.SaveDataAboutCompanies.top_most_profit_companies"
)
@patch(
    "multiprocessing.pool.Pool.map",
    side_effect=lambda func, func_list: [func(f) for f in func_list],
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
    saving_class = SaveDataAboutCompanies()
    saving_class.save()
    calls = save_to_file.call_args_list
    assert saving_class.data == [{"company": 1}]
    expect = [
        call(most_expensive),
        call(fewest_pe_e),
        call(most_growth),
        call(most_profit),
    ]
    assert calls == expect


@patch("builtins.open")
@patch("All_home_works.hw10.task1_save_result.json.dump")
def test_save_to_file(dump, open_mock):
    data = []
    limit = 0
    func = Mock(return_value="result")
    func.__name__ = "name"
    saving_class = SaveDataAboutCompanies()
    saving_class.data = []
    saving_class.limit = limit
    saving_class.save_to_file(func)
    func.assert_called_once_with(data, limit)
    dump.assert_called_once()


def test_top_most_expensive_companies():
    data = [
        {"price": 3},
        {"price": 1},
        {"price": 2},
    ]
    limit = 2
    result = SaveDataAboutCompanies.top_most_expensive_companies(data, limit)
    assert result == [{"price": 3}, {"price": 2}]


def test_top_most_expensive_companies_with_limit_equals_len_data():
    data = [
        {"price": 3},
        {"price": 1},
        {"price": 2},
    ]
    limit = 3
    result = SaveDataAboutCompanies.top_most_expensive_companies(data, limit)
    assert result == [{"price": 3}, {"price": 2}, {"price": 1}]


def test_top_most_expensive_companies_with_limit_more_than_len_data():
    data = [
        {"price": 3},
        {"price": 1},
        {"price": 2},
    ]
    limit = 4
    result = SaveDataAboutCompanies.top_most_expensive_companies(data, limit)
    assert result == [{"price": 3}, {"price": 2}, {"price": 1}]


def test_top_fewest_pe_rating_companies():
    data = [
        {"P/E": 3},
        {"P/E": 1},
        {"P/E": 2},
    ]
    limit = 2
    result = SaveDataAboutCompanies.top_fewest_pe_rating_companies(data, limit)
    assert result == [{"P/E": 1}, {"P/E": 2}]


def test_top_fewest_pe_rating_companies_if_one_pe_is_none():
    data = [
        {"P/E": 3},
        {"P/E": None},
        {"P/E": 2},
    ]
    limit = 3
    result = SaveDataAboutCompanies.top_fewest_pe_rating_companies(data, limit)
    assert result == [{"P/E": 2}, {"P/E": 3}, {"P/E": None}]


def test_top_most_growth_companies():
    data = [
        {"growth": 3},
        {"growth": 1},
        {"growth": 2},
    ]
    limit = 2
    result = SaveDataAboutCompanies.top_most_growth_companies(data, limit)
    assert result == [{"growth": 3}, {"growth": 2}]


def test_top_most_growth_companies_if_one_growth_is_none():
    data = [
        {"growth": 3},
        {"growth": None},
        {"growth": 2},
    ]
    limit = 3
    result = SaveDataAboutCompanies.top_most_growth_companies(data, limit)
    assert result == [{"growth": 3}, {"growth": 2}, {"growth": None}]


def test_top_most_profit_companies():
    data = [
        {"potential profit": 3},
        {"potential profit": 1},
        {"potential profit": 2},
    ]
    limit = 2
    result = SaveDataAboutCompanies.top_most_profit_companies(data, limit)
    assert result == [
        {"potential profit": 3},
        {"potential profit": 2},
    ]


def test_top_most_profit_companies_if_one_growth_is_none():
    data = [
        {"potential profit": 3},
        {"potential profit": None},
        {"potential profit": 2},
    ]
    limit = 3
    result = SaveDataAboutCompanies.top_most_profit_companies(data, limit)
    assert result == [
        {"potential profit": 3},
        {"potential profit": 2},
        {"potential profit": None},
    ]
