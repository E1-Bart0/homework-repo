import pytest

from All_home_works.hw7.task2 import backspace_compare


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("aB#c", "aD#c"),
        ("A##c", "#A#c"),
        ("#", ""),
        ("abcABCD####", "abc"),
    ],
)
def test__backspace_compare__with_backspace__expected_true(first, second):
    result = backspace_compare(first, second)
    assert result


@pytest.mark.parametrize(
    ("first", "second"),
    [("A#c", "b"), ("##a", "c")],
)
def test__backspace_compare__with_backspace__expected_false(first, second):
    result = backspace_compare(first, second)
    assert not result
