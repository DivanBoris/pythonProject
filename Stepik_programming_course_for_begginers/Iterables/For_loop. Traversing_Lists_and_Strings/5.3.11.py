a = input()
all = []
fst = []
snd = []
for i in a:
    i = ord(i)
    all.append(int(i))
for i in all:
    if i == 40:
        fst.append(i)
    elif i == 41:
        snd.append(i)
if len(fst) == len(snd):
    print("YES")
elif all[0] == 40:
    print('NO')
else:
    print("NO")
