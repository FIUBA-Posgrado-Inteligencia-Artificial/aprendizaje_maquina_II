while True:
    try:
        x = int(input("Please enter a number: "))
        result = 10/x
        print("The number 10 devided by the input is:",result)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
