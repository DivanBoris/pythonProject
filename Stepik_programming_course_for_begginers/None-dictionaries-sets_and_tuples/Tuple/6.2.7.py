a = int(input())
c = [i for i in range(a, a ** 2 + 1) if i % 2 != 0]
print(tuple(c))
