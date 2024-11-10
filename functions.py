
def hello_world() -> None:
    print("Hello world!")

# hello_world()

def full_name(first_name: str, last_name: str) -> str:
    return first_name.capitalize() + " " + last_name.capitalize()

first_name: str = input('Enter your first name: ')
last_name: str = input("Enter your last name: ")

fname: str = full_name(first_name, last_name)
print(fname)

