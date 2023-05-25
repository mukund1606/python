# Implement binary search, quick sort and merge sort in python

def binarySearch(arr, l, r, elem):
    if (l <= r):
        mid = (l + r) // 2
        if (arr[mid] == elem):
            return mid
        elif (arr[mid] > elem):
            return binarySearch(arr, l, mid - 1, elem)
        else:
            return binarySearch(arr, mid + 1, r, elem)
    return -1


def quickSort(arr, l, r):
    if (l < r):
        pivot = partition(arr, l, r)
        quickSort(arr, l, pivot - 1)
        quickSort(arr, pivot + 1, r)


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if (arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def mergeSort(arr, l, r):
    if (l < r):
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    b = []
    i = l
    k = mid + 1
    while (i <= mid and k <= r):
        if (arr[i] < arr[k]):
            b.append(arr[i])
            i += 1
        else:
            b.append(arr[k])
            k += 1
    while (i <= mid):
        b.append(arr[i])
        i += 1
    while (k <= r):
        b.append(arr[k])
        k += 1
    for i in range(len(b)):
        arr[l+i] = b[i]


def main():
    arr = [int(i) for i in input("Enter the elements of the array: ").split()]
    print("The array is: ", arr)
    print("Enter 1 for binary search, 2 for quick sort, 3 for merge sort")
    inputChoice = int(input("Enter your choice: "))
    if inputChoice == 1:
        elem = int(input("Enter the element to be searched: "))
        elemIndex = binarySearch(arr, 0, len(arr) - 1, elem)
        if (elemIndex == -1):
            print("Element not found")
        else:
            print("Element found at index: ", elemIndex)
    elif inputChoice == 2:
        quickSort(arr, 0, len(arr) - 1)
        print("Sorted array via quick sort: ", arr)
    elif inputChoice == 3:
        mergeSort(arr, 0, len(arr) - 1)
        print("Sorted array via merge sort: ", arr)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
