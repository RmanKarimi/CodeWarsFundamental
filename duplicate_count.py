"""
count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""


def duplicate_count(text):
    i = 0
    for t in text:
        if str(text).lower().count(t) >= 2:
            text = str(text).replace(t, "")
            i += 1
    return i
