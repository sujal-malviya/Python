#Counting Positive Number - 
mylist = list(map(int,input().split()))
def count_positive(mylist):
    count = 0
    for i in mylist:
        if(i>0):
            count += 1
        else:
            continue
    return count

print(count_positive(mylist))