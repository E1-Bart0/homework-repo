"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def backspace_compare(first: str, second: str) -> bool:
    first_gen = get_filtered(first)
    second_gen = get_filtered(second)
    return all(
        char1 == char2
        for char1, char2 in zip_longest(first_gen, second_gen, fillvalue=False)
    )


def get_filtered(string):  # noqa: CCR001
    counter = 0
    for char in reversed(string):
        if char == "#":
            counter += 1
        elif char != "#" and counter:
            counter -= 1
        else:
            yield char
