# sets
# unordered collection of multiple items
# mutable 
# unindexed 
# No duplicates

set1 = {1,2,3,4}
print(set1)

set1 = set()
print(set1)
set2 = set("Geeks")
print(set2)
set3 = set(["Geeks","for","Geeks"])
print(set3)
mylist = [1,2,3,1,1,4,5]
print(set(mylist))
set3.add(4)
print(set3)
set3.update("Geeks","Hello")
print(set3)
print()
for i in set3:
    print(i,end=" ")
print()
# for removing u can use
# pop()
# discard
# clear()
print(set3.remove("Geeks"))
