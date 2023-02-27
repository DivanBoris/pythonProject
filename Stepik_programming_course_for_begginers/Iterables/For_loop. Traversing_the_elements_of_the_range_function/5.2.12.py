n = int(input())
s = []
for i in range(n):
    i = input()
    s.append(i)
    if len(i) > 10:
        s.pop()
        f = i[0] + str((len(i) - 2)) + i[-1]
        s.append(f)
for i in s:
    print(i)
