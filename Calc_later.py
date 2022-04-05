while True:
    try:
        x = input("Enter a number: ")
        y = input("Enter another number: ")
        print("The sum of the two numbers is: ", int(x) + int(y))
        break
    except ValueError:
        print("Please enter a number")
