# write a progarm to find out whether a student has passes or failed if it required a total of 40% and and at leasty 33% in each subject to pas Assume 3 subjects and take marks as an input from the user
math = int(input("Enter the marks of math:"))
physics=int(input("Enetr the marks of physics:"))
chemistry=int(input("Enetr the marks of chemistry:"))
total=(math+physics+chemistry) /3

if(total>=40 and math>=33 and physics>=33 and chemistry>=33):
    print("you are  pass as well as in each subject")


else:
    print("you are fail")    


