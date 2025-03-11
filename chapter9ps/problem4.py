# a file contains a word "Donkey" multiple tiomes you need to write it to a program which replace the the word with ##### by updating the file
word="Donkey"

with open("file.txt","r") as f:
    content=f.read()
contentNew=content.replace(word,"#####")
with open("file.txt",'w') as f:
    f.write(contentNew)    