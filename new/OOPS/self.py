class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Toyota","hilux")
print(my_car.brand)
print(my_car.model)

my_newcar = Car("Tata","Safari")
result = my_newcar.full_name()
print(result)
