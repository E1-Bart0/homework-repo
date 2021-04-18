from All_home_works.hw1.task4 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum__init_data__end_subarray():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = 16
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__middle_subarray():
    nums = [0, 10, 10, 0]
    k = 2
    result = 20
    assert result == find_maximal_subarray_sum(nums, k)


def test_find_maximal_subarray_sum__start_subarray():
    nums = [100, -10, 10, 10, 0]
    k = 3
    result = 100
    assert result == find_maximal_subarray_sum(nums, k)


if __name__ == "__main__":
    test_find_maximal_subarray_sum__init_data__end_subarray()
    test_find_maximal_subarray_sum__middle_subarray()
    test_find_maximal_subarray_sum__start_subarray()
