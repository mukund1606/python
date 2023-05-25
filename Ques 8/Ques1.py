# Write a function that accepts two positive integers a and b, and returns a list of all the even and odd number between a and b (including a and not including b).

def findOddEven(a: int, b: int):
    a, b = a, b if a < b else b, a
    myList = list(range(a, b))
    oddList = [i for i in myList if i % 2 != 0]
    evenList = [i for i in myList if i % 2 == 0]
    return evenList, oddList


def main():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    evenList, oddList = findOddEven(a, b)
    print("Even Elements Are:", evenList)
    print("Odd Elements Are:", oddList)


if __name__ == "__main__":
    main()
