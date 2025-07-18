#function with *args(arguments) -
def SumAll(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(SumAll(1,2))
print(SumAll(1,2,3,3))