#Coffee Customization

coffee_size = str(input("Giv'me the order : "))
extra_shot = False

if extra_shot:
    coffee = coffee_size + " coffee with extra shot"
else:
    coffee = coffee_size + " coffee"

print(coffee)