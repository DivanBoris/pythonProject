a, b, c = map(int, input().split())
if a < b < c:
    print(c - a)
elif b < a < c:
    print(c - b)
elif a < c < b:
    print(b - a)
elif c < a < b:
    print(b - c)
elif c < b < a:
    print(a - c)
elif b < c < a:
    print(a - b)
