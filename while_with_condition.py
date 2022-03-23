# Declare variables
list_test = [1, 2, 1, 2]
value = 2

# Repeat if there is value in list_test
while value in list_test:
    list_test.remove(value)

# Print
print(list_test)