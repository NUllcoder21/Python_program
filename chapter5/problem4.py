# set all methods

# Initializing sets for demonstration
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# add() - Adds an element to the set
set1.add(5)
print("After add(5):", set1)  # Output: {1, 2, 3, 4, 5}

# remove() - Removes an element from the set (raises KeyError if not found)
set1.remove(5)
print("After remove(5):", set1)  # Output: {1, 2, 3, 4}

# discard() - Removes an element from the set (no error if not found)
set1.discard(4)
set1.discard(10)  # No error even if 10 is not present
print("After discard(4, 10):", set1)  # Output: {1, 2, 3}

# pop() - Removes and returns an arbitrary element from the set
removed_element = set1.pop()
print("After pop():", removed_element, "Remaining set:", set1)  # Output: Removed element, Remaining set

# clear() - Removes all elements from the set
set1.clear()
print("After clear():", set1)  # Output: set()

# Reinitializing sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# union() - Returns a new set with all elements from both sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# intersection() - Returns a new set with common elements
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)  # Output: {3, 4}

# difference() - Returns a new set with elements in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)  # Output: {1, 2}

# symmetric_difference() - Returns a new set with elements not in both sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# issubset() - Checks if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?:", is_subset)  # Output: False

# issuperset() - Checks if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?:", is_superset)  # Output: False

# isdisjoint() - Checks if set1 and set2 have no common elements
is_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?:", is_disjoint)  # Output: False

# update() - Updates set1 with the union of set1 and another set
set1.update({5, 6})
print("After update({5, 6}):", set1)  # Output: {1, 2, 3, 4, 5, 6}

# intersection_update() - Updates set1 with the intersection of set1 and another set
set1.intersection_update({3, 4, 5})
print("After intersection_update({3, 4, 5}):", set1)  # Output: {3, 4, 5}

# difference_update() - Updates set1 by removing elements found in another set
set1.difference_update({4, 5})
print("After difference_update({4, 5}):", set1)  # Output: {3}

# symmetric_difference_update() - Updates set1 with elements not in both sets
set1.symmetric_difference_update({3, 6, 7})
print("After symmetric_difference_update({3, 6, 7}):", set1)  # Output: {6, 7}
