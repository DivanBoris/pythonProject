a = list(map(int, input().split()))
if a[0] <= a[1]:
    b = [i ** 2 for i in range(a[0], a[1] + 1)]
elif a[0] > a[1]:
    b = [i ** 3 for i in range(a[0], a[1] - 1, -1)]
print(b)
