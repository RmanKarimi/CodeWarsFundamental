"""
convert a string into an integer. The strings simply represent the numbers in words
The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

"""


def parse_int(string):
    numberDict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
        "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90,
        "hundred": 100, "thousand": 1000, "mililion": 1000000
    }

    strNumber = string.replace("-", " ").split()
    res = 0
    i = 0
    for strNumbers in strNumber:
        if strNumbers != "and":
            if strNumbers.__contains__("hundred") or strNumbers.__contains__("thousand"):
                i += 1
                res *= int(numberDict[strNumbers])
            else:
                res += int(numberDict[strNumbers])

    return res
