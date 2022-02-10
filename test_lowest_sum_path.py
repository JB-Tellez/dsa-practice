from lowest_sum_path import sum_lowest_path


def test_sum_lowest_path():
    nums = [[1, 2, 3], [1, 2, 4], [6, 3, 5]]

    assert sum_lowest_path(nums) == 12
