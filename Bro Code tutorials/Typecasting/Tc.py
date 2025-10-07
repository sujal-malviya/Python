# TYPECASTING = it is process of converting a variable from one data type to another datatype.
# str(),int(),float(),bool()

User_name = "Sam"
User_age = 21
GPA = 3.45
isStudent = True

# TO know the types of variable we will be using type() function.

print(type(User_name))
print(type(User_age))
print(type(GPA))
print(type(isStudent))


# TypeCasting -

User_age = str(User_age)

print(User_age)# now User_age is string.

# User_age = User_age +1
# print(User_age) TypeError: can only concatenate str (not "int") to str

User_age = User_age + "1"# it concatenates the string and has given the output.

print(User_age)

# User_name = int(User_name)
# print(User_name)ValueError: invalid literal for int() with base 10: 'Sam'

User_name = bool(User_name)

print(User_name)