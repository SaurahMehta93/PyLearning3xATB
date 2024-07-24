# File Read only

import os.path
try:
    file = open("read_file.txt", 'r')
    print(file.read())
except FileNotFoundError as e:
    print("File not found")
finally:
    try:
        file.close()
    except NameError as e1:
        print("invalid file name")
