def ZeroDivision(a, b):
    try:
        c = a / b
        print("a/b is:", c)
    except ZeroDivisionError as e:
        print("Error Occurred:", e)


def ValueException():
    try:
        a = int(input("Enter 1st Number:"))
        b = int(input("Enter 2nd Number:"))
        print("a+b is:", a + b)
    except ValueError as e:
        print("Value Error Occurred:", e)


def AttributeException():
    try:
        a = int(input("Enter 1st Number:"))
        b = int(input("Enter 2nd Number:"))
        a.push(b)
    except AttributeError as e:
        print("Type Error Occurred:", e)


def TypeException():
    try:
        a = 5
        b = "Hello"
        c = a + b
    except TypeError as e:
        print("Type Error Occurred:", e)


def NameException():
    try:
        a = int(input("Enter 1st Number:"))
        b = int(input("Enter 2nd Number:"))
        print("Sum is:", a + c)
    except NameError as e:
        print("Name Error Occurred:", e)


def ModuleNotFoundException():
    try:
        import myUnknownModule
    except ModuleNotFoundError as e:
        print("Module Not Found Error Occurred:", e)


def main():
    ZeroDivision(123, 0)
    ValueException()
    # AttributeException()
    TypeException()
    # NameException()
    ModuleNotFoundException()
    pass


if __name__ == "__main__":
    main()


"""
Error Occurred: division by zero
Enter 1st Number:5
Enter 2nd Number:a
Value Error Occurred: invalid literal for int() with base 10: 'a'
Type Error Occurred: unsupported operand type(s) for +: 'int' and 'str'
Module Not Found Error Occurred: No module named 'myUnknownModule
"""
