a = list(map(int, input()))
count = [0] * (max(a) + 1)
for i in a:
    count[i] += 1
for i in range(len(count)):
    if count[i] > 0:
        print(i, count[i])
