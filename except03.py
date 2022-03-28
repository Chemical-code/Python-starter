# Declare variables
list_number = [52, 273, 32, 72, 100]

# Exception process by try except phrase
try:
    # Input number
    number_input = int(input("Enter integer> "))
    # Print list elements
    print("{}th element: {}".format(number_input, list_number[number_input]))
    make.error()
except ValueError as exception:
    # If ValueError occurs
    print("Enter the integer!")
    print("exception:", exception)
except IndexError as exception:
    # If InedxError occurs
    print("Out of index of list!")
    print("exception:", exception)