# Tuple -
# This are immutable .
# this are ordered collection of elements.
# this can hold diffrent data types
# main Characterstics - ordered , hetrogeneous immutable.

t = (1,2,3)
print(type(t))
print(t)

# about indexing same like list
print(t[0])
print(t[-1])
t = (0)*5
print(t)
print(t)
# t[0] = 1
# print(t) as we know that tuple are immutable so we can not assign value in it.
tup = (1,"Geek",2.2)
print(tup)
mlsit = [1,2,3,"Geek"]
print(tuple(mlsit))

# Iterating tuple -
for i in tup:
    print(i,end=" ")

# Basic Operations -
# accesing python tuple
# concatenate tuple (using + operator)
# slicing tuple
# deleting tuple
print()
t1 = (1,2,3)
t2 = ("a","b","c")
t3 = t1 + t2
print(t3)

# for deleting 
del t3
# print(t3)
# not defined t3

# * opeartor is used in tuple to grap multiple items in unpacking of tuple.
tup = (1,2,3,4,5,6)

a , *b ,c = tup
print(a)
print(b)
print(c)
