name="vishal"

#pring the length of string
print(len(name))

#check the string ends with given word

print(name.endswith("al"))

# check that the string is start with given string
print(name.startswith("v"))

#change the first char of word of string in capital
print(name.capitalize())

replace_string=name.replace("vishal","Badal")

print(replace_string)

reversed_string = name[::-1]
print(reversed_string)


# Basic String Methods
text = "  Hello Python!  "

print(text.upper())       # Converts all characters to uppercase -> "  HELLO PYTHON!  "
print(text.lower())       # Converts all characters to lowercase -> "  hello python!  "
print(text.capitalize())  # Capitalizes the first character -> "  hello python!"
print(text.title())       # Capitalizes the first letter of each word -> "  Hello Python!"
print(text.strip())       # Removes leading and trailing whitespaces -> "Hello Python!"
print(text.lstrip())      # Removes leading whitespaces -> "Hello Python!  "
print(text.rstrip())      # Removes trailing whitespaces -> "  Hello Python!"

# Searching and Replacing
print(text.find("Python"))      # Finds substring "Python" -> 8
print(text.index("Python"))     # Similar to find() but raises error if not found -> 8
print(text.count("l"))          # Counts occurrences of 'l' -> 2
print(text.replace("Python", "World"))  # Replaces "Python" with "World" -> "  Hello World!  "

# String Checking
print(text.startswith("  H"))   # Checks if string starts with "  H" -> True
print(text.endswith("!  "))     # Checks if string ends with "!  " -> True
print("Hello".isalpha())        # Checks if all characters are alphabetic -> True
print("12345".isdigit())        # Checks if all characters are digits -> True
print("Hello123".isalnum())     # Checks if all characters are alphanumeric -> True
print("   ".isspace())          # Checks if string contains only spaces -> True
print("HELLO".isupper())        # Checks if all characters are uppercase -> True
print("hello".islower())        # Checks if all characters are lowercase -> True

# Splitting and Joining
words = text.split()            # Splits into list by spaces -> ['Hello', 'Python!']
print(words)
print(" ".join(words))          # Joins list elements into a string with spaces -> "Hello Python!"
lines = "Line1\nLine2\nLine3"
print(lines.splitlines())       # Splits by line breaks -> ['Line1', 'Line2', 'Line3']

# String Alignment
print(text.center(20))          # Centers the text in 20-char width -> "    Hello Python!   "
print(text.ljust(20))           # Left-aligns in 20-char width -> "  Hello Python!      "
print(text.rjust(20))           # Right-aligns in 20-char width -> "      Hello Python!  "
print("42".zfill(5))            # Pads with zeros to make the string 5 characters -> "00042"

# Encoding and Decoding
encoded_text = text.encode('utf-8')  # Encodes the string to bytes using UTF-8
print(encoded_text)                  # Outputs: b'  Hello Python!  '
decoded_text = encoded_text.decode('utf-8')  # Decodes bytes back to string
print(decoded_text)                  # Outputs: "  Hello Python!  "