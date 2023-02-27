a, b = int(input()), int(input())
minimum = a if a < b else b
maximum = b if b > a else a
print(f'{minimum} {maximum}')
