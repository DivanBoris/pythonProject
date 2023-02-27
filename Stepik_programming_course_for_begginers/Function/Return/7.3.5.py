def find_duplicate(lst):
    b = []
    for i in lst:
        if lst.count(i) > 1:
            if i not in b:
                b.append(i)
    return b


print(find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]))
