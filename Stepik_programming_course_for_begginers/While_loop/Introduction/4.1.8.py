x = int(input())
n = 0
while 2 ** n < x:
    n += 1
if 2 ** n == x:
    print(n)
else:
    print('НЕТ')
