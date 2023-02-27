data = {
    "my_friends": {
        "count": ...,
        "people": [
            {
                "first_name": 'Serge',
                "id": 1,
                "last_name": 'Werda',
            },
            {
                "first_name": 'Ivan',
                "id": 2,
                "last_name": 'Corva',
            },
        ]
    }
}

res = []
for name in data['my_friends']['people']:
    res.append(name['first_name'])
[print(i) for i in sorted(res)]
