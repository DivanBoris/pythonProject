a = input()
count = 0
while len(a) != count:
    if a[count] == 'a' or a[count] == 'e':
        print('Ага! Нашлась')
        count = count + (len(a) - count)
        break
    print(f'Текущая буква: {a[count]}')
    count += 1
else:
    print('Распечатали все буквы')
