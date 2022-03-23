# Declare variables
example_dictionary = {
    "Key_A": "Value_A",
    "Key_B": "Value_B",
    "Key_C": "Value_C"
}

# Print of items() of dictionary
print("# items() function of dictionary")
print("items(): ", example_dictionary.items())
print()

# Combination of for loop and items()
print("# Combination of for loop and items() of dictionary")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))