def get_body_mass_index(m, h):
    if m / ((h / 100) ** 2) < 18.5:
        print("Недостаточная масса тела")
    elif 18.5 <= m / ((h / 100) ** 2) <= 25:
        print("Норма")
    elif m / ((h / 100) ** 2) > 25:
        print('Избыточная масса тела')


get_body_mass_index(2, 40)
