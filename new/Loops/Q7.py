# Validate Input -

def VaidateInput():
    while(True):
        n = int(input("Enter the input : "))
        if (n>0 and n<11):
            print(f"{n} match")
            break
        else:
            print("Invalid number, Try again !!")
print(VaidateInput())        