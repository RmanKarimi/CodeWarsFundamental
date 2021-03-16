def high_and_low(numbers):
    # ...
    str_numbers = str(numbers)
    int_numbers = []
    for s in str_numbers.split():
        int_numbers.append(int(s))
    _max = max(int_numbers)
    _min = min(int_numbers)
    numbers = str(_max) + " " + str(_min)
    return numbers











