# Polymorphism -
 
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def fullname(self):
        return f"{self.brand}{self.model}"
    def fueltype(self):
        return "Petrol or Diesel"
class Ecar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
    def fueltype(self):
        return "electric Charge"   
e1 = Ecar("Toyota","Safari","12v")
safari = Car("Toyota","safari")
# print(e1.fullname())
print(safari.fueltype())
print(e1.fueltype())