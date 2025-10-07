import math 

print("----------------Circumference of Circle---------------------")
radius = float(input("Enter the radii : "))
Circumference = 2*math.pi*radius

print(f"Circumference of Circle => {round(Circumference,2)}cm²")


print("--------------------Area of Circle---------------")


area = math.pi*pow(radius,2)

print(f"Area of Circle => {round(area,2)}cm²")


print("-------------------Hypoteneous of right triangle----------------------")
a = 3
b =4
c = math.sqrt(math.pow(a,2)+math.pow(b,2))

print(f"The hypotaneous of right triangle is {round(c,2)}cm²")