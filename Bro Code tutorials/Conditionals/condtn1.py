# Conditionals - if conditons means to execute block if condition is true else other statement.

age = int(input("Enter Your age : "))

if(age>=18 and age<40):
    print("You are Adult!")
elif(age<0):
    print("You are NOT Born")
elif(age>40 and age<70):
    print("You comes under old ones.")
else:
    print("You are Child under 18")