from unittest.mock import Mock

from All_home_works.hw3.task1 import cache


def test__cache_decorator():
    inner_function = Mock()
    inner_function_with_decorator = cache(times=3)(inner_function)
    inner_function_with_decorator()
    inner_function_with_decorator()
    inner_function_with_decorator()
    inner_function_with_decorator()
    inner_function.assert_called_once_with()
