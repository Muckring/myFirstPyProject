

text = "Python is a great programming language"
family: str = ["Kostya", "Elena", "Ariana"]
file_path = 'text.txt'

with open(file_path, 'a') as file:
    for member in family:
        file.write(member + "\n")
    print(f'text file {file_path} has been appended')