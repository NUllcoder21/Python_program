# write a program to find whether a given number is prime or not
 
n=int(input("Enter the number:"))

i=2
t=0
while(i*i<n):
    if(n%i==0):
        t+=1
    i+=1
if(t==0):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")            
        
