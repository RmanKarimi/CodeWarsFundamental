"""
  takes a number as input and returns the sum of the absolute value of each of the number's decimal digits
 """


def sum_digits(number):
    sumnumbers = 0
    for numbers in str(number.__abs__()):
        sumnumbers += int(numbers)
    return sumnumbers
    # return sum(int(d) for d in str(abs(number)))