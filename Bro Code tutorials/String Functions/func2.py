# Validate User Input Excercise -
# 1. Username is no more than 12 characters.
# 2. Username must not contains digits.
# 3. Username must not contains spaces.


User_name = input("What is your Name ?: ")

length = len(User_name)

Spaces = User_name.isalpha()

digits = User_name.isdigit()

if length>=12 :
    print("Username can't contain more than 12 characters.")
elif not User_name.find(" ")==-1:
    print("UserName can't contain spaces. ")
elif( not User_name.isalpha):
    print("User name Can't contain digits.")
else:
    print(f"Welcome {User_name}")