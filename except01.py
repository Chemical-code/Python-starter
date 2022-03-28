# Exception process by try except phrase
try:
    # Transfer to number
    number_input_a = int(input("Enter integer> "))
    # Print
    print("Diameter of circle:", number_input_a)
    print("Circumstance of circle:", 2 * 3.14 * number_input_a)
    print("Area of circle:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    # Print exception object
    print("type(exception):", type(exception))
    print("exception:", exception)
    