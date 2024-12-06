import csv
import time

family: list[str | int] = [["name", "age"], 
                           ["Kostya", 42], 
                           ["Elena", 38], 
                           ['Ariana', 6]] 
file_path = "output.csv"
try:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in family:
            writer.writerow(row)
    print(f"A new csv {file_path} has been created")
except FileExistsError:
    print('This file already exists')
finally:
    for i in reversed(range(6)):
        time.sleep(1)
        print(f"{i} Closing all files")
    print('all files are closed')

