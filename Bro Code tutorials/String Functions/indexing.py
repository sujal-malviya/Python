# Indexing - accessing elements of sequence using [] (indexing operator)
#  [start:end:step]

# STRING SLICING----------- 
credits = "1234-123-1234"

# print(credits[0])
# print(credits[0:4])

# print(credits[:4])

# print(credits[:])

# print(credits[-1:])

# print(credits[-1:0])

# print(credits[1:9:2])

# print(credits[::-1])

# print(credits[::2])

last_digit = credits[-4:]

print(f"XXXX-XXX-{last_digit}")