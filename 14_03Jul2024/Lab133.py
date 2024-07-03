try:
    with open('test_file.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError as file_not_found:
    print('File not found')
finally:
    file.close()

print("-----------------------")

try:
    with open('test_file.txt', 'r') as file:
        data = file.readline()
        print(data)
except FileNotFoundError as file_not_found:
    print('File not found')
finally:
    file.close()


print("-----------------------")

try:
    with open('test_file.txt', 'r') as file:
        data = file.readlines()
        print(data)
except FileNotFoundError as file_not_found:
    print('File not found')
finally:
    file.close()


print("-----------------------")

with open('test_file.txt', 'r') as file:
    line = file.readlines()

for i in line:
    print(i, end="")

