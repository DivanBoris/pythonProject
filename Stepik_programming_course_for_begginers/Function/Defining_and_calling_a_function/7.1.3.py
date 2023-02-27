def summa_n(x):
    S = 0
    for i in range(1, x + 1):
        S += i
    print(f'Я знаю, что сумма чисел от 1 до {x} равна {S}')


summa_n(5)
