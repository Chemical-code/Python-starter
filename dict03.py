# Declare dictionary
dictionary = {
    "name" : "7D dried mango",
    "type" : "Pickled"
}

# Print before deletion
print("Before delete elements:", dictionary)

# Delete elements
del dictionary["name"]
del dictionary["type"]

# Print after deletion
print("After delete elements:", dictionary)
