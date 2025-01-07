#what will be the length of the following set S:

s=set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s))

# here we push the three value but it print the lenght two because the python considers the 20 and 20.0 as same


