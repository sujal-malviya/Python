#Fruit Ripeness Checker
fruit = str(input("Give me the fruit : "))

if (fruit == "banana"):
    color = str(input("Give me the color of fruit : "))
    if (color == "Green"):
        print("Unripe")
    elif(color == "Yellow"):
        print("Ripe")
    else:
        print("Overrripe")
else:
    exit()