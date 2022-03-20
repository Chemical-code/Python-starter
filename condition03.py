# Input
number = input("Input integer> ")

# Extract last character of integer
last_character = number[-1]

# Change into number
last_number = int(last_character)

# Check even number
if last_number % 2 == 0:
    print("Even number")

# Check odd number
if last_number % 2 == 1:
    print("Odd number")
