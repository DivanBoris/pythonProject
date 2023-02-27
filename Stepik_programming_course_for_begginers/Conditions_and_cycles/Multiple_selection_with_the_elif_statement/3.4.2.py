a, b, c = int(input()), int(input()), int(input())
if a == b != c or a != b == c or a == c != b:
    print(2)
elif a == b == c:
    print(3)
else:
    print(0)
