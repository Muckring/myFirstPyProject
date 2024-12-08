import time

file_path = "plain_text.txt"
text = "This is a plain text file"

try:
    with open(file_path, "r") as file:
        content: str = file.read()
        print(content)
except FileNotFoundError:
    print('No such file or directory')
finally:
    for x in reversed(range(6)):
        time.sleep(1)
        print(f'{x} Closing all files...')
    print('All files are closed')