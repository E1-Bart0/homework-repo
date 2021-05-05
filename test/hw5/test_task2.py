from All_home_works.hw5.task2 import print_result


def foo(n):
    """Takes n and return str('foo') n times"""
    return "foo" * n


def test_decorator_saving_doc_string_main_function():
    foo_with_decorator = print_result(foo)
    assert foo_with_decorator.__doc__ == foo.__doc__
    assert foo_with_decorator.__name__ == foo.__name__
    assert foo_with_decorator.__original_func == foo


def test_function_works_fine_with_decorator():
    foo_with_decorator = print_result(foo)
    assert foo(2) == foo_with_decorator(2)
