for i in range(4):
    print(i)

l =[1,2,3,4,5,67,8]
for i in l:
    print(i)


t=(1,23,4,5,67,7)
for i in t:
    print(i)  

# Break example
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# Continue example
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4


for i in range(5):
    print(i)
else:
    print("Loop finished")

# Converting a string to uppercase
text = "hello world"
uppercase_text = text.upper()
print(uppercase_text)  # Output: "HELLO WORLD"


# Converting a list of strings to uppercase
words = ["python", "java", "c++"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['PYTHON', 'JAVA', 'C++']
