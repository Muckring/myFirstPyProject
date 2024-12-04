import os
from datatime import 

path: str = "C:\\Users\\igor\\Desktop\\vocabulary.docx"
path_two: str = "C:\\Users\\igor\\Desktop\\фото"
path_three: str = "C: \\Users\\Igor\\roberto"

if os.path.exists(path_three):
    print(f"{path} exists")
    if os.path.isfile(path_three):
        print("It is a file")
    elif os.path.isdir(path_three):
        print("It is a folder")
else:
    print("No such file or directory")