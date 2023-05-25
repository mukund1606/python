# WAP to traverse every second chracter of a string using for loop

string = input("Enter a string:")

for i in range(0, len(string), 2):
    print(f'Chracter {i} of "{string}" is {string[i]}')
