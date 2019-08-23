import os

filename = "http_1.py"

file1 = os.open(filename, os.O_RDONLY)


print(os.read(file1, 0))