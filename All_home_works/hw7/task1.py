"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    if tree == element and type(tree) == type(element):
        counter += 1
    elif isinstance(tree, (tuple, set, list)):
        counter += find_occurrences_in_list(tree, element)
    elif isinstance(tree, dict):
        counter += find_occurrences_in_dict(tree, element)
    return counter


def find_occurrences_in_list(array, element):
    counter = 0
    for new_element in array:
        counter += find_occurrences(new_element, element)
    return counter


def find_occurrences_in_dict(dictionary, element):
    counter = 0
    for key, value in dictionary.items():
        counter += find_occurrences(key, element)
        counter += find_occurrences(value, element)
    return counter
