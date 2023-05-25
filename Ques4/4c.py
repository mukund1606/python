# WAP to find even numbers from 0 to 10 and find the sum

s = 0
for i in range(0, 11):
    if i % 2 == 0 and i > 0:
        s += i
        print(f"{i} is Even")
print(f"Sum of Even Numbers between 0 and 10 (including 10) is {s}")
