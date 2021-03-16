"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements,
with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
"""


def comp(array1, array2):
    array1 = sorted(array1)
    array2 = sorted(array2)
    if len(array1) > 0 and len(array2) > 0:
        for arr1 in array1:
            if arr1 * arr1 not in array2:
                return False
            else:
                continue
        return True