import json
import time


father = {
    "name": "Kostya",
    "age": 42,
    "job": "Delivery Guy"
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(father, file)
        print(f"JSON file {file_path} has been created")
except FileExistsError:
    print("This file already exists")
finally:
    for i in reversed(range(6)):
        time.sleep(1)
        print(i)
    print("Closing all files")