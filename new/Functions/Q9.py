#Generation function with yield -

def even_generator(limit):
    list = []
    for i in range(2,limit+1,2):
        list.append(i)
        return list
print(even_generator(10))