"""
. Return a new sorted string, the longest possible, containing distinct letters,
"""


@staticmethod
def longest(self, s1, s2):
    return "".join(sorted(set(s1 + s2)))
