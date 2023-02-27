def multiply(*args):
    pr = 1
    for i in args:
        pr *= i
    return pr


print(multiply(1, 2, 3))