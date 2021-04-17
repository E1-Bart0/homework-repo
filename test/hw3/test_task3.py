import unittest

from All_home_works.hw3.task3 import Filter, make_filter, sample_data


class TestFilter(unittest.TestCase):
    def setUp(self) -> None:
        positive_even_filter_function = (
            lambda a: isinstance(a, int),
            lambda a: a % 2 == 0,
            lambda a: a > 0,
        )
        self.positive_even = Filter(positive_even_filter_function)

    def test_filter(self):
        expected = list(range(2, 100, 2))

        result = self.positive_even.apply(range(99))
        assert expected == result

    def test_filter_case__data_with_negative(self):
        expected = list(range(2, 100, 2))

        result = self.positive_even.apply(range(-100, 99))
        assert expected == result

    def test_filter__str_as_data(self):
        result = self.positive_even.apply("dsa")
        assert not result


class TestFilterMakeFunction(unittest.TestCase):
    def test_filter_make_functions_case1(self):
        expected = sample_data[1]
        dict_filter = make_filter(name="polly", type="bird")
        result = dict_filter.apply(sample_data)

        assert expected == result[0]

    def test_filter_make_functions_case2(self):
        expected = sample_data[0]
        dict_filter = make_filter(name="Bill")
        result = dict_filter.apply(sample_data)

        assert expected == result[0]

    def test_filter_make_functions_not_valid_for_all(self):
        dict_filter = make_filter(not_valid=True)
        result = dict_filter.apply(sample_data)

        assert not result

    def test_filter_make_functions_not_valid_for_one(self):
        expected = sample_data[1]
        dict_filter = make_filter(is_dead=True)
        result = dict_filter.apply(sample_data)

        assert expected == result[0]
