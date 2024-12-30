# A list in Python is a collection of items that are:

# Ordered: Items are stored in a specific sequence.
# Mutable: The contents of a list can be modified (e.g., add, remove, or update items).
# Heterogeneous: A list can contain items of different data types (e.g., integers, strings, other lists).
# Lists are defined using square brackets [], and elements are separated by commas.

friends=["Apple","Orange",5,345.06,False,"vishal"]

print(friends[0])

print(friends)
friends[0]="Mango" # unlike string list is mutable
print(friends[0]) 

print(friends)

print(friends[1:4])