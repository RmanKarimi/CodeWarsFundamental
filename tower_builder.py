"""
 Build Tower by the following given argument:
 number of floors (integer and always greater than 0).
 """


def tower_builder(n_floors):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]