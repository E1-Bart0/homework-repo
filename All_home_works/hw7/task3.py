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
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    result = set()
    for line in _get_all_lines(board):
        if len(set(line)) == 1 and line[0] != "-":
            result.add(line[0])
    return _analyze(result, board)


def _analyze(result, board):
    if not len(result) and "-" in chain(*board):
        return "unfinished!"
    elif len(result) % 2 == 0:
        return "draw!"
    else:
        return f"{result.pop()} wins!"


def _get_all_lines(board):
    diagonal, reverse_diagonal = [], []
    for index, row in enumerate(board):
        diagonal.append(row[index])
        reverse_diagonal.append(row[len(row) - 1 - index])
        yield row
        yield [row[index] for row in board]

    yield diagonal
    yield reverse_diagonal
