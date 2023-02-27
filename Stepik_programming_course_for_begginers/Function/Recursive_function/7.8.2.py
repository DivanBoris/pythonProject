def print_to(n: int) -> None:
    if n + 1 > 1:
        print_to(n - 1)
        print(n)


print_to(8)
