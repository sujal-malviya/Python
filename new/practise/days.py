# days between dates

date1 = (2014,7,2)
date2 = (2014,7,11)

for i in range(len(date1)):
    for j in range(len(date2)):
        if i==len(date1)-1 and j==len(date2)-1:
            print(date2[j]-date1[i],end=" ")
            
# next method -

from datetime import date

f_date = date(2014,7,2)

l_date = date(2014,7,11)
 
delta = l_date - f_date

print(delta.days)