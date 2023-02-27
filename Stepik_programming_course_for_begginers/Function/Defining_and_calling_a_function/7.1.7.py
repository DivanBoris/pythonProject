def check_password(p):
    numbers = [i for i in p if i.isdigit()]
    char = [i for i in p if i.isupper()]
    symb = [i for i in p if i in "!@#$%*"]

    print("Pefrect password" if len(numbers) >= 3 and len(char) >= 1 and len(symb) >= 1 and len(
        p) >= 10 else "Easy peasy")


check_password('4')
