def print_goods(*args: str):
    count = 0
    for i in args:
        if isinstance(i, str) == True and len(i) > 0:
            count += 1
            print(f'{count}. {i}')
    if count == 0:
        print('Нет товаров')


print_goods(1, True, 'Грушечка', '', 'Pineapple')