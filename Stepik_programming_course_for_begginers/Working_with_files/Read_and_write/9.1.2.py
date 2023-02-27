def create_file_with_numbers(n):
    name =f'range_{n}.txt'
    file = open(name, 'w+', encoding='utf-8')
    for i in range(1, n + 1):
        file.write(f'{i}\n')