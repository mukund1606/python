def main(ex, file):
    import re

    with open(file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if re.search(ex, line):
                print(f"String '{line.strip()}' Accepted")
            else:
                print(f"String '{line.strip()}' Not Accepted")


if __name__ == "__main__":
    ex = input("Enter Regular Expression:")
    file = input("Enter File Name:")
    main(ex, file)
