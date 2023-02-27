n = int(input())
hour = (n // 3600) % 24
n = n % 3600
minute = n // 60
n = n % 60
sec = n
print(hour, ':', minute // 10, minute % 10, ':', sec // 10, sec % 10, sep='')
