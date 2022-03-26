# Declare variables
list_input_a = [1, 2, 3, 4, 5]

# Use map() function
output_a = map(lambda x: x * x, list_input_a)
print("# Result of map() function")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# Use filter() function
output_b = filter(lambda x: x < 3, list_input_a)
print("# Result of filter() function")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))