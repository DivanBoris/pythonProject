d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}
capitals = {}
for i in d1:
    capitals.update({i: d1[i]})
for i in d2:
    capitals.update({i: d2[i]})
print(capitals)
