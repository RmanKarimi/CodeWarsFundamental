"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.
"""


def sum_two_smallest_numbers(numbers):
    # min1 = min(numbers)
    # numbers.remove(min1)
    # min2 = min(numbers)
    # return min1+min2
    return sum(sorted(numbers)[:2])