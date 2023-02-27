# Решение данной задачи заняло 15 минут

def numbers(f: float):
    return int(f + (5 - (f % 5))) if 5 - (f % 5) < f % 5 else int((f + 5 - (5 + (f % 5))))


print(numbers(27.8))
