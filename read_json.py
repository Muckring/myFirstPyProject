import json
import time


file_path = "output.json"
daughter = {
    "name": "Ariana",
    "age": 6
}

try:
    with open(file_path, 'r') as file:
        content: str = json.load(file)
        print(content)

except FileNotFoundError:
    print("No such file or directory")

# finally:
#     for x in range(6):
#         time.sleep(1)
#         print("Closing files")
#     print("All files are closed")