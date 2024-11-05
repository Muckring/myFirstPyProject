# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name:")
#     name = input("Enter your name: ")
# print(f"Hello {name:_^30}!")

sports = input("Enter your favourite sport. Please press q to exit: ")

list_sports = []

while not sports == 'q':
    list_sports.append(sports)
    sports = input("Enter your favourite sport. Please press q to exit: ")
print(f"Below are your favourite sports: {list_sports}")
