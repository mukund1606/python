# WAP to prompt a user to enter 2 different numbers and Perform basic arithmetic operations on them based on user's choice.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
ch = input(
    "Enter Your Choice\n(1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponential\n7. Floor Division):"
)
if ch == "1":
    print(f"Sum of {a} and {b} is {a + b}")
elif ch == "2":
    print(f"Difference of {a} and {b} is {a - b}")
elif ch == "3":
    print(f"Product of {a} and {b} is {a * b}")
elif ch == "4":
    if b != 0:
        print(f"Division of {a} and {b} is {a / b}")
    else:
        print("Division by Zero Not Possible")
elif ch == "5":
    if b != 0:
        print(f"Remainder of {a} by {b} is {a % b}")
    else:
        print("Division by Zero Not Possible")
elif ch == "6":
    print(f"Exponential {a}^{b} is {a ** b}")
elif ch == "7":
    if b != 0:
        print(f"Quotient of {a}/{b} is {a // b}")
    else:
        print("Division by Zero Not Possible")
else:
    print("Invalid Choice")
