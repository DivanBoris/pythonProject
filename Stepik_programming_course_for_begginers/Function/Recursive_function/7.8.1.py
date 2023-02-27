def print_from(n: int) -> None:
    if 0 < n:
        print(n)
        print_from(n - 1)


print_from(8)