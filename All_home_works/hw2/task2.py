"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    count = Counter()
    for num in inp:
        count[num] += 1
    counter = count.most_common()
    max_common = counter[0][0] if counter[0][1] > len(inp) // 2 else None
    min_common = counter[-1][0] if counter[-2][1] != counter[-1][1] else None
    return max_common, min_common