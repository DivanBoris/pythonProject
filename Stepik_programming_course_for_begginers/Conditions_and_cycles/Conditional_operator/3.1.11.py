n = input().rjust(6, '0')
print('YES' if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]) else 'NO')
