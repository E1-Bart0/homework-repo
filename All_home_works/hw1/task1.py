"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def generate_fib_sequence():
    current_num, next_num = 0, 1
    while True:
        yield current_num
        next_num, current_num = current_num + next_num, next_num


def get_fib_first_element(data, fib_sequence):
    fib_num = next(fib_sequence)
    while fib_num < data[0]:
        fib_num = next(fib_sequence)
    return fib_num


def check_fibonacci(data: Sequence[int]) -> bool:
    if not data:
        return False

    fib_sequence = generate_fib_sequence()
    fib_num = get_fib_first_element(data, fib_sequence)

    for num in data:
        if fib_num != num:
            return False
        fib_num = next(fib_sequence)
    return True
