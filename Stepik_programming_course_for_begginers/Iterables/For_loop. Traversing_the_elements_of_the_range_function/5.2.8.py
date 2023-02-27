a = int(input())
b = []
for i in range(a):
    if i % 5 == 0 or i % 3 == 0:
        b.append(i)
print(sum(b))
