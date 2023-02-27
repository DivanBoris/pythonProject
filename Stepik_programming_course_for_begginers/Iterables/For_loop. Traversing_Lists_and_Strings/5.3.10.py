a = input()
b = []
for i in a:
    i = int(ord(i))
    if 48 <= i <= 57:
        c = chr(i)
        b.append(int(c))
print(len(b), sum(b))
