pet = str(input("Which Pet ?\n"))

pet_age = int(input("Enter the Pet age : "))

if (pet == "Dog"):
    if(pet_age<2):
        print(pet,"-Puppy food")
    else:
        print(pet,"-senior food")
elif(pet == "cat"):
    if(pet_age>5):
     print(pet,"-Senior cat food")
    else:
        print(pet,"-small kitty food")
    