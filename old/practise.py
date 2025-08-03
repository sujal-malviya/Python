fruits = ["apple","orange","banana"]

for fruit in fruits:
    print(fruit,end=" ") 
print()   
# Countdown timer -
second = int(input("enter number of seconds : "))

while(second>0):
    print("Time Left :",second)
    second -=1
    
print()

total  =0
number = int(input("enter the number : "))

while(number !=0):
    total = total + number 
    number = int(input("Enter untill 0 comes : "))
    print("total : ",total)
print()

n = int(input())

for i in range(1,n+1):
    print(n*i,end=" ")