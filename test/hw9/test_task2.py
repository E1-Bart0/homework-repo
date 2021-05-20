import pytest

from All_home_works.hw9.task2 import Suppressor


def test_class_suppressor__catch_expected_exception():
    with Suppressor(IndexError):
        [][2]


def test_class_suppressor__catch_not_expected_exception():
    with pytest.raises(IndexError, match="list index out of range"):  # noqa: PT012
        with Suppressor(ZeroDivisionError):
            [][2]


def test_generator_suppressor__catch_expected_exception():
    with Suppressor(IndexError):
        [][2]


def test_generator_suppressor__catch_not_expected_exception():
    with pytest.raises(IndexError, match="list index out of range"):  # noqa: PT012
        with Suppressor(ZeroDivisionError):
            [][2]
