capitals: dict = {"Russia" : "Moscow", 
                  "Germany": "Berlin",
                  "Belarus": "Minsk",
                  "Ukraine": "Kyiv"}


# keys : object = capitals.keys()
# print(keys)
# for key in keys:
#     print(key, end=" ")

# print(" ")

# values : object = capitals.values()
# print(values)
# for value in values:
#     print(value, end=" ")

# print(" ")

# items = capitals.items()
# print(items)
# for key, value in capitals.items():
#     print(f"{key}: {value}")



# You can use update() to add a new key-value pair to the 
# end of the dictionary

capitals.update({"France" : "Paris"})
print(capitals)

# Or, you can modify the existing key-value pair

capitals.update({"Russia" : "Mukhosransk"})
print(capitals)

#You can also change an item as follows:
capitals["France"] = "Marseiile"
print(capitals)

# You can use pop() to remove an item and specify the key
# capitals.pop("Russia")
# print(capitals)

# popitem() removes the last item in the dict
# capitals.popitem()
# print(capitals)

# You can use either copy() or dict() constructor
# to copy a dict

# new_dict = capitals.copy()
# print(new_dict)

# dict2 = dict(capitals)
# print(dict2)

child1 = {
    "name" : "Kostya",
    "year" : 1983
}

child2 = {
    "name" : "Igor",
    "year" : 1992
}

siblings = {
    "brother1" : child1,
    "brother2" : child2
}

print(siblings)


for x, obj in siblings.items():
    print(x)
    for y in obj:
        print(y, ":", obj[y])
    print()