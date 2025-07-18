#Uniqueness element chaecker -
# mylist = input("Enter items separated by space: ")
# user_list = mylist.split()

# def Uniqueness_checker(userlist):
#     for i in userlist:
#         if userlist.count(i) > 1:
#             return f"Not Unique: Duplicate item found -> {i}"
#     return "ALL ARE UNIQUE"

# print(Uniqueness_checker(user_list))

# sir ka method

mylist = ["apple","banana","orange","apple","mango"]

unique_item = set()

for i in mylist:
    if i in unique_item:
        print("Duplicate : ",i)
        break
    unique_item.add(i)