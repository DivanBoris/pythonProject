a = input()
b = []
c = list(input().split(' '))
for i in c:
    i.lower()
    if i.find(a) >= 0:
        b.append(i)
for i in b:
    print(i)
