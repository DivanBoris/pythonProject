def create_actor(**kwargs):
    res = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }
    for key, val in kwargs.items():
        res[key] = val
    return res


print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
