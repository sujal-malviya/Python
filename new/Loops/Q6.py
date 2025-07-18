#factorial Calculator -
#Fatorial using For loop -
# def Factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(Factorial(6))

#Factorial using while loop -
n = int(input())
def Factorial(n):
    fact = 1
    i = 1
    while(i<=n):
        fact *= i
        i = i+1
    return fact
print(f"Factotial of {n} : ",Factorial(n))

#Formulla =>  n! = (n-1)! - (n-2)! --------(n-n)!