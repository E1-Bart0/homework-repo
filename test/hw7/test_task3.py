import pytest

from All_home_works.hw7.task3 import tic_tac_toe_checker


@pytest.mark.parametrize(  # noqa: PT006
    "input_data, expected",
    [
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["o", "o", "o"], ["x", "x", "o"], ["x", "o", "x"]], "o wins!"),
    ],
)
def test_tic_tac_toe_checker__return_win_in_row(input_data, expected):
    assert expected == tic_tac_toe_checker(input_data)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data, expected",
    [
        ([["o", "x", "o"], ["-", "x", "x"], ["x", "x", "o"]], "x wins!"),
        ([["o", "o", "o"], ["x", "x", "o"], ["x", "o", "o"]], "o wins!"),
    ],
)
def test_tic_tac_toe_checker__return_win_in_column(input_data, expected):
    assert expected == tic_tac_toe_checker(input_data)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data, expected",
    [
        ([["x", "o", "o"], ["-", "x", "x"], ["o", "o", "x"]], "x wins!"),
        ([["x", "x", "o"], ["x", "o", "o"], ["o", "x", "x"]], "o wins!"),
    ],
)
def test_tic_tac_toe_checker__return_win_in_diagonal(input_data, expected):
    assert expected == tic_tac_toe_checker(input_data)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data, expected",
    [
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished!"),
        ([["o", "x", "o"], ["x", "-", "o"], ["o", "x", "x"]], "unfinished!"),
    ],
)
def test_tic_tac_toe_checker__return_unfinished(input_data, expected):
    assert expected == tic_tac_toe_checker(input_data)


@pytest.mark.parametrize(  # noqa: PT006
    "input_data, expected",
    [
        ([["o", "x", "x"], ["x", "o", "o"], ["o", "x", "x"]], "draw!"),
        ([["x", "x", "x"], ["o", "o", "o"], ["x", "o", "x"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker__return_draw(input_data, expected):
    assert expected == tic_tac_toe_checker(input_data)
