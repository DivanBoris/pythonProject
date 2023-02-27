from datetime import datetime

hour1 = int(input())
minute1 = int(input())
second1 = int(input())

hour2 = int(input())
minute2 = int(input())
second2 = int(input())

date1 = datetime(1, 1, 1, hour1, minute1, second1)
date2 = datetime(1, 1, 1, hour2, minute2, second2)
print((date2 - date1).seconds)