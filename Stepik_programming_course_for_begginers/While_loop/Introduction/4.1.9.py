x = input()
i = int(str(x)[0])
while int(str(x)[0]) != 1 and int(x) < 1000000000:
    x = int(str(x)[0]) * int(x)
print(x)
