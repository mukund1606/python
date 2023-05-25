def getLength(elem):
    length = 0
    if (elem == 0):
        return 1
    while (abs(elem) > 0):
        length += 1
        elem //= 10
    return length


def bubbleSort(arr, ch=0):
    if (ch == 0):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    else:
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if (getLength(arr[j]) > getLength(arr[j + 1])):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    myList = [int(elem) for elem in input(
        "Enter the elements of the array: ").split()]
    ch = int(input("Enter 1 to sort via length, 2 to sort in ascending order: "))
    if (ch == 1):
        bubbleSort(myList, 1)
        print("Array sorted via length of elem: ", myList)
    elif ch == 2:
        bubbleSort(myList)
        print("Array sorted in ascending order: ", myList)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
