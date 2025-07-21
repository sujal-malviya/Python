# Multiple Inheritance -
class Battery:
    def battery_info(self):
        return "This is Battery"
class Engine:
    def EngineInfo(self):
        return "This is Engine"
class Ecar(Battery,Engine):
    pass
my_newCar = Ecar()
print(my_newCar.battery_info())
print(my_newCar.EngineInfo())    