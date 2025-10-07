# Few Functions 

name = "Sam Johnson"

# To find length of name - len() function
result = len(name)
print(f"length of name : {result}")

# To Capitalise a string - capitalize() function

result = name.capitalize()
print(f"Capitalize version : {result}")

# To covert whole string into UpperCase - upper() function

result = name.upper()
print(f"UpperCase Name: {result}")

# To convert whole string to lowecase - lower() function.

result = name.lower()
print(f"Lower case name: {result}") 

# To check if there is digit in string or not - isdigit() function.

result = name.isdigit()
print(f"Digit Present or not (True/False): {result}")

# to check the string is contains all aphabets or not - isalpha() function.
#  if space is there then also it will give False.

result = name.isalpha()
print(f"Alphabet present => (true/false) : {result}")

# to find the character's index from the string - find() function.
# if character is present more then 1 time in string so it will give last character's index.

result = name.find("s")
print(f"Index : {result}")

# to find the last index of string - rfind() function.

result = name.rfind("m")
print(f"Index : {result}")


#if we have to count any character in a string so we will use count() function.
# It is only applicable in String.
phone = input("enter a phone number: ")

result = phone.count("-")
print(f"Count(-) in phone Number {result}")

phone = phone.replace("-"," ")
print(phone)

