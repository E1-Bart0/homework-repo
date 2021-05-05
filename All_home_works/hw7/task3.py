"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List

import numpy as np


def tic_tac_toe_checker(board: List[List]) -> str:
    result = set()
    for line in _get_all_lines(board):
        _if_all_element_same__add_to(result, line)
    return _analyze(result, board)


def _analyze(result, board):
    if not len(result) and "-" in np.ravel(board):
        return "unfinished!"
    elif len(result) % 2 == 0:
        return "draw!"
    else:
        return f"{result.pop()} wins!"


def _get_all_lines(board):
    rows = np.array(board)
    yield from rows
    yield from rows.T
    yield rows.diagonal()
    yield np.fliplr(rows).diagonal()


def _if_all_element_same__add_to(res, line):
    if len(set(line)) == 1:
        if line[0] != "-":
            res.add(line[0])
