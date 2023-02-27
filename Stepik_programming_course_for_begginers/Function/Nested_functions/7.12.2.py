def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition():
        a = x + y
        print(a)

    def subtraction():
        s = x - y
        print(s)

    def division():
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            d = x / y
            print(d)

    def multiplication():
        m = x * y
        print(m)

    if operation == 'a':
        addition()
    if operation == 's':
        subtraction()
    if operation == 'd':
        division()
    if operation == 'm':
        multiplication()
    if operation != 'm' and operation != 'd' and operation != 's' and operation != 'a':
        print('Ошибка. Данной операции не существует')


calculate(45, 60, 'a')
