def rec(a, b):
    if a > 0:
        print(b[a - 1], end=' ')
        rec(a - 1, b)


rec(a=int(input()), b=list(map(int, input().split())))

