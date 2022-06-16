import os

files = []
for file in os.listdir():
    if file == "encrypt.py":
        continue
    files.append(file)
print(files)