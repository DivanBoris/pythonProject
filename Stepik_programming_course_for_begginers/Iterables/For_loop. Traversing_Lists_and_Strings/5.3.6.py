a = list(map(str, input().split()))
b = int(input())
n = len(a)
for i in range(n):
    if int(a[i]) == b:
        print(i + 1)
        break
else:
    print('ErrorValue')
