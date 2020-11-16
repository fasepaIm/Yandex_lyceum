def dell(first, second):
    lol = set(first) & set(second)
    first = list(filter(lambda x: x not in lol, first))
    second = list(filter(lambda x: x not in lol, second))
    return first, second


print(*dell([1, 5, 5, 9], [2, 5, 8, 7]))