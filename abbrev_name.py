"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
"""


def abbrev_name(name):
    return ((str(name).split())[0].upper())[0] + "." + ((str(name).split())[1].upper())[0]
