# Declare function
def write_text_file(filename, text):
    # Use try except phrase
    try:
        # Open file
        file = open(filename, "w")
        # Operate various step
        return
        # Write a text in file
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # Close file
        file.close()

# Recall function
write_text_file("test.txt", "Hello!")