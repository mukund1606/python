# Consider an example of a tuple has T = (11, 12, 13, 14, 15). Write a program to store numbers present at odd index into a new tuple

def main():
    T = (11, 12, 13, 14, 15)
    NewTuple = T[1::2]
    print(NewTuple)


if __name__ == "__main__":
    main()
