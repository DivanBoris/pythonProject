a = int(input())
ch = []
nech = []
count = 0
for i in str(a):
    count += 1
    if count % 2 == 0:
        ch.append(int(i))
    elif count % 2 != 0:
        nech.append(int(i))
if (sum(ch) - sum(nech)) % 11 == 0:
    print('YES')
else:
    print('NO')
