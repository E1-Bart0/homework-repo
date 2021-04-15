"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args, **kwargs):
        call = str(args) + str(kwargs)
        if call in memo:
            return memo[call]
        else:
            memo[call] = func(*args, **kwargs)
            return memo[call]

    return wrapper
