# write a function function to calculate the sum of n n natural numbers

def calSum(n):
   if n==1:
      return 1
   return n+calSum(n-1)

n=int(input("Enter the sum of number:"))

print(f"The sum of n natural number is:{calSum(n)}")
