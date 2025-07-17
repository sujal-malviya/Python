#First Non repeated character -

def Non_repeatchar(name):
    non_rep =""
    for i in name:
        if name.count(i)==1:
            non_rep = i
            break
    return non_rep

print(Non_repeatchar("teeter"))