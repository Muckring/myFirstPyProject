import random

# You can generate random numbers with randint()
# You can set min and max values

high: int = 5
low: int = 1

# number = random.randint(low, high)
# print(number)

# You can randomly generate a random value from
# a tuble or a list of string values

# Create a tuble of family members

family = ("Kostya", "Igor", "Ariana")
# Select a family member randomly
# using choice() method of the random module

member = random.choice(family)
print(member)