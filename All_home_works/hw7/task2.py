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


def backspace_compare(first: str, second: str) -> bool:
    return get_filtered(first) == get_filtered(second)


def get_filtered(string):
    def filter_function(args):
        index, char = args
        next_char_index = min(index + 1, len(string) - 1)
        if char == "#" or string[next_char_index] == "#":
            return False
        return True

    filtered = filter(filter_function, enumerate(string))
    return [item[1] for item in filtered]
