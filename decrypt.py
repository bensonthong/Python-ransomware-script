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
    # This checks to see if the file in the directory is a file.
    if os.path.isfile(file):
        files.append(file)
print(files)

# ========================================================= #
# Open the key.key file to read they encryption             #
# ========================================================= #
with open("key.key", "rb") as k:
    secretkey = k.read()

# ========================================================= #
# Creating password and ask user for password to decrypt    #
# ========================================================= #
password = "notpassword"
user_phrase = input("Enter password to decrypt: \n")

# ========================================================= #
# Check if password is successful, then decrypts all files  #
# ========================================================= #
if user_phrase == password:
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)  # decrypting the contents generated for each file
        with open(file, "wb") as f:
            f.write(contents_decrypted)                           # write it back as a decrypted
    print("Files are decrypted!")
else:
    print("Wrong password!")
