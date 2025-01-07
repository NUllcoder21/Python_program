# can we change the value inside a list which contained in a set s

s={8,7,12,"Vishal",[1,2]}

# No, you cannot change the value inside a list that is contained in a set. This is because sets in Python require their elements to be immutable (unchangeable) and hashable.

# Lists are mutable and cannot be hashed, so you cannot include a list as an element of a set. If you try to create a set with a list as one of its elements, Python will raise a TypeError.