# Decorator - 
import time

def timer(funx):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = funx(*args,**kwargs)
        end = time.time()
        print(f"{funx.__name__} ran in {end-start} time")
        return result
    return wrapper
@timer
def example_funx(n):
    time.sleep(n)
    
example_funx(2)