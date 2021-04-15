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
    res, nums = [], []
    if args:
        recursion(res, nums, args)
    return res


def recursion(res, nums, args, index=0):
    for num in args[index]:
        nums.append(num)
        if len(args) == index + 1:
            res.append(nums.copy())
        else:
            recursion(res, nums, args, index=index + 1)
        nums.pop()
    return res
