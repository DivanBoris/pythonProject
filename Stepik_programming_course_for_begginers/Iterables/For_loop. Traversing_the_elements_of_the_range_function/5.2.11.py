n = int(input())
s = []
for i in range(n):
    i = input()
    if i.find('соль') == -1:
        s.append(i)
print(', '.join(s))
