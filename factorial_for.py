# Declare function
def factorial(n):
    # Declare variables
    output = 1
    # Add numbers by using loop
    for i in range(1, n + 1):
        output *= i
    # Return
    return output

# Recall function
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))