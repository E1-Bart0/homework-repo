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
    max_sum = nums[0]
    for index in range(len(nums)):
        max_sum = _get_max_sum(max_sum, index - k, index, nums)
    return max_sum


def _get_max_sum(max_sum, index_start, index_finish, array):
    index_start = max(0, index_start + 1)
    reversed_sub_array = reversed(array[index_start : index_finish + 1])
    current_sum = 0
    for num in reversed_sub_array:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
