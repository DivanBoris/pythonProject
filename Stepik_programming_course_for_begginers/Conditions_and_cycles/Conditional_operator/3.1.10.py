n1, n2, n3 = int(input()), int(input()), int(input())
if n1 < n2 + n3 and n3 < n2 + n1 and n2 < n1 + n3:
    print('YES')
else:
    print('NO')
