# Declare dictionary
dictionary = {
    "name" : "7D dried mango",
    "type" : "Pickled",
    "ingredient" : ["Mango", "Sugar", "Sodium metabisulfate", "Gardenia yellow pigment"],
    "origin" : "Philippines"
}

# Imput from user
key = input("> key wanted to access: ")

# Print
if key in dictionary:
    print(dictionary[key])
else:
    print("Access denied.")