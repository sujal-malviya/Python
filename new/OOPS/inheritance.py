# Inheritance - 
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def fullname(self):
        return f"{self.brand}{self.model}"
class Ecar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
        
e1 = Ecar("Toyota","Safari","12v")
print(e1.fullname())
