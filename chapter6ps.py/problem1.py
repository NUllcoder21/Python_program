a1=int(input("Enter th number 1:"))
a2=int(input("Enter th number 2:"))
a3=int(input("Enter th number 3:"))
a4=int(input("Enter th number 4:"))

if a1>a2 and a1>a3 and a1>a4 :
    print( a1  , " is graeter number among tese four ")

elif(a2>a3 and a2>a4 and a2>a1):
     print( a2 , " is graeter number among tese four ")
elif(a3>a4 and a3>a2 and a3>a1):
      print( a3 , " is graeter number among tese four ")
else:
     print( a4 ," is graeter number among tese four ")