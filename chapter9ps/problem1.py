#write a program to read the text from a given file poems.txt and find out whether it contain the word twinkle
f=open("poems.txt")
word=f.read()

if "twinkle" in word:
    print("the word is found")
else:
    print("the word not found")    

f.close()    