# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Count Method: Count occurrences of 'x' in the tuple
count_20 = my_tuple.count(20)  # Counting how many times 20 appears in the tuple
print("Count of 20:", count_20)  # Output: 1

# 2. Index Method: Return the index of the first occurrence of 'x' in the tuple
index_of_30 = my_tuple.index(30)  # Finding the index of the first occurrence of 30
print("Index of 30:", index_of_30)  # Output: 2

# 3. Concatenation: Combine two tuples into one
another_tuple = (60, 70)
concatenated_tuple = my_tuple + another_tuple  # Concatenating my_tuple and another_tuple
print("Concatenated tuple:", concatenated_tuple)  # Output: (10, 20, 30, 40, 50, 60, 70)

# 4. Repetition: Repeat the tuple multiple times
repeated_tuple = my_tuple * 2  # Repeating the tuple twice
print("Repeated tuple:", repeated_tuple)  # Output: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# 5. Slicing: Extract a part of the tuple (sub-tuple)
sliced_tuple = my_tuple[1:4]  # Extracting elements from index 1 to index 3
print("Sliced tuple:", sliced_tuple)  # Output: (20, 30, 40)

# 6. Membership Test: Check if an element exists in the tuple
is_30_in_tuple = 30 in my_tuple  # Checking if 30 is in my_tuple
print("Is 30 in the tuple?", is_30_in_tuple)  # Output: True

is_100_not_in_tuple = 100 not in my_tuple  # Checking if 100 is NOT in my_tuple
print("Is 100 not in the tuple?", is_100_not_in_tuple)  # Output: True

# 7. Length: Get the number of elements in the tuple
length_of_tuple = len(my_tuple)  # Getting the length of my_tuple
print("Length of tuple:", length_of_tuple)  # Output: 5
