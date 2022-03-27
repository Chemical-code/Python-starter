# Declare variables
list_input_a = ["52", "273", "32", "spy", "103"]

# Apply loop
list_number = []
for item in list_input_a:
    # Add to list by chaning number
    try:
        float(item)
        list_number.append(item)
    except:
        pass

# Print
print("The number in side {}".format(list_input_a))
print("is {}.".format(list_number))