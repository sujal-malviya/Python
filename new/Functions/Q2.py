#Function with Multiple parameters -
n,m = map(int,input("enter 2 Numbers: ").split())
def SumOfNumbers(n,m):
    sum = n + m
    return sum
print(f"Sum of {n} + {m} is :",SumOfNumbers(n,m))