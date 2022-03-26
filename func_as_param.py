# Recalling ten times using parameter
def call_10_times(func):
    for i in range(10):
        func()
    
# Simple print function
def print_hello():
    print("Hello")

# Combination
call_10_times(print_hello)