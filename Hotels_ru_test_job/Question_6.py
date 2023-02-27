# Решение данной задачи заняло 35 минут

def multiplication_table(step: int):
    for i in range(1, step + 1):
        for j in range(i, i * step + 1, i):
            print(j, end='\t')
        print()


multiplication_table(int(input('Введите число: ')))
