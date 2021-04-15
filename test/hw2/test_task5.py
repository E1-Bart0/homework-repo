import string

from All_home_works.hw2.task5 import custom_range


def test_custom_range_str_case1():
    assert ["a", "b", "c", "d", "e", "f"] == custom_range(string.ascii_lowercase, "g")


def test_custom_range_str_case2():
    assert ["g", "h", "i", "j", "k", "l", "m", "n", "o"] == custom_range(
        string.ascii_lowercase, "g", "p"
    )


def test_custom_range_str_case3():
    assert ["p", "n", "l", "j", "h"] == custom_range(
        string.ascii_lowercase, "p", "g", -2
    )
