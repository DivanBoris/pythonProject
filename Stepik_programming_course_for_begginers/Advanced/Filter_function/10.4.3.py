days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
a = list(filter(lambda x: x[0] == 'S' or len(x) == 4, days))
a.sort()
print(*a, sep='\n')
