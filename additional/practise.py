mylist = ["GeekforGeeks", "FreeCodeCamp", "stackOverFlow", "MyCodeSchool"]

# Function to find the longest name(s)
def longest_name(mylist):
    if not mylist:  
        return []
    
    longest = []          
    max_length = 0         
    for name in mylist:
        if len(name) > max_length:
            max_length = len(name)   
            longest = [name]         
        elif len(name) == max_length:
            longest.append(name)     
    
    return longest


result = longest_name(mylist)

print("Longest name(s):", result)
