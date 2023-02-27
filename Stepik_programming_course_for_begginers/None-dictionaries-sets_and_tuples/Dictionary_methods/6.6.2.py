a = int(input())
b = {}
for i in range(a):
    c = input()
    if c in b:
        print(f'{c}{b[c]}')
        b[c] += 1
    else:
        print("OK")
        b[c] = 1
