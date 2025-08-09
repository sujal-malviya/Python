firstname = input()
lastname = input()
fullname = firstname+" " +lastname

print(f"Before reversing name : {fullname}")
i = len(fullname)-1
reversedname = ""
while i>=0:
    # print(fullname[i],end="")
    reversedname += fullname[i]
    i = i-1
print()
print(f"after reversing : {reversedname}")