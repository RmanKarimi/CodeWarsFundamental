"""
The main idea is to count all the occurring characters in a string. If you have a string like aba,
then the result should be {'a': 2, 'b': 1}.
"""


def count(string):
    count_res = {}
    for s in string:
        count_res[s] = string.count(s)
    return count_res
