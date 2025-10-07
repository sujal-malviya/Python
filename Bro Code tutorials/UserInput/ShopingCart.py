item = input("What item do you want ?: ")
price = float(input("What is the price ?: $"))
quantity = int(input("How many ?: "))

print()
total =  quantity*price

print(f"I want a {item}.")
print(f"Prize of a {item} : ${price}")
print(f"I want {quantity} {item}/s")
print(f"Total is ${total}")