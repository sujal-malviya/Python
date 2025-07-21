# Static method -
 #decorators are the ones who enhance the functionality of method for ex @static method is one of the decorator.

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    @staticmethod
    def general_description():
        return "Car is missing"
    
    @property
    def model(self):
        return self.__model
    
    def fullname(self):
        return f"{self.__brand}{self.__model}"


class Ecar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
        
mycar = Car("Tata","safari")
# mycar.model = "city"
print(mycar.model)
e1 = Ecar("Toyota","Safari","12v")
print(e1.fullname())
# @property  use kr rhe ho to uska matlab ki aap usko property ki tarah treat kre na ki method or yadi aapko access krna hai to app meri method ke through access kre .
# isinstance is used to prove that the object of derived class refers to both class or not.
print(isinstance(e1,Car))
print(isinstance(e1,Ecar))