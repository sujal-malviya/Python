# def Prime_Number(n):
#     if n <= 1:
#         return f"{n} is not prime"
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return f"{n} is not prime"
#     return f"{n} is prime"

# print(Prime_Number(-1))  # Output: 1 is not prime

def Isprime(n):
    prime = True
    if n>1:
        for i in range(2,n):
            if(n%i )== 0:
                prime = False
                break
            return prime
print(Isprime(7))