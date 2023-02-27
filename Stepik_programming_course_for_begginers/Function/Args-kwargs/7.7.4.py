def only_one_positive(*args):
    a = []
    for i in args:
        if i > 0:
            a.append(i)
    return True if len(a) == 1 else False

print(only_one_positive(1, 2))