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
    queue = []
    max_sum = nums[0]

    for num in nums:
        if len(queue) == k:
            queue.pop(0)
        queue.append(num)

        max_sum = get_max_sum(max_sum, queue)

    return max_sum


def get_max_sum(max_sum, queue):
    queue_copy = queue.copy()
    while len(queue_copy):
        if sum(queue_copy) > max_sum:
            max_sum = sum(queue_copy)
        queue_copy.pop(0)
    return max_sum
