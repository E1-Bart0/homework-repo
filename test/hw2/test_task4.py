from All_home_works.hw2.task4 import cache


def test_cache():
    some = 100, 200

    cache_fun = cache(func)
    val1 = cache_fun(*some)
    val2 = cache_fun(*some)
    assert val1 is val2


def func(a, b):
    return (a ** b) ** 2
