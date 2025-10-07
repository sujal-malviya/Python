# WEIGHT Converter -

weigth = float(input("Enter Your Weight: "))
unit = input("Kilogram or Pounds? (K/P): ")

if unit =="K":
    weigth = weigth * 2.205
    unit = "lbs"
    print(f"weight is {round(weigth,2)}{unit}")
elif unit == "P":
    weigth = weigth/2.205
    unit = "kgs"
    print(f"weight is {round(weigth,2)}{unit}")
else:
    print("Invalid Unit.")
    
