def count_letters(a):
    N, K = 0, 0
    for i in a:
        if i.isalpha():
            if True == i.isupper():
                N += 1
            elif i != i.isupper():
                K += 1
    print(f'Количество заглавных символов: {N}')
    print(f'Количество строчных символов: {K}')


count_letters('ff')