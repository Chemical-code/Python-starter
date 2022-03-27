# Use try except()
try:
    # Open file
    file = open("info.txt", "w")
    # Proceed various steps
    error.occuring()
    # Close file
    file.close()
except Exception as e:
    print(e)

print("# Check whether file is well closed")
print("file.closed:", file.closed)
