# File Handling

# How to read text and write into it using python code

# Function
# open("filename", "mode")
# mode
# r - read
# w - write
# a - append
# 'b' - binary (zoom.exe)
# '+' - for updating (reading and writing)

# read and write documents
# read file
# reading entire content: content = file_object.read()
# line = file_object.readline() for single file
# lines = file_object.readlines() for all lines in list.
# close the file

file = open("test_file.txt", 'r')
content = file.read()
print(content)
file.close()