"""
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
"""


def digital_root(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + digital_root(number // 10)
