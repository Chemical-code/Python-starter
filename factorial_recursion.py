# Declare function
def factorial(n):
    # if n is 0, then return 1
    if n == 0:
        return 1
    # if n is not 0, then return n * (n-1)!
    else:
        return n * factorial(n - 1)

# Recall function
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))