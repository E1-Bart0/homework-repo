import pytest

from All_home_works.hw7.task1 import find_occurrences


@pytest.mark.parametrize(  # noqa: PT006
    "input_data,element,expected",
    [
        ({"key1": "OK", "key2": "NOT OK"}, "OK", 1),
        ({"key1": ["OK"], "key2": ["NOT OK"]}, "OK", 1),
        ({"key1": ("OK",), "key2": ("NOT OK", "OK")}, "OK", 2),
        ({"key1": {"OK"}, "key2": {"NOT OK"}}, "OK", 1),
        ({"key1": {"key1": "OK"}, "key2": {"key1": "OK"}}, "OK", 2),
        ({"key1": {"key1": ["OK"]}, "key2": {"key1": ("OK",)}}, "OK", 2),
    ],
)
def test_find_occurrences__search_string(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data,element,expected",
    [
        ({"key1": ["OK"], "key2": ["NOT OK"]}, ["OK"], 1),
        ({"key1": ("OK",), "key2": ("NOT OK", "OK")}, ("OK",), 1),
        ({"key1": {"OK"}, "key2": {"NOT OK"}}, {"OK"}, 1),
        ({"key1": {"key1": ["OK"]}, "key2": {"key1": ("OK",)}}, ["OK"], 1),
        (
            {"key1": {"key1": ["OK"]}, "key2": {"key1": ("OK", {"key1": ["OK"]})}},
            ["OK"],
            2,
        ),
    ],
)
def test_find_occurrences__search__list__tuple__set(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data,element,expected",
    [
        ({"key1": ["OK"]}, {"key1": ["OK"]}, 1),
        ({"key1": ["OK", {"key1": "OK"}], "key2": ["NOT OK"]}, {"key1": "OK"}, 1),
    ],
)
def test_find_occurrences__search__dict(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data,element,expected",
    [
        ({"key1": 1, "key2": True}, 1, 1),
        ({"key1": [1], "key2": ["NOT OK", 1]}, 1, 2),
        ({"key1": {"key1": ["OK", 1]}, "key2": {"key1": ("OK", 1)}}, 1, 2),
    ],
)
def test_find_occurrences__search_int(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data,element,expected",
    [
        ({"key1": 1, "key2": True}, True, 1),
        ({"key1": [True], "key2": ["NOT OK", False]}, True, 1),
        ({"key1": {"key1": ["OK", True]}, "key2": {"key1": ("OK", None)}}, False, 0),
    ],
)
def test_find_occurrences__search_bool(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


def test_find_occurrences__many_occurrences__example_from_description():
    input_data = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    element = "RED"
    expected = 6
    assert expected == find_occurrences(input_data, element)
