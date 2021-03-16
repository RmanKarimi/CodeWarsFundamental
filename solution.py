import re

"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""


def solution(s):
    return " ".join(re.findall('[a-zA-Z][^A-Z]*', s))
