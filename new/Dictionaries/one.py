# Dictionaries -
# it is a data structure that stores the value in key :value pairs.
# values can be duplicated , whereas key can not be repeated and must be immutable.
 
dict1 = {1:"Geeks", 2:"For",3:"Geeks"}
print(dict1)
# dict constructor

b = dict({1:"apple",2:"for"})
print(b)
# dictionary is case-sensitive
# key must be immutable
# key must be unique
# dictionary internally uses hashing. Hence , operation like search ,insert ,delete can perform in constant time.

e = {1:"Hello",2:"World",(4,3):[1,2,3,4]}
print(e)
print(e[1])
# with help of key as index we can access dictionary
print(e.get((4,3)))
# with the help of get function we can access the dictionary.
# dictionary is mutable
dict2 = {1:"python",2:"is",3:"good"}
dict2["func"] = "super!!!"
dict2[1] = "PYTHON"
print(dict2)
print()
# removing dictionary items
# del statement :-
# pop() :-
# clear() :- full clear krdega
# popitem :- first se item  clear krega
for key,value in dict2.items():
    print(key," : ",value)

# shallow copy padna hai
# Deep Copy padna hai
