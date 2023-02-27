def find_keys(**kwargs):
    a = list(k for k, v in kwargs.items() if isinstance(v, (list, tuple)))
    return sorted(a, key=str.lower)


print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
