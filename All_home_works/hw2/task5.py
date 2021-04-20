"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, start=None, stop=None, step=None):
    iterable = list(iterable)
    if stop is None:
        stop = iterable.index(start)
        start = 0
    else:
        stop = iterable.index(stop)
        start = iterable.index(start)

    step = step or 1
    return iterable[start:stop:step]
