"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    for seqs in seq:
        if seq.count(seqs) % 2 != 0:
            return seqs
