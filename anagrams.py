"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:
"""


def anagrams(word, words):
    word_list = list(word)
    word_list.sort()
    res = []
    for wrd in words:
        str1_list = list(wrd)
        str1_list.sort()
        if str1_list == word_list:
            res.append(wrd)
    return res
