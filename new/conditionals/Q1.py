#Age group Classification
age = int(input("provide me age : "))

if (age<13):
    print("Child")
elif (age>=13 and  age<20):
    print("teenager")
elif (age>=20 and age<=59):
    print("adult")
else :
    print("senior")