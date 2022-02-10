import pytest
from remove_popular import solution


def test_solution_simple():
    actual = solution([1], 0)
    expected = []
    assert actual == expected


def test_solution():
    actual = solution([1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 4, 2, 4], 3)
    expected = [3, 5, 6, 6]
    assert actual == expected
