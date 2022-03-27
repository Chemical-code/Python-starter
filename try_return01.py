# Declare test()
def test():
    print("First line of test() function.")
    try:
        print("try phrase is operating.")
        return
        print("after the return of try phrase.")
    except:
        print("except phrase is operating.")
    else:
        print("else phrase is operating.")
    finally:
        print("finally phrase is operating.")
    print("Last line of test() function.")

# Recall test() function
test()
