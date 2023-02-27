a = list(map(int, input().split()))
fr = [3, 5, 7, 9]
[a.remove(i) for i in fr if i in a]
print(a)
