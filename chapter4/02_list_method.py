# Starting list
my_list = [3, 1, 4, 2]

# 1. Adding Elements
# Append an element to the end of the list
my_list.append(5)  # List becomes: [3, 1, 4, 2, 5]
print("After append:", my_list)

# Insert an element at a specific index
my_list.insert(1, 7)  # Inserts 7 at index 1 -> [3, 7, 1, 4, 2, 5]
print("After insert:", my_list)

# Extend the list by appending elements from another list
my_list.extend([6, 8])  # List becomes: [3, 7, 1, 4, 2, 5, 6, 8]
print("After extend:", my_list)

# 2. Removing Elements
# Remove the first occurrence of a specific value
my_list.remove(4)  # Removes 4 -> [3, 7, 1, 2, 5, 6, 8]
print("After remove:", my_list)

# Remove and return the element at a specific index
removed_element = my_list.pop(2)  # Removes element at index 2 -> [3, 7, 2, 5, 6, 8]
print("After pop:", my_list)
print("Removed element:", removed_element)

# Clear all elements from the list
temp_list = my_list.copy()  # Create a copy before clearing for further use
my_list.clear()  # Clears the list -> []
print("After clear:", my_list)

# Reset my_list for further operations
my_list = temp_list  # Restore the list: [3, 7, 2, 5, 6, 8]

# 3. Searching and Counting
# Find the index of the first occurrence of a value
index_of_7 = my_list.index(7)  # Finds 7 -> Index: 1
print("Index of 7:", index_of_7)

# Count the occurrences of a specific value
count_of_5 = my_list.count(5)  # Counts 5 -> 1
print("Count of 5:", count_of_5)

# 4. Sorting and Reversing
# Sort the list in ascending order
my_list.sort()  # List becomes: [2, 3, 5, 6, 7, 8]
print("After sort:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)  # List becomes: [8, 7, 6, 5, 3, 2]
print("After sort (descending):", my_list)

# Reverse the elements of the list
my_list.reverse()  # List becomes: [2, 3, 5, 6, 7, 8]
print("After reverse:", my_list)

# 5. Copying
# Create a shallow copy of the list
copied_list = my_list.copy()  # copied_list: [2, 3, 5, 6, 7, 8]
print("Copied list:", copied_list)

# 6. Clearing
# Clear all elements from the list again
my_list.clear()  # List becomes: []
print("After final clear:", my_list)

# Final state of copied_list
print("Final copied list:", copied_list)
