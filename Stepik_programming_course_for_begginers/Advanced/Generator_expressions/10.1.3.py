week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ]

w = (week[i] for i in range(1, 8))
days = ((i + 1, week[(i % len(week))]) for i in range(77))
for i in days:
    print(i)
