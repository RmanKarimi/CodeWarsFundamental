import re


class PyFundamental:
    @staticmethod
    def is_isogram(self, string):
        string = string.lower()
        slist = []
        for l in string:
            if l != " ":
                if l in slist:
                    return False
                slist.append(l)
        return True

    @staticmethod
    def high_and_low(self, numbers):
        # ...
        str_numbers = str(numbers)
        int_numbers = []
        for s in str_numbers.split():
            int_numbers.append(int(s))
        _max = max(int_numbers)
        _min = min(int_numbers)
        numbers = str(_max) + " " + str(_min)
        return numbers

    @staticmethod
    def even_or_odd(number):
        return "Odd" if number % 2 == 0 else "Even"

    """
    The goal of this exercise is to convert a string to a new string where each character in the new string is
    "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
    Ignore capitalization when determining if a character is a duplicate.
    """
    @staticmethod
    def duplicate_encode(self, word):
        word = word.lower()
        for w in word:
            if w != "(" and w != ")":
                if str(word).count(w) > 1:
                    word = str(word).replace(w, ")")
                else:
                    word = str(word).replace(w, "(")

        return word

    """
    Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
    No floats or non-positive integers will be passed.
    """
    @staticmethod
    def sum_two_smallest_numbers(self, numbers):
        # min1 = min(numbers)
        # numbers.remove(min1)
        # min2 = min(numbers)
        # return min1+min2
        return sum(sorted(numbers)[:2])

    """
    Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
    
    The output should be two capital letters with a dot separating them.
    """
    @staticmethod
    def abbrev_name(self, name):
        return ((str(name).split())[0].upper())[0] + "." + ((str(name).split())[1].upper())[0]

    """
    Complete the square sum function so that it squares each number passed into it and then sums the results together.
    """
    @staticmethod
    def square_sum(self, numbers):
        return sum(num.__pow__(2) for num in numbers)

    """
    The main idea is to count all the occurring characters in a string. If you have a string like aba, 
    then the result should be {'a': 2, 'b': 1}.
    """
    @staticmethod
    def count(self, string):
        count_res = {}
        for s in string:
            count_res[s] = string.count(s)
        return count_res

    #     return {i: string.count(i) for i in string}

    """
    implementing the line numbering.
    
    Write a function which takes a list of strings and returns each line prepended by the correct number.
    
    The numbering starts at 1. The format is n: string. Notice the colon and space in between.
    """
    @staticmethod
    def number(self, lines):
        i = 1
        res = []
        for line in lines:
            res.append(f"{i}: {line}")
            # res.append("{}: {}".format(i+1, line))
            i += 1
        return res

    """
    Given an array of integers, find the one that appears an odd number of times.
    
    There will always be only one integer that appears an odd number of times.
    """
    @staticmethod
    def find_it(self, seq):
        for seqs in seq:
            if seq.count(seqs) % 2 != 0:
                return seqs

    """
    What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
    
    Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words.
    You should return an array of all the anagrams or an empty array if there are none. For example:
    
    """
    @staticmethod
    def anagrams(self, word, words):
        word_list = list(word)
        word_list.sort()
        res = []
        for wrd in words:
            str1_list = list(wrd)
            str1_list.sort()
            if str1_list == word_list:
                res.append(wrd)
        return res

    """
     take any non-negative integer as an argument and return it with its digits in descending order. 
     Essentially, rearrange the digits to create the highest possible number.
    """
    @staticmethod
    def descending_order(self, num):

        return int("".join(sorted(str(num), reverse=True)))

    """
    . Return a new sorted string, the longest possible, containing distinct letters,
    """
    @staticmethod
    def longest(self, s1, s2):
        return "".join(sorted(set(s1 + s2)))

    """
    determine whether the sum of list of numbers's elements is odd or even.
    If the input array is empty consider it as: [0] (array with a zero).
    """
    @staticmethod
    def odd_or_even(self, arr):
        return "even" if sum(arr) % 2 == 0 else "odd"

    """
     takes a number as input and returns the sum of the absolute value of each of the number's decimal digits
    """
    @staticmethod
    def sum_digits(self, number):
        sumnumbers = 0
        for numbers in str(number.__abs__()):
            sumnumbers += int(numbers)
        return sumnumbers
        # return sum(int(d) for d in str(abs(number)))

    """ 
    count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
    The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
    """
    @staticmethod
    def duplicate_count(self, text):
        i = 0
        for t in text:
            if str(text).lower().count(t) >= 2:
                text = str(text).replace(t, "")
                i += 1
        return i

    """
    subtracts one list from another and returns the result.
    It should remove all values from list a, which are present in list b.
    """
    @staticmethod
    def array_diff(self, a, b):
        for b1 in b:
            for a1 in a:
                if a1 == b1:
                    for j in range(0, list(a).count(a1)):
                        a.remove(a1)

        return a
        # return [x for x in a if x not in b]

    """
    Build Tower by the following given argument:
    number of floors (integer and always greater than 0).
    """
    @staticmethod
    def tower_builder(self, n_floors):
        return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]

    """
     returns the time in a human-readable format (HH:MM:SS) from none-negative integer value
    """
    @staticmethod
    def make_readable(self, sec):
        hours, rem = divmod(sec, 3600)
        minutes, seconds = divmod(rem, 60)

        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        # return strftime("%I:%M:%S", gmtime(sec))

    """
    sum of all the numbers between a and b including them too and return it. If the two numbers are equal return a or b.
    
    """
    @staticmethod
    def get_sum(self, a, b):
        return sum(range(min(a, b), max(a, b) + 1))

    """
    function that does four basic mathematical operations.
    The function should take three arguments - operation(string/char), value1(number), value2(number).
    The function should return result of numbers after applying the chosen operation.
    """
    @staticmethod
    def basic_op(self, operator, a, b):

        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        else:
            return a / b

    """
    array of ones and zeroes, convert the equivalent binary value to an integer.
    """
    @staticmethod
    def binary_array_to_number(self, arr):
        return int(''.join(str(i) for i in arr), 2)

    """
     function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
    """
    @staticmethod
    def add_binary(self, a, b):
        return bin(a + b)[2:]
        # return '{0:b}'.format(a + b)

    """
     function which repeats the given string src exactly count times.
    """
    @staticmethod
    def repeat_str(self, repeat, string):
        # return str("".join(string for i in range(0, repeat)))
        return repeat * string

    """
    Digital root is the recursive sum of all the digits in a number.
    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    """
    @staticmethod
    def digital_root(self, number):
        if number == 0:
            return 0
        else:
            return (number % 10) + PyFundamental.digital_root(number // 10)

    """
    Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
    You will always be given an array with five six-sided dice values.
     Three 1's => 1000 points
     Three 6's =>  600 points
     Three 5's =>  500 points
     Three 4's =>  400 points
     Three 3's =>  300 points
     Three 2's =>  200 points
     One   1   =>  100 points
     One   5   =>   50 point
    """
    @staticmethod
    def score(self, dice):
        s = 0
        if dice.count(1) >= 3:
            s += 1000
            s += int(dice.count(1) - 3) * 100
        elif dice.count(1) < 3:
            s += int(dice.count(1)) * 100
        if dice.count(2) == 3:
            s += 200
        if dice.count(3) == 3:
            s += 300
        if dice.count(4) == 3:
            s += 400
        if dice.count(5) >= 3:
            s += 500
            s += int(dice.count(5) - 3) * 100
        elif dice.count(5) < 3:
            s += int(dice.count(5)) * 50
        if dice.count(6) == 3:
            s += 600
        return s

    """
    The marketing team is spending way too much time typing in hashtags.
    Let's help them with our own Hashtag Generator!
    
    Here's the deal:
    
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
    """
    @staticmethod
    def generate_hashtag(self, s):
        res = "#"
        if 0 < len(s) < 140:
            for s1 in s.split():
                res += s1.capitalize()
            return res
        else:
            return False
        # return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

    """
    Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, 
    with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
    """
    @staticmethod
    def comp(self, array1, array2):
        array1 = sorted(array1)
        array2 = sorted(array2)
        if len(array1) > 0 and len(array2) > 0:
            for arr1 in array1:
                if arr1 * arr1 not in array2:
                    return False
                else:
                    continue
            return True

    """
    convert a string into an integer. The strings simply represent the numbers in words
    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them

    """
    @staticmethod
    def parse_int(self, string):
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

    """
    Complete the solution so that the function will break up camel casing, using a space between words.
    """
    @staticmethod
    def solution(self, s):
        return " ".join(re.findall('[a-zA-Z][^A-Z]*', s))

