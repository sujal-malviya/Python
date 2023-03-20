a="1"
b="2"
print(a+b)
c="sam"
d="jackson"
print(c+d)
c = "shree ram"
print ("jay"+c)
print(c[0],end="")
print(c[1],end="")
print(c[2],end="")  
print(c[3],end="")
print(c[4],end="")
print(" the name of god:")
names="radhe,krishna"
print(names[0:5])
print(names[6:13],end="")
#multiline string-
apple = '''hi i am harry
i am from bangladesh .
do you want to be in my team ? '''
print(apple)
#you can use multiline string with the help of triple single code as well as triple double code.
#string indexing-
name = "michael"
print(name[0])#it will print the first position oo first letter of name string.
 # by the help of for loop-
for i in name:
     print(i,end="\n")
m ="jambo,i am your big fan"
print(m[0:5])
fruit ="mango"
print(len(fruit))#it will show the lenght of string.
print(fruit[1:4])#it is operation of string slicing will show letter of fruits.
print(fruit[0:4])#it will print the character of string.
print(fruit[:4])#by default python will show the index as 0.
print(fruit[:])#by default python will put thier the lenght of string.
print(fruit[0:-3])#before -3 pyhton will put len of function like = print(fruit[0:len(fruit)-3]) so it will subtract and will give the value.
nm = "harry" #strings are imuttable.
print(nm[-4:-2])
print(nm.upper())
print(nm.swapcase())
print(nm.lower())
ww = "nani!!"
print(ww.rstrip("!"))#it will remove the symbol from the string.it will remove the symbol which are at back of the string it won't remove symbol which are infront of string.
ex= "!!janu!!!"
print(ex.rstrip("!"))
aa="harry!!jamatara"
print(aa.replace("harry","johny"))
print(aa.split("!"))
print(aa.capitalize())
print(aa.count("!"))
print(aa.endswith("!"))#it repreaent the symbol coming back of string.and gives you output with respect to true and false like boolean.
qq =" he is my friend how is he now ?"
print(qq.find("is"))#it is use to find the position of that particular word or symol etc.
