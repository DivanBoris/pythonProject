def format_name_list(dict):
    a = []
    for all in dict:
        for key, val in all.items():
            a.append(val)
    if len(a) <= 2:
        return " и ".join(a)
    else:
        return f'{", ".join(a[:-2])}, {" и ".join(a[-2:])}'


print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]))