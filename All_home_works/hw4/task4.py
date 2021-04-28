"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def compare_number_if_fizzbuzz(number):
    """
    Any number divisible by three is replaced by the word fizz,
    >>> compare_number_if_fizzbuzz(3)
    'Fizz'

    Any number divisible by five by the word buzz.
    >>> compare_number_if_fizzbuzz(5)
    'Buzz'

    Numbers divisible by 15 become fizz buzz
    >>> compare_number_if_fizzbuzz(15)
    'Fizz Buzz'

    Else return number
    >>> compare_number_if_fizzbuzz(1)
    '1'
    """
    if number % 15 == 0:
        return "Fizz Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    return str(number)


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']

    """
    return list(map(compare_number_if_fizzbuzz, range(1, n + 1)))
