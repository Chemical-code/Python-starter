# Declare variables
counter = 0

# Declare function
def fibonacci(n):
    global counter
    counter += 1
    # Calculate fibonacci number
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Recall function
print(fibonacci(10))