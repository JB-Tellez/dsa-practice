from codefellows.dsa.queue import Queue
from min_value_in_queue import min_value


def test_min_value():
    q = Queue()
    nums = [1, 4, 2, 7, 3, -2, 0]
    for num in nums:
        q.enqueue(num)

    actual = min_value(q)
    expected = -2
    assert actual == expected
