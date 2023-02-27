def factorial(n):
    pr = 1
    if n >= 1:
        for i in range(1, n + 1):
            pr *= i
    return pr


print(factorial(4))
