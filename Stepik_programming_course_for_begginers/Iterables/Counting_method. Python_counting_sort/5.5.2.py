a = int(input())
b = list(map(int, input().split()))
c = max(b) - min(b) + 1
d = []
count = [0] * c
if min(b) >= 0:
    for i in b:
        count[i - abs(min(b))] += 1
    for i in range(c):
        if count[i] > 0:
            d.append(i + abs(min(b)))
            if count[i] > 1:
                d.append(i + abs(min(b)))
    for i in d:
        print(i, end=" ")
elif min(b) < 0:
    for i in b:
        count[i + abs(min(b))] += 1
    for i in range(c):
        if count[i] > 0:
            d.append(i - abs(min(b)))
            if count[i] > 1:
                d.append(i - abs(min(b)))
    for i in d:
        print(i, end=" ")
