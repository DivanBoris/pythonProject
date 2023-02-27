def info_kwargs(**kwargs):
    for key, val in sorted(list(kwargs.items())):
        print(f'{key} = {val}')


info_kwargs(first_name="John", last_name="Doe", age=33)
