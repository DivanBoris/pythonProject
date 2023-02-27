import random

a = [3, 4, 5, 6, 7, 8, 9, 10, 11]
s = 3
count = 0
while a[3] * a[4] * a[5] != a[1] * a[4] * a[7]:
    random.shuffle(a)
    count += 1
while a[0] * a[1] * a[2] != a[0] * a[3] * a[6]:
    b = [a[0], a[2], a[6], a[8]]
    random.shuffle(b)
    count += 1
    a = [b[0], a[1], b[1], a[3], a[4], a[5], b[2], a[7], b[3]]
    for i in a:
        print(i, end=' ')
    print()
mat = [a[i:i + s] for i in range(0, len(a), s)]
print(*mat, sep='\n')
print(count)

