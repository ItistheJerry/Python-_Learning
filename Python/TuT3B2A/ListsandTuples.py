# In any programming language if we want to store many similar elemts we either use array or lists
# Lists are used in python an Array

# Arrays are homogeneous (all elements of the same type) fixed size, while lists are heterogeneous (elements can be different) are dynamic.
# In simplest form is Containers to store set of values of any data types

friends = ["apple", "akash", "rohan", 7, False]
# it has strings, can store value of any datatype, int , bool

# List INDEXING
print(friends[0])
# Unlike strings lists are mutable
friends[0] = "Apples"
friends[1] = "Akash"
# same indexing can be performed with lists as with strings
# As in string methods a new string is returning then we have to print it
# but in lists we can change the elements

# List Method

# insertion at the end of list
friends.append("Jerry")
print(friends)

l1 = [1, 34, 62, 2, 6, 11, 21]

# sort = as name suggests updates the list


# reverse = as name suggests it reverses the list


# insert(3,8) = adds 8 at index 3

# fruits = []
# insert(0,(input("Enter Fruit 1: ")))

# pop(2) = will delete element at index 2 and then returns its value


# remove(21) = will remove 21 from the list

print(l1)

l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,8)
print(l1)
l1.pop(3)
print(l1)
l1.remove(21)
print(l1)


# print(v,a,l,u,e)



# TUPLES
# Is a immutable Datatype in python

a = () #empty tuple
b = (1, ) # Tuple with only one element needs a comma
c = (1, 7, 6, 3, 5) # Tuple with more than one element
print(type(a)) # = Will return tuple

# TUPLE METHODS

d = (1, 7, 6, 2, 1, "Jerry")

print(d.count(1)) # = Number of times 1 returns
# print(d)
print(d.index(1)) # = Will return index of first occurance of 1
# print(d)

n = d.index("Jerry")
print(n)


# c[2] = 35
# print(c)
#'tuple' object does not support item assignment



d.__add__
d.__class_getitem__
d.__contains__
d.__delattr__
d.__dir__
d * 3
