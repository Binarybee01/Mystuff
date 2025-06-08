def calc():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation: ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    choice = (input("Enter your choice (A/B/C/D):"))
               

    if choice == ("A"):
        print(f"The sum is {num1 + num2}")
    elif choice == ("B"):
        print (f"The difference is {num1 - num2}")
    elif choice == ("C"):
        print(f"The product is {num1 * num2}")
    elif  choice == ("D"):
        if num2 == 0:
            print("Error:Cannot divide by zero.")
        else:
            print(f"The quotient is {num1 / num2}")

    else :
        print("The input is invalid.") 


calc()