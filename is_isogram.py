def is_isogram(string):
    string = string.lower()
    lists = []
    for item in string:
        if item != " ":
            if item in lists:
                return False
            lists.append(item)
    return True
