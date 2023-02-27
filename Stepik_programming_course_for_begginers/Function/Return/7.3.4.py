from functools import reduce

n = int(input())
A = [int(input()) for i in range(n)]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(reduce(gcd, A))