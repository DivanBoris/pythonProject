volume = int(input())
i = int()
b = int()
a = []
count = 0
while b <= volume:
    i = int(input())
    a.append(i)
    count += 1
    b = sum(a)
print('Довольно!')
a.pop()
print(sum(a))
print(count - 1)
