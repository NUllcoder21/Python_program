# write a program to mine a log file and find out whether it contains python
with open("log.txt")as f:
    content=f.read()
if("python" in content):
    print("yes python is present in it")
else:
    print("no python is not present in it")        