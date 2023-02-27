a = list(map(str, input().upper().split(' ')))
b = []
list(map(lambda x: b.append('A' in x), a))
print(all(b))
