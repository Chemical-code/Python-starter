print("Program is now operating.")

while True:
    try:
        print("try phrase is operating.")
        break
        print("try phrase after the break.")
    except:
        print("except phrase is operating.")
    finally:
        print("finally phrase is operating.")
    print("Last line of while loop")
print("Program is now terminated.")