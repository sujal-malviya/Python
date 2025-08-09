# List is built-in dynamic sized array (automatically grows and shrinks)
# list contain duplicate items.
# List are ordered 
# List are mutable , order of element based on how they are added.
# List store all type of data that can mixed as well.
a = [10,20,"bhoo",2.2,True]
print(a)
print(a[0])
print(type(a))
print(type(type))
print(type(type(int)))
# List stores referencees , not values.
a = [1,2,3]
b = ["apple","banana","grapes"]
c = [True,False]
print(a)
print(b)
print(c)
# creating List with help of list constructor :-
d = list((1,2,3))
print(d)
e = list((1,2,2.2,"apple",True))
print(e)
# creating list with repeated ekements :-
f = [0]*5
print(f)
g = [2]*5
print(g)
# Accessing elements in List :-
# with index we can access the element in list.
a = [10,20,30,40,50]
print(a[0])
print(a[-1])
# For adding element into list :-
# 1) Append :-
# 2) extend :-
# 3) insert :-
print(a)
a.append(100)
print(a)
# ouput -  [10, 20, 30, 40, 50, 100]
a.extend([11,12,13])
print(a)
# output - [10, 20, 30, 40, 50, 100, 11, 12, 13]
a.insert(0,200)
print(a)
# in insert command it will insert the value like insert(postion,value)
# output - [200, 10, 20, 30, 40, 50, 100, 11, 12, 13]


# List is mutable -
a[0] = 111
print(a)
 
# For removing element from list :-

# 1) remove() :-
# 2) pop() :-
# 3) del statement :-
a.remove(10)
print(a)
print(a.pop()) # pop function u can write index based on removal of value.
# pop deletes the last element and  from remove u can remove the particular element .
print(a)
del a[0]
print(a)

# Iterating over List :-

a =["applle","banana","grapes"]
for i in a:
    print(i,end=" ")
print()
# Nested List :-

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix ,sep=" ")
 
print()
#List Comprehension -

sq =[x**2 for x  in range(1,5)]
print(sq)
even = [x for x in range(1,20) if x%2==0]
print(even)