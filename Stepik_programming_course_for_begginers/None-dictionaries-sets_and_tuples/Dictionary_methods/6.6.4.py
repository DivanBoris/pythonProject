countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
for i in countries:
    if city in countries[i]:
        print(f'INFO: {city} is a city in {i}')
        break
else:
    print(f"ERROR: Country for {city} not found")
