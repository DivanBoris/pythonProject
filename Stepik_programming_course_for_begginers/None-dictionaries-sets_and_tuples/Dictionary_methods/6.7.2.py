s = input().lower()
d = {i: s.count(i) for i in s if i.isalpha()}
print(d)