# list = [1,2,3,4]
# tuple = (1,2,3,4)

# mylist = [1,2,3,4]

#GIL =  (Global Interpreter Lock)-
#Module and packages
#try and catch
#List and Dictionary comprehension
#generator
#decorator
#Reverse Loop
#slicing (reverse)
# name ="sujal"  
# print(name[:])
# print(name[0:3])
# print(name[-1:])
# print(name[:])
# #String Pallindrome -
# name1 = "naman"
# if (name1 == name1[::-1]):
#     print("string pallindrome")
# else:
#     print ("not")
#copy and deep copy
#animal class private attribute name , method make sound .
#2 subclass dog ,cat animal -> inherit , both the class will override make sound

#Full (python,Backend,OOpS)-
class Animal:
    def __init__(self,__name):
        self.name = __name
    def makesound():
        print("Roar")
class Dog(Animal):
    def makesound():
        print("Bark")
class Cat(Animal):
    def makesound():
        print("Meow")

c1 = Cat("Dog")
c1.makesound()

# Base class
class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def make_sound(self):
        print("Some generic animal sound")

# # Subclass Dog
# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.get_name()} says: Woof!")

# # Subclass Cat
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.get_name()} says: Meow!")

# # Testing
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# dog.make_sound()  # Output: Buddy says: Woof!
# cat.make_sound()  # Output: Whiskers says: Meow!
