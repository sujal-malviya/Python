PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python> python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.      
>>> import random
>>> random.random()
0.11754517037635603
>>> random.choice()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    random.choice()
    ~~~~~~~~~~~~~^^
TypeError: Random.choice() missing 1 required positional argument: 'seq'
>>> l1 = [1,2,3,4]
>>> random.choice(l1)
4
>>> random.choice(l1)
2
>>> random.choice(l1)
4
>>> random.choice(l1)
3
>>> random.choice(l1)
1
>>> random.shuffle(l1)
>>> l1
[4, 1, 3, 2]
>>> l1
[4, 1, 3, 2]
>>> random.shuffle(l1)
>>> l1
[2, 1, 3, 4]
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')
Decimal('0.2')
>>>
KeyboardInterrupt
>>> from fractions import fraction
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    from fractions import fraction
ImportError: cannot import name 'fraction' from 'fractions' (C:\Program Files\Python313\Lib\fractions.py). Did you mean: 'Fraction'?
>>> from fractions import fractions
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    from fractions import fractions
ImportError: cannot import name 'fractions' from 'fractions' (C:\Program Files\Python313\Lib\fractions.py). Did you mean: 'Fraction'?
>>> from fractions import Fraction 
>>> m = 1/2
>>> m
0.5
>>> my = Fraction(2/4)
>>> my
Fraction(1, 2)
>>> setone = {1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone |{1,3}
{1, 2, 3, 4}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone - {1,2,3,4}
set()
>>> type(set())
<class 'set'>
>>> type({})    
<class 'dict'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    type(true)
>>> True is equal 1
  File "<stdin>", line 1
    True is equal 1
                  ^
SyntaxError: invalid syntax
>>> True isequal 1
  File "<stdin>", line 1
    True isequal 1
         ^^^^^^^
SyntaxError: invalid syntax
>>> True is 1
<stdin>-34:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?    
False
>>> True + 4
5
>>>
 *  History restored 

PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python> python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> "" "" ""
''
>>> chai = "chai"
>>> chai
'chai'
>>> chai = 'Lemonn tea'
>>> chai
'Lemonn tea'
>>> chai(1:2)
  File "<stdin>", line 1
    chai(1:2)
          ^
SyntaxError: invalid syntax
>>> chai[1:2]
'e'
>>> first_char = chai[0]
>>> first_char
'L'
>>> print(first_char)
L
>>> slice_chai = chai[7:10]
>>> slice_chai 
'tea'
>>> slice_chai1 = chai[0:7]
>>> slice_chai1
'Lemonn '
>>> chai[-1]
'a'
>>> num_list = "0123456789"
>>> numlist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    numlist
NameError: name 'numlist' is not defined. Did you mean: 'num_list'?
>>> num_list
'0123456789'
>>> num_list[0:5]
'01234'
>>> num_list[0:]
'0123456789'
>>> num_list[-1:] 
'9'
>>> num_list[-10:] 
'0123456789'
>>> num_list[0:7:2] 
'0246'
>>> num_list[0:7:3] 
'036'
>>> num_list[-1:7:-2] 
'9'
>>> print(chai.lower())
lemonn tea
>>> print(chai.upper())   
LEMONN TEA
>>> chai = "   Masala tea"
>>> chai
'   Masala tea'
>>> print(chai.strip)
<built-in method strip of str object at 0x000001CCC3742AF0>
>>> print(chai.strip()) 
Masala tea
>>>  chai = 'Lemon chai'
  File "<stdin>", line 1
    chai = 'Lemon chai'
IndentationError: unexpected indent
>>> chai = 'Lemon chai'  
>>> print(chai.replace("lemon"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(chai.replace("lemon"))
          ~~~~~~~~~~~~^^^^^^^^^
TypeError: replace() takes at least 2 positional arguments (1 given)
>>> print(chai.replace("Lemon")) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(chai.replace("Lemon"))
          ~~~~~~~~~~~~^^^^^^^^^
TypeError: replace() takes at least 2 positional arguments (1 given)
>>> print(chai.replace("Lemon","ginger)) 
  File "<stdin>", line 1
    print(chai.replace("Lemon","ginger))
                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(chai.replace("Lemon","ginger")) 
ginger chai
>>> chai = "Lemon , Ginger, Masala, Mint "
>>> print(chai.split())
['Lemon', ',', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", ")) 
['Lemon ', 'Ginger', 'Masala', 'Mint ']
>>> chai = "Masala chai"
>>> print(chai.find("chai"))
7
>>> print(chai.find("Chai"))
-1
>>> chai = "Masala chai chai chai"
>>> print(chai.count("chai"))
3
>>> chai_type = "Masala chai"
>>> quantity = 1
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type)) 
I ordered 2 cups of Masala chai chai
>>> chai_variety = ["lemon","masala","ginger"] 
>>> chai_variety
['lemon', 'masala', 'ginger']
>>> print("".join(chai_variety)) 
lemonmasalaginger
>>> print(" ".join(chai_variety)) 
lemon masala ginger
>>> print("# ".join(chai_variety)) 
lemon# masala# ginger
>>> chai
'Masala chai chai chai'
>>> chai ="Masala chai"
>>> chai
'Masala chai'
>>> print(len(chai))
11
>>> for i in chai
  File "<stdin>", line 1
    for i in chai
                 ^
SyntaxError: expected ':'
>>> for i in chai:
... print(chai)
  File "<stdin>", line 2
    print(chai)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in chai:
... print(i)
  File "<stdin>", line 2
    print(i)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in chai:
... print(i) 
  File "<stdin>", line 2
    print(i)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in chai:
... print(chai)    
  File "<stdin>", line 2
    print(chai)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in chai:
... print(i)         
  File "<stdin>", line 2
    print(i)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in chai:
...     print(i)    
...
M
a
s
a
l
a

c
h
a
i
>>> chai = "He said ,\"Masala chai is awesome\" " 
>>> chai
'He said ,"Masala chai is awesome" '
>>> chai = "Masala\nchai"
>>> chai
'Masala\nchai'
>>> print(chai)
Masala
chai
>>> chai = r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> print(chai)
Masala\nchai
>>> chai = r"c:\user\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>> chai = "c:\user\pwd"
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> chai = "c:\\user\\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>> unicode escaping
  File "<stdin>", line 1
    unicode escaping
            ^^^^^^^^
SyntaxError: invalid syntax
>>> chai = "Masala chai"
>>> print("Masala" in chai)
True
>>> tea_variety = "Wong tea"
>>> tea_variety
'Wong tea'
>>> tea_variety = ["Black" , "Green","Oolong","white"]
>>> print(tea_variety)
['Black', 'Green', 'Oolong', 'white']
>>> tea_variety.append("Blue")
>>> tea_variety
['Black', 'Green', 'Oolong', 'white', 'Blue']
>>> tea_variety.remove("Blue")
>>> tea_variety
['Black', 'Green', 'Oolong', 'white']
>>> tea_variety[1:3] = ["blue","red"]
>>> tea_variety                      
['Black', 'blue', 'red', 'white']
>>> tea_variety[1:1]
[]
>>> tea_variety[1:1] = ["test","test"]
>>> tea_variety      
['Black', 'test', 'test', 'blue', 'red', 'white']
>>> tea_variety[1:2]
['test']
>>> tea_variety[1:3] 
['test', 'test']
>>> tea_variety[1:3] = []
>>> tea_variety           
['Black', 'blue', 'red', 'white']
>>> for i in te_varity:
...    print(i)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for i in te_varity:
             ^^^^^^^^^
NameError: name 'te_varity' is not defined. Did you mean: 'tea_variety'?
>>> for i in te_varity:
...     print(tea_variety)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for i in te_varity:
             ^^^^^^^^^
NameError: name 'te_varity' is not defined. Did you mean: 'tea_variety'?
>>> for i in tea_varity:   
...     print(tea_variety)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for i in tea_varity:
             ^^^^^^^^^^
NameError: name 'tea_varity' is not defined. Did you mean: 'tea_variety'?
>>> for i in tea_varity:   
...     print(i)           
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for i in tea_varity:
             ^^^^^^^^^^
NameError: name 'tea_varity' is not defined. Did you mean: 'tea_variety'?
>>> for i in tea_variety:  
...     print(i)
...
Black
blue
red
white
>>> for i in tea_varity:
...     print(i,end="-")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for i in tea_varity:
             ^^^^^^^^^^
NameError: name 'tea_varity' is not defined. Did you mean: 'tea_variety'?
>>> for i in tea_variety: 
...     print(i,end="-")  
...
Black-blue-red-white->>>
KeyboardInterrupt
>>> if "oOlong" in tea_variety:
...     print("I have")
...
>>> tea_variety.append("oolong")
>>> if "oolong" in tea_variety: 
...     print("I have")
...
I have
>>> tea_variety.pop()
'oolong'
>>> tea_variety      
['Black', 'blue', 'red', 'white']
>>> tea_variety.insert(1,"oolong")
>>> tea_variety
['Black', 'oolong', 'blue', 'red', 'white']
>>> tea_variety_copy = tea_variety
>>> tea_variety_copy              
['Black', 'oolong', 'blue', 'red', 'white']
>>> tea_variety_copy = tea_variety.copy()
>>> tea_variety_copy
['Black', 'oolong', 'blue', 'red', 'white']
>>> square_num = [x**2 for x in range(10)]
>>> square_num                             
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> square_num = [x**3 for x in range(10)] 
>>> square_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> chai_types = {"first":"Masala","second":"Green","third":"herbal"}
>>> chai_types
{'first': 'Masala', 'second': 'Green', 'third': 'herbal'}
>>> chai_types[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types[0]
    ~~~~~~~~~~^^^
KeyError: 0
>>> chai_types["Masala"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types["Masala"]
    ~~~~~~~~~~^^^^^^^^^^
KeyError: 'Masala'
>>> chai_types["first"]  
'Masala'
>>> chai_types.get["first"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.get["first"]
    ~~~~~~~~~~~~~~^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> chai_types.get["Masala"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.get["Masala"]
    ~~~~~~~~~~~~~~^^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> chai_types.get["Ginger"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.get["Ginger"]
    ~~~~~~~~~~~~~~^^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> chai_types.get["Gingery"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.get["Gingery"]
    ~~~~~~~~~~~~~~^^^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> chai_types.get["Gingery":"zency"] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.get["Gingery":"zency"]
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> for i in chai_types:
...     print(i)
...
first
second
third
>>> for i in chai_types:
...     print(i,chai_types[i])
...
first Masala
second Green
third herbal
>>> for key,values in chai_types.items(): 
...     print(key,values)
...
first Masala
second Green
third herbal
>>> if "Masala" in chai_types:
...     print("Yes")
...
>>> if "first" in chai_types:  
...     print("Yes")
...
Yes
>>> print(len(chai_types)
...
...     
...
KeyboardInterrupt
>>> print(len(chai_types))
3
>>> chai_types["earld":"citrus"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types["earld":"citrus"]
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^
KeyError: slice('earld', 'citrus', None)
>>> chai_types["earld"]="Citrus" 
>>> chai_types                  
{'first': 'Masala', 'second': 'Green', 'third': 'herbal', 'earld': 'Citrus'}
>>> chai_types.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.pop()
    ~~~~~~~~~~~~~~^^
TypeError: pop expected at least 1 argument, got 0
>>> chai_types.pop("earld")) 
  File "<stdin>", line 1
    chai_types.pop("earld"))
                           ^
SyntaxError: unmatched ')'
>>> chai_types.pop("earld") 
'Citrus'
>>> chai_types.popitem()
('third', 'herbal')
>>> chai_types       
{'first': 'Masala', 'second': 'Green'}
>>> print(len(chai_types))
2
>>> chai_types.delete("second")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.delete("second")
    ^^^^^^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'delete'
>>> del chai_types["second")    
  File "<stdin>", line 1
    del chai_types["second")
                           ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> del chai_types["second"]
>>> chai_types
{'first': 'Masala'}
>>> chai_types_cpy = chai_types
>>> chai_types_cpy             
{'first': 'Masala'}
>>> tea_shop = {
... "chai":{"Masala":"spicy","ginger":"zesty"},
... "tea":{"Green":"Mild","Balck":"Strong"}
... }
>>> tea_shop 
{'chai': {'Masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'Green': 'Mild', 'Balck': 'Strong'}}  
>>> print(tea_shop)
{'chai': {'Masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'Green': 'Mild', 'Balck': 'Strong'}}  
>>> print(tea_shop[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(tea_shop[0])
          ~~~~~~~~^^^
KeyError: 0
>>> print(tea_shop["chai])) 
  File "<stdin>", line 1
    print(tea_shop["chai]))
                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(tea_shop["chai]) 
  File "<stdin>", line 1
    print(tea_shop["chai])
                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(tea_shop["chai"]) 
{'Masala': 'spicy', 'ginger': 'zesty'}
>>> print(tea_shop[["ginger"]) 
  File "<stdin>", line 1
    print(tea_shop[["ginger"])
                             ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(tea_shop[["ginger"]]) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(tea_shop[["ginger"]])
          ~~~~~~~~^^^^^^^^^^^^
TypeError: unhashable type: 'list'
>>> print(tea_shop["chai"]["ginger"]) 
zesty
>>> square_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> square_num ={ x:x**2 for x in range(5)}
>>> square_num                             
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>> square_num.clear()
>>> square_num
{}
>>> del square_num
>>> square_num
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    square_num
NameError: name 'square_num' is not defined
>>> keys = {"masala":"spicy","ginger":"zesty"}
>>> keys
{'masala': 'spicy', 'ginger': 'zesty'}
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys,default_vlaue)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    new_dict = dict.fromkeys(keys,default_vlaue)
                                  ^^^^^^^^^^^^^
NameError: name 'default_vlaue' is not defined. Did you mean: 'default_value'?
>>> new_dict = dict.fromkeys(keys,default_value) 
>>> new_dict                                    
{'masala': 'Delicious', 'ginger': 'Delicious'}
>>> new_dict = dict.fromkeys(keys,keys)          
>>> new_dict
{'masala': {'masala': 'spicy', 'ginger': 'zesty'}, 'ginger': {'masala': 'spicy', 'ginger': 'zesty'}}
>>> del new_dict
>>>   
PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new\concepts>python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('chai.py')
>>> f.readline()
'from hello import greet\n'
>>> f.readline()
'\n'
>>> f.readline()
'greet("chai") \n'
>>> f.readline()
'\n'
>>> f.__next__()
'greet("hai")'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> for i in open('chai.py'):           
...     print(i)
...
from hello import greet



greet("chai")



greet("hai")
>>> mylist = [1,2,3,4]
>>> iter(mylist)
<list_iterator object at 0x0000027DE91678B0>
>>>         