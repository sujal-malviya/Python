# PYTHON CALCULATOR -
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

operator = input("ENTER THE OPERATOR : (+,-,*,/): ")

if(operator == "+"):
    print(f"{round(a+b,2)}")
elif(operator == "-"):
    print(f"{round(a-b,2)}")
elif(operator == "*"):
    print(f"{round(a*b,2)}")
elif(operator == "/"):
    print(f"{round(a/b,2)}")
else:
    print("Invalid Operator")