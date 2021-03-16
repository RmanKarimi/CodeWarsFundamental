"""
implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""


def number(lines):
    i = 1
    res = []
    for line in lines:
        res.append(f"{i}: {line}")
        # res.append("{}: {}".format(i+1, line))
        i += 1
    return res
