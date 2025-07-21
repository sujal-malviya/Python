## even Generator -

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    
#value ko return nhi krna or us value ko generate krna usee ham yeild bolte hai
for num in even_generator(10):
    print(num)
#ek baar yeild kra to hame memory me ye bhi yad rakhna hai kya generate kra hai.