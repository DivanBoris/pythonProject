from itertools import zip_longest

n = int(input())
s1 = []
s2 = []
count1 = 0
count2 = 0
for i in range(n):
    i = input().lower()
    count1 += 1
    a = i.find('рок')
    if a + 1 > 0:
        s2.append(a + 1)
        s1.append(count1)
for s1, s2 in zip_longest(s1, s2, fillvalue=' '):
    print(s1, s2)
