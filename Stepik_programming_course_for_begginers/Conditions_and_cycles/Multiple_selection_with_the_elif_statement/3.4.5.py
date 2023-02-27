n1 = float(input())
n2 = float(input())
n3 = input()
if n3 == '+':
    print(n1 + n2)
elif n3 == '/' and n2 == 0:
    print('Неизвестно')
elif n3 == '/':
    print(n1 / n2)
elif n3 == '*':
    print(n1 * n2)
elif n3 == '-':
    print(n1 - n2)
else:
    print('Неизвестно')
