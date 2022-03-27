# Use try except()
try:
    # Open file
    file = open("info.txt", "w")
    # Proceed various steps
    error.occuring()
except Exception as e:
    print(e)

# Close file
file.close()
print("# Check whether file is well closed")
print("file.closed:", file.closed)
