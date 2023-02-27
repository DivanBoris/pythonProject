def double_it(func):
    def inner(*args):
        a = func(*args)
        return a * 2

    return inner


@double_it
def multiply(num1, num2):
    return num1 * num2


res = multiply(9, 4)
print(res)
