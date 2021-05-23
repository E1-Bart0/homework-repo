"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
 Modify it to be a parametrized decorator, so that the following code:

 @cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""


def cache(times=0):
    def wrapper(func):
        memo = {}

        def inner_wrapper(*args, **kwargs):
            call = frozenset(args) | frozenset(kwargs)

            if not _check_call_in_memo(call, memo):
                memo[call] = {"result": func(*args, **kwargs), "counter": times}

            return memo[call]["result"]

        return inner_wrapper

    return wrapper


def _check_call_in_memo(call, memo):
    if call in memo and memo[call]["counter"] > 0:
        memo[call]["counter"] -= 1
        return True
    return False
