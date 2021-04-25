from All_home_works.hw3.task1 import cache

N = 4


@cache(times=N)
def f(attr=None):
    return attr


def test__cache():
    input_data = 1
    solution = f(input_data)
    assert solution is f()
    assert solution is f()
    assert solution is f()
    assert solution is f()
    assert solution is not f()
