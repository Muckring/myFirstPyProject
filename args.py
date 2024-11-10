# *args is a tuple so you can loop over it.
# you can send a varying amount of arguments

def add(*args) -> int:
    total: int = 0
    for arg in args:
        total+=arg
    return total

# result: int = add(3,4,6,7,8)
# print(result)

# **kwargs (or keyword arguments) is a dictionary
# you can also send a varying amount of key-value pairs as 
# argument in the following format key = "value"

def display_info(**kwargs) -> None:
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

result = display_info(fname="Robert", lname="De Paris", job="Crusader")
print(result)