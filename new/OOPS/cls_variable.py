# Class Variable
 
class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    def fullname(self):
        return f"{self.brand}{self.model}"
class Ecar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize

# safai = Car("Toyota","safari")     
e1 = Ecar("Toyota","Safari","12v")
print(Car.total_car)
# print(e1.fullname())
#Immediate garbage collection nhi hota python me .