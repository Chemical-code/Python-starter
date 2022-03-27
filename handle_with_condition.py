# Input number
user_input_a = input("Enter integer> ")

# If input is only integer
if user_input_a.isdigit():
    # Trasfer to number
    number_input_a = int(user_input_a)
    # Print
    print("Diameter of circle:", number_input_a)
    print("Circumstance of circle:", 2 * 3.14 * number_input_a)
    print("Area of circle:", 3.14 * number_input_a * number_input_a)
else:
    print("You did not enter integer.")