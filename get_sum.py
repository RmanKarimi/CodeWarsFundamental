"""
 sum of all the numbers between a and b including them too and return it. If the two numbers are equal return a or b.
 """


def get_sum(self, a, b):
    return sum(range(min(a, b), max(a, b) + 1))
