"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0

    for num_a, num_b, num_c, num_d in generate_all_variant(a, b, c, d):
        if num_a + num_b + num_c + num_d == 0:
            result += 1
    return result


def generate_all_variant(a, b, c, d):
    for num_a in a:
        for num_b in b:
            for num_c in c:
                for num_d in d:
                    yield num_a, num_b, num_c, num_d
