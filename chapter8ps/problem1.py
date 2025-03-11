# write a program using function to find greatest of three numbers

def find_greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

print(f"The greatest number is :{find_greatest(a,b,c)}")