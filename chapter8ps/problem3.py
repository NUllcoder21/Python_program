# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+2):
#             print("*",end="")
#         print()

# pattern(6)            


# using recursion

def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)

pattern(5)    