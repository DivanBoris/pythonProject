dictionary1 = {}
dictionary2 = {}
var1 = input()
var2 = input()
for i in var1:
    if i not in dictionary1:
        dictionary1[i] = 1
    elif i in dictionary1:
        dictionary1[i] += 1
for i in var2:
    if i not in dictionary2:
        dictionary2[i] = 1
    elif i in dictionary2:
        dictionary2[i] += 1
[print("YES") if dictionary1 == dictionary2 else print("NO")]
