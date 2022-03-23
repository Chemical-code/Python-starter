# Declare variables
i = 0

# Repeat infinitely
while True:
    # Print the times
    print("It is {} times repeat.".format(i))
    i = i + 1
    # End loop
    input_text = input("Do you want to quit?(y/n): ")
    if input_text in ["y", "Y"]:
        print("Quit the loop.")
        break
