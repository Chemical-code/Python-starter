# Declare variables
list_number = [52, 273, 32, 72, 100]

# Exception process by try except phrase
try:
    # Input number
    number_input = int(input("Enter integer> "))
    # Print list elements
    print("{}th element: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    # Print exception object
    print("type(exception):", type(exception))
    print("exception:", exception)
    