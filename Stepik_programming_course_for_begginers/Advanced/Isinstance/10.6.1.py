def count_strings(*args):
    return len(list((i for i in args if isinstance(i, str))))


print(count_strings(1, 2, 'hello', [2, 3, 4], True))
