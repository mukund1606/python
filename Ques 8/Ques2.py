# Write a program that prompt user to enter the elements of a list and add the element to a list. Write a function maximum with one list argument and minimum with one list argument to find the maximum and minimum number from the list.

def prompt():
    myList = []
    while True:
        elem = input("Enter a number(Enter stop to stop adding numbers):")
        if elem.lower() == "stop":
            break
        elem = int(elem)
        myList.append(elem)
    return myList


def minimum(myList):
    if len(myList) == 0:
        print("Empty List")
        return
    temp = myList[0]
    for i in myList:
        if i < temp:
            temp = i
    return temp


def maximum(myList):
    if len(myList) == 0:
        print("Empty List")
        return
    temp = myList[0]
    for i in myList:
        if i > temp:
            temp = i
    return temp


def main():
    myList = prompt()
    print("List is", myList)
    print("Maximum of list is", maximum(myList))
    print("Minimum of list is", minimum(myList))


if __name__ == "__main__":
    main()
