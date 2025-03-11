'''
factorial(1)=1
factorial(2)=2 X 1
factorial(1)=3X2X1
factorial(1)=4X3X2X1
factorial(1)=5X4X3X2X1

factorial(n)=n*factorial(n-1)
'''

def factorial(n):
    if (n==1 or n==0):
        return 1
    return  n*factorial(n-1)

n=int(input("Enter the number that you want to print the factorial:"))

fact=factorial(n)

print(fact)