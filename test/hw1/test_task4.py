from All_home_works.hw1.task4 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum__init_data__end_subarray():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = 16
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__middle_subarray():
    nums = [0, 0, 10, 10, 0, 0]
    k = 2
    result = 20
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__start_subarray():
    nums = [110, -10, 50, 10, 0]
    k = 3
    result = 150
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__less_k_in_end():
    nums = [10, 1, 10, 0, -10, -100, 100]
    k = 3
    result = 100
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__less_k_in_middle():
    nums = [10, 10, -100, 20, 100, -100, 10]
    k = 4
    result = 120
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__less_k_in_start():
    nums = [100, 20, -100, 10, 10, 0]
    k = 4
    result = 120
    assert result == find_maximal_subarray_sum(nums, k)
