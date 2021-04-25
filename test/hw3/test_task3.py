from All_home_works.hw3.task3 import Filter, make_filter

TEST_DATA = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
        "valid": True,
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly", "valid": True},
]


def test_filter__positive_even__all_positive_numbers():
    data = [1, 2, 3, 4]
    expected = [2, 4]
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    result = positive_even.apply(data)
    assert expected == result


def test_filter__positive_even__data_with_negative_numbers_in_data():
    data = [-2 - 1, 0, 1, 2, 3, 4]
    expected = [2, 4]
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    result = positive_even.apply(data)
    assert expected == result


def test_filter__make_functions__valid_for_only_one_dict():
    expected = TEST_DATA[1]
    result = make_filter(name="polly", type="bird").apply(TEST_DATA)
    assert expected == result[0]


def test_filter__make_functions__valid_for_all_dict():
    result = make_filter(valid=True).apply(TEST_DATA)
    assert TEST_DATA == result


def test_filter__make_functions__not_valid_for_all_dict():
    result = make_filter(valid=False).apply(TEST_DATA)
    assert [] == result


def test_filter__make_functions__not_valid_for_all_dict_with_not_existing_key():
    result = make_filter(not_valid=True).apply(TEST_DATA)
    assert not result
