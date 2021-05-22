"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import Counter
from typing import List


def generate_sum_of_all_variant_of_two_lists(list1, list2):
    for num1 in list1:
        for num2 in list2:
            yield num1 + num2


def solution_with_n_in_2(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0
    a_b = Counter(generate_sum_of_all_variant_of_two_lists(a, b))
    d_c = Counter(generate_sum_of_all_variant_of_two_lists(d, c))
    for sum_a__b, counter in a_b.items():
        if -sum_a__b in d_c:
            result += counter * d_c[-sum_a__b]
    return result


def solution_with_n_in_3(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0
    d = Counter(d)
    for num_a, num_b, num_c in generate_all_variant_of_three_lists(a, b, c):
        sum_of_three = num_a + num_b + num_c
        if -sum_of_three in d:
            result += d[-sum_of_three]
    return result


def generate_all_variant_of_three_lists(a, b, c):
    for num_a in a:
        for num_b in b:
            for num_c in c:
                yield num_a, num_b, num_c
