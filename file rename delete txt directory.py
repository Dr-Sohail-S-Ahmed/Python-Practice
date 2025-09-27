# Remove '#' to run each command separately but its effect can be seen in the folder (not here)

import os

print(os.getcwd())      # Prints path of the current working directory (CWD)

os.mkdir("Temp")
os.renames("Temp", "Perm")

print(os.listdir())     # Prints filenames within the CWD

os.rmdir("Perm")
print(os.listdir())

# os.renames("A.txt", "X.txt")

# os.remove("X.txt")