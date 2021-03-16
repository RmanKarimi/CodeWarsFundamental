"""
 subtracts one list from another and returns the result.
 It should remove all values from list a, which are present in list b.
 """


def array_diff(a, b):
    for b1 in b:
        for a1 in a:
            if a1 == b1:
                for j in range(0, list(a).count(a1)):
                    a.remove(a1)

    return a
    # return [x for x in a if x not in b]