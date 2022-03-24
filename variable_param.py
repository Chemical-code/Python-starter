def print_n_times(n, *values):
    # Repeat n times
    for i in range(n):
        # Use values as list
        for value in values:
            print(value)

        print()

# Recall function
print_n_times(3, "Hello", "Happy", "Python progamming")