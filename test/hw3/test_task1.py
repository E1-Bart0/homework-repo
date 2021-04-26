from unittest.mock import patch

from All_home_works.hw3.task1 import cache


@cache(times=2)
def f():
    return input("? ")


@patch("hw3.test_task1.f", return_value=2)
def test__cache(f):
    function = cache(3)(f)
    function()
    function()
    function()
    function()
    assert 1 == len(f.mock_calls)
