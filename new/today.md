PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new> ls


    Directory: C:\Users\Sujal Malviya\OneDriv
    e\Desktop\Documents\GitHub\python\Python\ 
    new


Mode                 LastWriteTime     Length 
----                 -------------     ------ 
dar--l         7/10/2025   2:38 PM
-a---l         7/10/2025   2:39 PM         40
-a---l         7/10/2025   2:35 PM         67


PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new>                        python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new> print("hello")
Unable to initialize device PRN
PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\PyType "help", "copyright", "credits" or "license" for more information.
>>> print("hello")
hello
>>> import os
>>> os.getcwd()
'C:\\Users\\Sujal Malviya\\OneDrive\\Desktop\\Documents\\GitHub\\python\\Python\\new'
>>> for c in "chai":
...     print(c)
...     
c
h
a
i
>>> 
 *  History restored 

PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new> python chai.py
hello
hello
chai
hai
PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new> python shell
C:\Program Files\Python313\python.exe: can't open file 'C:\\Users\\Sujal Malviya\\OneDrive\\Desktop\\Documents\\GitHub\\python\\Python\\new\\shell': [Errno 2] No such file or directory
PS C:\Users\Sujal Malviya\OneDrive\Desktop\Documents\GitHub\python\Python\new> python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.platform
'win32'
>>> import hello
hello
hello
>>> import greet
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    import greet
ModuleNotFoundError: No module named 'greet'
>>> hello.greet
<function greet at 0x000002494CC27B00>
>>> hello.greet("mint")
mint
>>> hello.chai_one
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    hello.chai_one
AttributeError: module 'hello' has no attribute 'chai_one'
>>> import hello
>>> hello.chai_one
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    hello.chai_one
AttributeError: module 'hello' has no attribute 'chai_one'
>>> from importlib import reload
>>> hello.chai_one
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    hello.chai_one
AttributeError: module 'hello' has no attribute 'chai_one'
>>> from importlib import reload
>>> reload
<function reload at 0x000002494C9A4040>
>>> from importlib import reload
>>> reload(hello)
hello
hello
<module 'hello' from 'C:\\Users\\Sujal Malviya\\OneDrive\\Desktop\\Documents\\GitHub\\python\\Python\\new\\hello.py'>
>>> hello.chai_one
'lemon tea'
>>> hello.chai_two
'ginger tea'
>>> hello.chai_three
'masala chai'
>>> username = "sujal"
>>> username
'sujal'
>>> username = "malviya"
>>> username
'malviya'
>>>  mylist = [1,2,3]
  File "<python-input-22>", line 1
    mylist = [1,2,3]
IndentationError: unexpected indent
>>> mylist[1,2,3]
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    mylist[1,2,3]
    ^^^^^^
NameError: name 'mylist' is not defined. Did you mean: 'list'?
>>> lsit
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    lsit
NameError: name 'lsit' is not defined
>>> list
<class 'list'>
>>> mylist = [1,2,3]
>>> 
>>> mylist
[1, 2, 3]
>>> 
KeyboardInterrupt
>>> num= 10
>>> num
10
>>> num = 3.14
>>> num
3.14
>>> int  = 10
>>> int
10
>>> name = 'wong;
  File "<python-input-35>", line 1
    name = 'wong;
           ^
SyntaxError: unterminated string literal (detected at line 1)        
>>> name = 'wong'
>>> name
'wong'
>>> list
<class 'list'>
>>> mylist = [1,"hello",2.22]
>>> mylist
[1, 'hello', 2.22]
>>> mylist[0]
1
>>> mylist[1]
'hello'
>>> name[0]
'w'
>>> name[-1]
'g'
>>> mylist[-1]
2.22
>>> dict
<class 'dict'>
>>> mydict = {'name' : 'sujal' ,'city' : 'banglore'}
>>> mydict
{'name': 'sujal', 'city': 'banglore'}
>>> mydict[0]
Traceback (most recent call last):
  File "<python-input-49>", line 1, in <module>
    mydict[0]
    ~~~~~~^^^
KeyError: 0
>>> mydict['name']
'sujal'
>>> mydict['city']
'banglore'
>>> tuple
<class 'tuple'>
>>> mytup = (1,2,3)
>>> mytup
(1, 2, 3)
>>> mytup[0]
1
>>> mytup[-1]
3
>>> len(mytup)
3
>>> name[1:3]
'on'
>>> name[0:4]
'wong'
>>> import sys
>>> sys.getrefcount(22)
4294967295
>>> sys.refcount('sujal')
Traceback (most recent call last):
  File "<python-input-63>", line 1, in <module>
    sys.refcount('sujal')
    ^^^^^^^^^^^^
AttributeError: module 'sys' has no attribute 'refcount'. Did you mean: 'getrefcount'?
>>> sys.getrefcount('sujal')

