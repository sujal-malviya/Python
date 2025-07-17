#Reverse a string -

def Reverse(name):
    rev = ""
    for i in name:
       rev = i + rev
        
    return rev

print(Reverse("sujal"))