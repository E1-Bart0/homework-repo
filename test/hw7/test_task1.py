import pytest

from All_home_works.hw7.task1 import find_occurrences


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({"key1": "OK", "key2": "NOT OK"}, "OK", 1),
        ({"key1": ["OK"], "key2": ["NOT OK"]}, "OK", 1),
        ({"key1": ("OK",), "key2": ("NOT OK", "OK")}, "OK", 2),
        ({"key1": {"OK"}, "key2": {"NOT OK"}}, "OK", 1),
        ({"key1": {"key1": "OK"}, "key2": {"key1": "OK"}}, "OK", 2),
        ({"key1": {"key1": ["OK"]}, "key2": {"key1": ("OK",)}}, "OK", 2),
    ],
)
def test_find_occurrences__search_string_in_values(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({"key1": "OK", "key2": "NOT OK"}, "key1", 1),
        (
            {("key1", ("key1", "key1")): {"key1": "OK"}, "key1": {"key1": "OK"}},
            "key1",
            6,
        ),
    ],
)
def test_find_occurrences__search_string_in_values_and_keys(
    input_data, element, expected
):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
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


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({("OK",): ("OK",), "key2": ("NOT OK", "OK")}, ("OK",), 2),
        ({("OK", ("OK",)): ("OK",), ("OK",): ("NOT OK", "OK")}, ("OK",), 3),
    ],
)
def test_find_occurrences__search__tuple_in_keys_and_values(
    input_data, element, expected
):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element"),
    [
        ({"key1": ["OK"]}, {"key1": ["OK"]}),
        ({"key1": ["OK", {"key1": "OK"}], "key2": ["NOT OK"]}, {"key1": "OK"}),
    ],
)
def test_find_occurrences__search__dict(input_data, element):
    assert 1 == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({"key1": 1, "key2": True}, 1, 1),
        ({"key1": [1], "key2": ["NOT OK", 1]}, 1, 2),
        ({"key1": {"key1": ["OK", 1]}, "key2": {"key1": ("OK", 1)}}, 1, 2),
    ],
)
def test_find_occurrences__search_int_in_values(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({1: "1", "key2": True}, 1, 1),
        ({1: [1], "key2": ["NOT OK", 1]}, 1, 3),
        ({(1, 2, (1, 2)): {"key1": ["OK", 1]}, "key2": {"key1": ("OK", 1)}}, 1, 4),
    ],
)
def test_find_occurrences__search_int_in_keys_and_values(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


@pytest.mark.parametrize(
    ("input_data", "element", "expected"),
    [
        ({"key1": 1, "key2": True}, True, 1),
        ({"key1": [True], "key2": ["NOT OK", False]}, True, 1),
        ({"key1": {"key1": ["OK", True]}, "key2": {"key1": ("OK", None)}}, False, 0),
    ],
)
def test_find_occurrences__search_bool(input_data, element, expected):
    assert expected == find_occurrences(input_data, element)


def test_find_occurrences__just_str__example_from_description():
    input_data = {
        "fourth": "RED",
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)


def test_find_occurrences__str_in_list__example_from_description():
    input_data = {
        "first": ["RED", "BLUE"],
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)


def test_find_occurrences__str_in_dict__example_from_description():
    input_data = {
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
        },
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)


def test_find_occurrences__str_in_list_in_dict__example_from_description():
    input_data = {
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)


def test_find_occurrences__str_in_dict_in_dict__example_from_description():
    input_data = {
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
        },
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)


def test_find_occurrences__str_in_list_in_dict_in_dict__example_from_description():
    input_data = {
        "third": {
            "complex_key": {
                "key1": "value1",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
    }
    element = "RED"
    assert 1 == find_occurrences(input_data, element)
