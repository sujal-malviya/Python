# Compound Intrest Calculator -


principle = 0
rate = 0
time = 0


while True:
    principle = float(input("enter the priciple : "))
    if principle <0:
        print("priciple can't be zero or equal to zero")
    else:
        break
        
while True:
    rate = float(input("Enter the rate : "))
    if rate <0:
        print("rate can't be zero or equal to zero")
    else:
        break
    
while True:
    time =  float(input("Enter the time: "))
    if time <0:
        print("time can't be zero or equal to zero")      
    else:
        break

print(principle)
print(rate)
print(time)        
total = principle * pow((1+rate/100),time)
print(f"Total is ${total}")