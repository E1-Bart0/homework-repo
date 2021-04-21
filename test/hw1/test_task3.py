from All_home_works.hw1.task3 import solution_with_n_in_2


def test_check_sum_of_four():
    data = [[7, -7, -5], [-7, 5, -2], [-7, 0, -10], [-3, 0, 2]]

    result = solution_with_n_in_2(*data)
    assert 4 == result


def test_check_sum_of_four_with_zeros():
    data = [[0, 0], [0, 0], [0, 0], [0, 0]]

    result = solution_with_n_in_2(*data)
    assert 2 ** 4 == result
