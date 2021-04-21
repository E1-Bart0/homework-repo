from All_home_works.hw3.task3 import Filter, make_filter, sample_data


def test_filter():
    expected = list(range(2, 100, 2))
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    result = positive_even.apply(range(99))
    assert expected == result


def test_filter_case__data_with_negative():
    expected = list(range(2, 100, 2))
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    result = positive_even.apply(range(-99, 99))
    assert expected == result


def test_filter_make_functions_valid_for_second():
    expected = sample_data[1]
    result = make_filter(name="polly", type="bird").apply(sample_data)
    assert expected == result[0]


def test_filter_make_functions_valid_for_first():
    expected = sample_data[0]
    result = make_filter(name="Bill").apply(sample_data)
    assert expected == result[0]


def test_filter_make_functions_not_valid_for_all():
    result = make_filter(not_valid=True).apply(sample_data)
    assert not result
