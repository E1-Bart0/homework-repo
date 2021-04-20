import string

from All_home_works.hw2.task5 import custom_range


def test_custom_range_str__start():
    assert ["a", "b", "c", "d", "e", "f"] == custom_range(string.ascii_lowercase, "g")


def test_custom_range_str__start__stop():
    assert ["g", "h", "i", "j", "k", "l", "m", "n", "o"] == custom_range(
        string.ascii_lowercase, "g", "p"
    )


def test_custom_range_str_start__stop__step():
    assert ["p", "n", "l", "j", "h"] == custom_range(
        string.ascii_lowercase, "p", "g", -2
    )


def test_custom_range_not_str():
    assert [1] == custom_range([2, 1, 0], 1, 0)
