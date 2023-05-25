# WAP to display the reverse of the number entered
num = int(input("Enter a number:"))
rev_num = 0

if num > 0:
    while num > 0:
        rev_num *= 10
        r = num % 10
        rev_num += r
        num = num // 10
else:
    num = num * -1
    while num > 0:
        rev_num *= 10
        r = num % 10
        rev_num += r
        num = num // 10
    rev_num = rev_num * -1

print(rev_num)
