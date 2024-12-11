import csv

file_path: str = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print('File not found')

finally:
    print("All files closed")