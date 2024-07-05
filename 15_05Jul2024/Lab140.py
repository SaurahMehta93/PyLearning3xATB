import os

fd = os.open("test_file.txt",os.O_RDWR)
os.write(fd, b"Hello, world!")
os.close(fd)