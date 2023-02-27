def gen_squares(x):
    for i in range(1, x + 1):
               yield i ** 2

for i in gen_squares(5):
    print(i)