# Calculate the factorial of a number using recursion


def fact(num: int) -> int:
    if num == 0:
        return 1
    elif num < 0:
        raise Exception
    else:
        return num * fact(num - 1)


num = int(input("Enter Number to find Factorial:"))
print(f"Factorial of {num} is {fact(num)}")
