# Logical operator =  evaluate multiple conditions (or,and ,not)
# or = at least one condition must be true
# and = both the conditions must be true
#  not inverts the condtion (NOT false,not true)

# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("Event is cancelled")
# else:
#     print("Event is not cancelled")

temp = int(input("Enter the temprature: "))

is_sunny = True

if (temp>=28 and is_sunny):
    print("It is Hot outside ")
    print("It is Sunny")
elif(temp<0 and is_sunny):
    print("It is cold outside")
    print("It is sunny")
elif(28>temp>0 and  is_sunny ):
    print("It is Warm Outside")
    print("It is Sunny")
elif(temp>=28 and not is_sunny):
    print("It is Hot Outside")
    print("It is Cloudy ")
elif(temp<0 and not is_sunny):
    print("It is Cold Outside")
    print("It is Cloudy")
elif(28>temp>0 and not is_sunny):
    print("It is Warm Outside.")
    print("It is cloudy ")
