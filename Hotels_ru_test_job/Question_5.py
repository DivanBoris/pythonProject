# Решение данной задачи заняло 25 минут

def coincidence(*args: list):
    first = {x for x in args[0] if args[0].count(x) > 1}
    second = {x for x in args[0] if args[1].count(x) > 1}
    print(set(first) & set(second))


coincidence([7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1])
