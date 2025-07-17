#Password Strength Checker -
#pehla dimaag
# char_size = int(input("enter the password size :"))

# if(char_size <6):
#     strength = "Weak"
# elif(char_size<=10):
#     strength = "medium"
# else:
#     strength = "strong"
    
# print("What's the strength :",strength)


#second dimaag -
password = str(input("enter the password : "))

length = len(password)

if(length<6):
    strength1 ="weak"
elif(length<=10):
    strength1 = "medium"
else:
    strength1 = "strong"

print("What's the status :",strength1)