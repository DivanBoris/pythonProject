n1 = input()
n2 = input()
print('YES' if ((ord(n1[0]) + ord(n1[1])) % 2 == 0 and (ord(n2[0]) + ord(n2[1])) % 2 == 0) or
               ((ord(n1[0]) + ord(n1[1])) % 2 != 0 and (ord(n2[0]) + ord(n2[1])) % 2 != 0)
      else 'NO')
