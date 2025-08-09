# first and last character of list -

mylist = ["red","green","white","black"]

# def First_last(mylist):
#     for i in range(len(mylist)):
#         if(i==0 or i==len(mylist)-1):
#             print(mylist[i],end=" ")
            
# First_last(mylist)

i = 0
n =len(mylist)
while i<n:
    if i==0 or i==n-1:
        print(mylist[i],end=" ")
    i = i+1

