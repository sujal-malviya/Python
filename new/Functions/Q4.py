# funtion return Multiple Values -
import math
def Math(radius):
    area = math.pi*radius*radius
    circumference = 2 * math.pi* radius
    return area, circumference

a ,c = Math(2)
print("Area : ",round(a,3))
print("Circumference : ",round(c,3))