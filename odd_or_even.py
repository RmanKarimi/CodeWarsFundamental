"""
determine whether the sum of list of numbers's elements is odd or even.
If the input array is empty consider it as: [0] (array with a zero).
"""


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"
