#Decorator - 

def debug(func):
    def wrapper(*args,**kwargs): 
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_vlaues = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_values} and kwargs {kwargs_vlaues}")
        result = func(*args,**kwargs)
        return result
    return wrapper
@debug
def hello():
    print("hello")
     
@debug    
def greet(name,greeting="Hi"):
    print(f"{greeting} , {name}")
    
greet("sujal",greeting="Ha Bhai")

hello()
greet("heelo")

#formated string me None nhi ataa hai.