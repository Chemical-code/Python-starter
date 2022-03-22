# Declare dictionary
dictionary = {
    "name" : "7D dried mango",
    "type" : "Pickled",
    "ingredient" : ["Mango", "Sugar", "Sodium metabisulfate", "Gardenia yellow pigment"],
    "origin" : "Philippines"
}

# Print
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# Exchange value
dictionary["name"] = "8D dried mango"
print("name:", dictionary["name"])