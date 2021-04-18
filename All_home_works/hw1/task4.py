"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    counter = 0
    max_sum = 0

    for index, current_num in enumerate(nums):
        if index < k:
            counter += current_num
            max_sum += current_num
        else:
            num_k_indexes_ago = nums[index - k]
            counter += current_num - num_k_indexes_ago
            max_sum = _get_max_sum(counter, max_sum)
    return max_sum


def _get_max_sum(counter, max_sum):
    if counter > max_sum:
        max_sum = counter
    return max_sum  # noqa: R504
