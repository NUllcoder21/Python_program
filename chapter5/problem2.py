# All dict methods

# Dictionary for demonstration
my_dict = {'a': 1, 'b': 2, 'c': 3}

# clear() - Removes all items from the dictionary
my_dict.clear()
print("After clear():", my_dict)  # Output: {}

# Reinitializing the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# copy() - Returns a shallow copy of the dictionary
new_dict = my_dict.copy()
print("After copy():", new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# fromkeys() - Creates a new dictionary from given keys with a default value
keys = ['x', 'y', 'z']
default_dict = dict.fromkeys(keys, 0)
print("Using fromkeys():", default_dict)  # Output: {'x': 0, 'y': 0, 'z': 0}

# get() - Returns the value for a specified key, or a default value if the key doesn't exist
value = my_dict.get('b', 'default_value')
print("Using get():", value)  # Output: 2

# items() - Returns all key-value pairs as tuples
for key, value in my_dict.items():
    print("Using items():", key, value)

# keys() - Returns all keys in the dictionary
all_keys = my_dict.keys()
print("Using keys():", list(all_keys))  # Output: ['a', 'b', 'c']

# values() - Returns all values in the dictionary
all_values = my_dict.values()
print("Using values():", list(all_values))  # Output: [1, 2, 3]

# pop() - Removes the specified key and returns its value
removed_value = my_dict.pop('a', 'default_value')
print("Using pop():", removed_value)  # Output: 1
print("After pop():", my_dict)  # Output: {'b': 2, 'c': 3}

# popitem() - Removes and returns the last inserted key-value pair as a tuple
key, value = my_dict.popitem()
print("Using popitem():", (key, value))  # Output: ('c', 3)
print("After popitem():", my_dict)  # Output: {'b': 2}

# Reinitializing the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# setdefault() - Returns the value of a key, or sets it to a default if not present
default_value = my_dict.setdefault('d', 4)
print("Using setdefault():", default_value)  # Output: 4
print("After setdefault():", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# update() - Updates the dictionary with key-value pairs from another dictionary
my_dict.update({'e': 5, 'f': 6})
print("After update():", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
