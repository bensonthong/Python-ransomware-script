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

with open("key.key", "rb") as k:
    secretkey = k.read()

password = "notpassword"
user_phrase = input("Enter password to decrypt: \n")
if user_phrase == password:
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)  # encrypting the contents generated for each file
        with open(file, "wb") as f:
            f.write(contents_decrypted)                     # write it back as an encrypted file
    print("Files are decrypted!")
else:
    print("Wrong password!")
