x, y = list(map(int, input().split()))
count = 0
while x <= y:
    count += 1
    x *= 1.15
print(count + 1)
