#encapsulation-

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        
    def fullname(self):
        return f"{self.__brand}{self.model}"
    def get_brand(self):
        return self.__brand + "!"
class Ecar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
        
e1 = Ecar("Toyota"," Safari","12v")
print(e1.fullname())
# print(e1.__brand)
print(e1.get_brand())