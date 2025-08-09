#Number Calculator =

n = int(input("enter the value of n: "))

# def Number_expansion_calculator(n):
#     print("result: ",n+(n*n)+(n*n*n)+(n*n*n*n)+(n*n*n*n*n))
    
# Number_expansion_calculator(n)

a = int("%s"%n)
b = int("%s%s"%(n,n))
c = int("%s%s%s"%(n,n,n))

print(a+b+c)