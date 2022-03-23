# Declare variable
example_list = ["Element_A", "Element_B", "Element_C"]

# Print
print("# Simple print")
print(example_list)
print()

# Print by applying enumerate() function
print("# Application of enumerate() function")
print(enumerate(example_list))
print()

# Print by forcing change with list() function
print("# Forced change with list() function")
print(list(enumerate(example_list)))
print()

# Combination of for loop and enumerate() function
print("# Combination of for loop")
for i, value in enumerate(example_list):
    print("{}th elelment is {}".format(i, value))
