# Dictionary is a Collection of Keys-Value Pairs


marks = {
    "Jerry" : 100,
    "Samyak" : 100,
    "GunGun" : 100
}

# print(marks, type(marks))
# this wont work
#print(marks[0])

# print(marks["Jerry"])


# Properties
# it is unordered
# it is mutable
# it is indexed
# cannot duplicate Keys
# strings or integers can be used



# Dictionary Methods

# print(marks.items())  # gives list of key value items in form of a tuple
# print(marks.values()) # right side
# print(marks.keys()) # left side

# as dictionary can be updated, curent items can be changed and new one can be added

# marks.update({"GunGun": 99})
# print(marks)



# GET
#  a.get("name") Returns the value of the specific keys ( and value is returned eg "Jerry" is returned here)

print(marks.get("Jerry"))

# pop
# pop item









# SETS  = is a collection of well defined objects and also a collection of non - repetitive elements

# s = {} # empty dictionary
# e = set() # Empty set
# f = {1, 4, 7} # is a set




# set methods

f = {1, 4, 7}

print(f, type(f))

# set.add  = 
f.add(566)

# print(f, type(f))

# set.clear 
# set.discard
# set.difference
# set.difference_update




# Properties
 # Are unordered = elements order dosen't matter
 # Are unindexed = Cannot access elements by index
 # No way to change existing items in a set
 # Sets cannot contain duplicate Values


# Operations on Sets

# len(f) : Returns 4 the length of the above set 
# f.remove(7) = Updates the set f and removes 8 from f
# f.pop() = Removes an arbitary from the set and return the element removed
# f.clear() = Empties the set f
# f.union(4, 34) = Returns a new set with all itmes from both sets {1,4,7,566,34}
# f.intersection(4, 34) = Returns a set which contain only item in both sets (4).

# print(len(f))
# f.remove(1)
# f.pop()
print(f)
s1 = {1,8,5,6}
s2 = {2,7,8,3}
print(s1.union(s2))
print(s1.intersection(s2))

# Try more set methods properties and all using chatgpt
# n = set()
# n1 = int(input("Enter a number: "))
# n.add(n1)
# n2 = int(input("Enter a number: "))
# n.add(n2)
# n3 = int(input("Enter a Number: "))
# n.add(n3)

# print(n)