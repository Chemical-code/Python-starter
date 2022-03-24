# Declare function
from doctest import OutputChecker


def sum_all(start=0, end=0, step=1):
    # Declare variables
    output = 0
    # Add numbers using loop
    for i in range(start, end + 1, step):
        output += i
    # Return
    return output

# Declare function
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))