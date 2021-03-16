"""
 The goal of this exercise is to convert a string to a new string where each character in the new string is
 "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
 Ignore capitalization when determining if a character is a duplicate.
 """


def duplicate_encode(word):
    word_: object = word.lower()
    for w in word_:
        if w != "(" and w != ")":
            if str(word_).count(w) > 1:
                word_ = str(word_).replace(w, ")")
            else:
                word_ = str(word_).replace(w, "(")

    return word_