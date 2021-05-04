from All_home_works.hw5.task2 import print_result


def foo():
    """Return str('foo')"""
    return "foo"


def test_doc_string():
    foo_with_decorator = print_result(foo)
    assert foo_with_decorator.__doc__ == "Return str('foo')"
    assert foo_with_decorator.__name__ == "foo"
    assert foo_with_decorator.__original_func == foo
