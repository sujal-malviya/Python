# FORMAT SPECIFIERS -
# {value :  flags} format a value based on  what flags are intrested.

price1 = 12.3213 
price2 = -23.1212
price3 = 12.31

print(f"Price1 = ${price1:.2f}")# round off or giving only .2 decimals
print(f"Price2 = ${price2:.2f}")
print(f"Price3 = ${price3:.2f}")

print()

print(f"Price1 = ${price1:010}")
print(f"Price2 = ${price2:010}")
print(f"Price3 = ${price3:010}")

print()

print(f"Price1 = ${price1:<10}")
print(f"Price2 = ${price2:<10}")
print(f"Price3 = ${price3:<10}")

print()

print(f"Price1 = ${price1:>10}")
print(f"Price2 = ${price2:>10}")
print(f"Price3 = ${price3:>10}")

print()

print(f"Price1 = ${price1:+}")
print(f"Price2 = ${price2:+}")
print(f"Price3 = ${price3:+}")

print()

print(f"Price1 = ${price1:^,.2f}")
print(f"Price2 = ${price2:^,.2f}")
print(f"Price3 = ${price3:^,.2f}")

print()

print(f"Price1 = ${price1:10}")
print(f"Price2 = ${price2:10}")
print(f"Price3 = ${price3:10}")

print()

print(f"Price1 = ${price1:^10}")
print(f"Price2 = ${price2:^10}")
print(f"Price3 = ${price3:^10}")

print()

print(f"Price1 = ${price1:+,.2f}")
print(f"Price2 = ${price2:+,.2f}")
print(f"Price3 = ${price3:+,.2f}")

