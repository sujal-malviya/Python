# TEMPRATURE Calculator - 

temp = float(input("Enter the temprature: "))
unit = input("Celcius or Farhenhiet (C/F): ")

if unit == "C":
    temp = round((temp * 9)/5 + 32,1)
    print(f"Temprature is {temp}°F")
elif(unit == "F"):
    temp = round((temp-32)*5/9,1)
    print(f"the Temprature is {temp}°C")
else:
    print(f"The {unit} is invalid unit.")