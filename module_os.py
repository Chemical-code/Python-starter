# Import module
import os

# Print elemental info
print("Current OS:", os.name)
print("Current folder:", os.getcwd())
print("Elements of current folder:", os.listdir())

# Make folder and eliminate
os.mkdir("hello")
os.rmdir("hello")

# Form file and change name
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# Eliminate file
os.remove("new.txt")
# os.unlink("new.txt")

# Run system commend
os.system("dirs")
