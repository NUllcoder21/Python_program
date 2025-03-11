# write the program to print multiplication table of n using for loop in reversed order

n=int(input("Enter the number that you want tpo print the table:"))
# for i in range (1,11):
#     print(f"{n} * {11-i} = {n*(11-i)}")

for i in range(10,0,-1):
    print(f"{n} * {i} = {n*i}")