from codefellows.dsa.linked_list import LinkedList
from sum_linked_list import sum_linked_list


def test_sum_linked_list():
    nums = LinkedList(values=[1, 2, 3, 4, 5])
    actual = sum_linked_list(nums.head)
    expected = 15
    assert actual == expected
