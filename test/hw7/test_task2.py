import pytest

from All_home_works.hw7.task2 import backspace_compare


@pytest.mark.parametrize(  # noqa: PT006
    "first,second,expected",
    [
        ("aB#c", "aD#c", True),
        ("A##c", "#A#c", True),
        ("#", "", True),
        ("abcABCD####", "abc", True),
    ],
)
def test__backspace_compare__with_backspace__expected_true(first, second, expected):
    result = backspace_compare(first, second)
    assert result


@pytest.mark.parametrize(  # noqa: PT006
    "first,second,expected",
    [("A#c", "b", False), ("##a", "c", False)],
)
def test__backspace_compare__with_backspace__expected_false(first, second, expected):
    result = backspace_compare(first, second)
    assert expected is result
