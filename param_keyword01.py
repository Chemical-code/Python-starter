def print_n_times(*values, n=2):
    # Repeats n times
    for i in range(n):
        # Use values as list
        for value in values:
            print(value)
        
        print()

# Recall function
print_n_times("Hello", "Happy", "Python progamming", n=3)