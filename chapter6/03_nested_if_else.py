number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")
