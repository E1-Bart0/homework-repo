from unittest.mock import Mock, call

from All_home_works.hw3.task1 import cache


def test__cache_decorator():
    inner_function = Mock()
    inner_function_with_decorator = cache(times=2)(inner_function)
    inner_function_with_decorator(1)
    inner_function_with_decorator(2)
    inner_function_with_decorator(1)
    inner_function_with_decorator(1)
    inner_function_with_decorator(2)
    inner_function_with_decorator(2)

    inner_function_with_decorator(1)
    assert inner_function.call_args_list == [call(1), call(2), call(1)]
