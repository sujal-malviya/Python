# import sujal 
# import List 
# sujal -> class that  we have imported.
# list = [1,"sujal",False]
# x = "sujal"
# # print(typeof(x))
# list = [1,2,3,4] # mutable
# # newlist = []
# # for i in list:
# #     newlist.append(i)
# #Json
# res = [x for x in list  if x%2==0]
# print(res)
# tuple = (1,2,3,4) # immutable
# print(list[start:end:steps])
# # 0 -> 1 end->4 = 4-1 (0 -3)
# # -1 -> 4,3,2,1 
# # [::-1]->reverse
# # .split
# #for integer split doesn't works. 
# y = "sujal"
# x = list(y)

# # print(x.split("j"))
# #split - read krke split krega
# print(x)
# list = ["sujal"]
# print(list)
#                                                     OOPS - Object Oriented  Prograaming 
#
class animal: #parent
    def __init__(self,name,color): #self connection 
        self.name = name  
        
    def sound(self):
        print("bark")
class dog(animal):#child 
    def name(self):
        print("labrador")
class cat(dog):
    def isitanimal(self):
        print("ya! it's animal")

class cheetah(dog,cat):
    
d = dog()#object
print(d.sound())
#sinlge level inheritance
#inhertitace - 
# 1)siingle
#2) multi level 
#3)multiple 
# dog  <----- >  cat ----> cheetah
##############################################                       abstraction .
#decorator - special function 
# def hello():
#     print("hello")
#     def hi():
#         print("Hi")
# # *args(non-keyword arguments ) ,**kwargs(keywords) key value pair 
# # * iterable args for i in fruits :  [x = args for x in fruits: ]    
# @hello#decorator 
# def greet ():
#     print("heelo")
    
      
# class alpabhet:
#     def letters(self):
#         print("how many letters ??")
# class numbers(alpabhet):
    
#     def letters(self):
#         print(" Ab C D----")
fruits = ["apple","banana","mango"]
def unknnown(*args,fruits):
    print(args)

####                                                              database integration in fastapi.
#Fast API -----------------------------------------------------------------------------------------------------------------------------------------------------------