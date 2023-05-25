# WAP to display multiplication tables from 1 to 5

# print(
#     "---------------------------------------------------------------------------------"
# )
# for i in range(1, 11):
#     for j in range(1, 6):
#         print(f"|  {j} x {i} = {i*j}", end="\t|")
#     print()
# print(
#     "---------------------------------------------------------------------------------"
# )

from prettytable import PrettyTable

x = PrettyTable()

for i in range(1, 6):
    col = []
    for j in range(1, 11):
        col.append(f"{i} x {j} = {i*j}")
    x.add_column(f"Table of {i}", col)
print(x)
