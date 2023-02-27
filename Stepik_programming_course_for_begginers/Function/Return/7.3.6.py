def first_unique_char(s):
    r = []
    for i in s:
        if s.count(i) == 1:
            r.append(s.index(i))
    if len(r) == 0:
        return -1
    return r[0]


print(first_unique_char('abracadabra'))