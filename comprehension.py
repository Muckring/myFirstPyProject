# List comprehension is an elegant way of
# creating lists
# SYNTAX = [1.expression 2. for value in iterable 3. (if required) condition]

# numbers: list [int] = [1,3,4,6,7,8]
# doubles: list [int] = [num * 3 for num in numbers]
# print(doubles)

vegs: list [str] = ['potato', 'carrot', 'cabbage', 'onion']

capital_letters: list [str] = [veg.capitalize() for veg in vegs if len(veg) < 7]
print(capital_letters)