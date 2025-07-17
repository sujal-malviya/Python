#Transportation Mode Selection
distance = int(input("Enter the Distance : "))

if(distance<3):
    activity = "walk"
elif(distance<=15):
    activity = "Bike"
else:
    activity = "car"

print("Activity : ",activity)