"""
Google FooBar problem 1
Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely
"""


def solution(nums, n):

    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    return [num for num in nums if counts[num] <= n]
