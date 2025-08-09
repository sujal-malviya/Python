# Strings :-
# This are sequence of Characters. 
# Python treats anything inside quotes as a string .
# Python don't have Character datatype.

s = "GFG"
print(s)
print(s[0]) # accessing with index
s1 = s[0]+'F'
s += s1 
print(s1)
print(s)
# From this line we can say that strings are immutable.
s = s+"Hello"
print(id(s))
# s[0] = "F"
print(s)
# For accessing the character in string we can use indexing.
  
  
# String can be written in single as well as double quotes.
st = 'GFG'
st1 = "GFG"
print(st,"-",st1)# if the value is same then both variable will refer the same value .
# In memory the object is created where the value is stored so whenever the value is same for two diffrent variable so they both will point to same value.
 
# Multi line String.

work = '''I am Learning from Geeks For Geeks'''
print(f"In this i used multiline string where i used triple quotes {work}")

print("-----------------------------This wsa multi-line string")
# Accessing Character :-
# 1) as we know the index starts from zero and then it will continue upto len-1.
# 2) we will go left to right so it is 0 to len-1 and from right to left it will start with -1.
name = "sujal"
print(f"Index 0 : {name[0]}")
print(f"Index -1 : {name[-1]}")
print("------------------before part was about indexing")
print(name[0]+name[1]+name[2]+name[3]+name[4])
print("----------------------------------------by simple concatenation with indices")
for i in name:
    print(i,end ="")
print("----------------------------------- by for loop")
print(name)
# basic logics :-
name = "malviya"
print(name)
print("-----------------------after name was concatenated")
print("------------------------become twice")
name = name + name # in this line u can see we have added one more malviya to the string 
# we can edit the character  but we can append the characters.
print(name)
print("---------------------------------in below code name became 4times in print statement" )
print(name+name)
print(name)
# String Slicing :-
 # this is a way to extract portion of string by specifying the start and end index.
movie = "Sci-Fi"
print(movie[:])
print(movie[0:])
print(movie[0:5])
print(movie[0:6])
print(movie[:6])
print(movie[:3])
print(movie[-1])
print(movie[:-1])
print(movie[-1:])
print(movie[-2:])
print(movie[-5:])
print(movie[-7:])
print("-----------------------if we want to step we will use this syntax")
print(movie[0::1])
print(movie[0::2])
print(movie[::-1])
print(movie[10:])
# to delete a string we will use del keyword
del movie
# print(movie)
# To update a part of string we need to create a new string. as we know string are immutable.
str1 = "Hello Geeks"
str2 = "H" + str1[1:]
str3 = str1.replace("Geeks","GeeksforGeeks")
print(str1)
print(str3)
print(str2)
# Common string methods -
print(len(str3))
print(str3.upper())
print(str2.lower())
newstr = "      GFG      "
print("to remove all whitespace ")
print(newstr.strip())
# Concatenating strings :-
a = "Hey" 
b = "Man"
print(a+"! "+b)
# we can repaet a string multiple time using * operator.
print(a*3)
# Formatting string :-

name ="sujal"
age = 21
print(f"I am {name} and i am {age} year old.")
print("name : {} , age : {}".format("raja",24))
# using string member ship -
k = "flower of dooms !!"
print("flower" in k)
