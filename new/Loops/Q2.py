#Sum of All even Numbers -
n = int(input("enter the range of numbers : "))

def SumOfEven(n):
    sum = 0
    for i in range(1, n):
        if (i%2 == 0):
            sum += i
    return sum
print("sum of even Number : ",SumOfEven(n))