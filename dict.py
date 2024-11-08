capitals: dict = {"Russia" : "Moscow", 
                  "Germany": "Berlin",
                  "Belarus": "Minsk",
                  "Ukraine": "Kyiv"}


keys : object = capitals.keys()
print(keys)
for key in keys:
    print(key, end=" ")

print(" ")

values : object = capitals.values()
print(values)
for value in values:
    print(value, end=" ")

print(" ")

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")
    