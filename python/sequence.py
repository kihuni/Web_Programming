# list - is sequemce of mutable values i.e can be changed
# tuple - sequence of immutable values i.e cannot be changed
# set - collection of uniques values
# dict - collection of key-value pairs etc

# Examples some datastructure above

names = ["harrry", "john", "mike"] # list
print(names)

names.append("kamau") # appending name to names list
print(names)

# set
s = set()
# append elements to set
s.add(1)
s.add(2)
s.add(3)
print(s)

# dictionary

peoples = {"john":1, "kamau":2}
print(peoples["john"])