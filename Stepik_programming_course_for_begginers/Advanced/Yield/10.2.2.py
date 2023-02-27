def gen_fibonacci_numbers(x):
    a, b = 1, 1
    for i in range(1, x + 1):
        yield a
        a, b = b, a + b


for i in gen_fibonacci_numbers(5):
    print(i)
