# Решение данной задачи заняло 15 минут

def prime(number: int):
    return f'Число {number} является простым числом'if number == 1 or number == 2 or number == 3 else [f'Число {number} является простым числом', f'Число {number} не является простым числом'][number % 2 == 0 or number % 3 == 0]


print(prime(int(input("Введите число: "))))