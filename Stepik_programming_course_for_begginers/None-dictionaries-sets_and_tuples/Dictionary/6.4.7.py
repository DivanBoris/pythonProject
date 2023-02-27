a = int(input())
b = {}
for i in range(1, a + 1):
    b.update({i: i ** 2})
print(b)
