def sum_num(x):
    s = 0
    for i in str(x):
        if 48 < ord(i) < 57:
            s += int(i)
    print(s)


sum_num(7)
