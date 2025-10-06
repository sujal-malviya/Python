# Variables = A container for value (String,Integer,Float,Boolean)
# variable behaves as if it was the value it contains.


#String

Name = "sujal"
Fav_food = "pizza!"
Car = "Mustang!"

print(f"Your Name : {Name}")
print(f"Your Favourite food : {Fav_food}")
print(f"Your Favourite Car : {Car}")

print()
#Integer -

age = 25
quantity = 3
num_of_students = 30

print(f"Your age is {age} years old.")
print(f"there is {quantity} items.")
print(f"Your class has {num_of_students} students.")

print()
#float

height = 5.9
distance = 5.5
price = 19.99

print(f"Your height is {height}ft")
print(f"You ran {distance}Km")
print(f"Apple price : ${price}")

print()

#Boolean

isStudent = True
IsOnline = True

if isStudent:
    print("Student is enrolled.")
else:
    print("Student is not enrolled")