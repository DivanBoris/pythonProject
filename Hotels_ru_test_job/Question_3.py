# Решение данной задачи заняло 15 минут

def case(general_number: int):
    last_number = general_number % 10
    print(f'{general_number} компьютер' if last_number == 1 else [f'{general_number} компьютеров', f'{general_number} компьютера'][2 <= last_number <= 4])



case(25)