#write a program to fill in a letter template given below with name and date
letter='''Dear <|Name|>,
you are selected!
<|Date|>
'''
name=input("Enter nmae:")
date=input("Enter date")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))

