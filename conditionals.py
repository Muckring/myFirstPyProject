name = str(input("Enter your name: "))

# if name == "":
#     print("You haven't entered your name")
# else:
#     print(f"Hello, {name}!")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello, {name}")