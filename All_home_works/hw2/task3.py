"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    accumulator = []
    if args:
        recursion(accumulator, args)
    return accumulator


def recursion(accumulator, args, index=0, nums=None):  # noqa: CCR001
    nums = nums or []
    for num in args[index]:
        nums.append(num)
        if len(args) == index + 1:
            accumulator.append(nums.copy())
        else:
            recursion(accumulator, args, index=index + 1, nums=nums)
        nums.pop()
