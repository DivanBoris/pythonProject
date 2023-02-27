a = int(input())
count = 0
while a != 1:
    if a % 2 == 0:
        count += 1
        a = a // 2
    elif a % 2 != 0:
        count += 1
        a = 3 * a + 1
print(count)
