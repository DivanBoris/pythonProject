# объявление функции
def is_between(name, surname, middlename):
    if surname <= name <= middlename or middlename <= name <= surname:
        print("True")
    else:
        print("False")


# считываем данные
a, b, c = map(int, input().split())

# вызываем функцию
is_between(a, b, c)
