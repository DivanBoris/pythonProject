a = input().lower()
b = []
c = int
for i in a:
    c = a.count(i)
    b.append(c)
print(max(b))
