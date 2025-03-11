# what is oop?
# oop object oriented programming is a programming paradigm based on the
#  concept of objects and their interactions.
# it is a way to model real-world entities and
#  their relationships using classes and objects.

# class is a blueprint for creating objects
# what is objet?
# object is an instance of a class
# object is a real-world entity that has attributes and behaviors

# x=10 # variable

# def test():
#     print("hello world")

# test()

# class Car:
#     model = "Toyota"

#     def info(self):
#         print("This is a car")

# obj = Car()
# print(obj.model)
# obj.info()

# class Calculator:
#     a =100
#     def add(self,x,y):
#         print(x+y)

#     def info(z):
#         print(z.a)


# cal = Calculator()
# cal.add(10,20)

# class Laptop:
#     def info(self):
#         print("1. Dell(Rs:20000) 2. Toshiba(Rs:30000) 3. Mac(Rs:50000)")

#     def dell(self):
#         print("Dell")

#     def toshiba(self):
#         print("Toshiba")


# obj = Laptop()
# print(dir(obj))
# # obj.info()

# option = int(input("Enter your choice: "))
# if option == 1:
#     obj.dell()

# elif option == 2:
#     obj.toshiba()



# data=['ram','shyam','hari','sita','gita']
# print(type(data))
# data.append('nita')

# class Car:
#     price = 100

#     def getPrice(self):
#         # obj = Car()
#         # obj -> instance
#         print(self.price)

# obj = Car()
# obj.getPrice()

# what is self?
# self is a reference to the current instance of the class

# dunder methods -> special methods -> magic methods

# class Car:
#     def __new__(cls):
#         print("This is a new method")
#         return object.__new__(cls)

#     def __init__(self):
#         print("This is a constructor")
    
#     def info(self):
#         print("This is a car")

#     def __del__(self):
#         print("This is a destructor")

# obj = Car()
# obj.info()

# class Car:
#     def __init__(self,name,price):
#         print(name)
#         print(price)

# obj = Car('Toyota',1000)

# class  Mobile:
#     price = 1000
#     brand = "Samsung"

#     def __str__(self):
#         return self.brand


# obj = Mobile()
# print(obj)
# inheritance

# class Laptop:
#     def brand(self,name):
#         print(name)

# class Dell(Laptop):
#     pass

# obj = Dell()
# obj.brand('Dell')

# class Toshiba(Laptop):
#    pass


# class Laptop:
#     def __init__(self,name,price):
#         print(name)
#         print(price)

# class Dell(Laptop):
#     def __init__(self,name,price,brand):
#         # Laptop.__init__(self,name,price)
#         super().__init__(name,price)
#         print(brand)


# obj = Dell('Dell',20000,'abc')

# what scope of variable
# public -> accessible from anywhere
# protected -> accessible within the class and subclass
# private -> accessible only within the class

# class Car:
#     __x=10

#     def getX(self):
#         print(self.__x)

#     def setX(self,a):
#         self.__x = a

# obj = Car()
# print(obj.__x)
# obj.setX(100)
# obj.getX()


# class Car:
#     __x=10

#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self,a):
#         self.__x = a


# obj = Car()
# obj.x=4000
# print(obj.x)
# encapsulation
# static method
# class method
# instance method


# class Laptop:
#     x=10

#     @property
#     def brand(self):
#         return "Dell"



# obj = Laptop()
# print(obj.x)
# print(obj.brand)


# class Laptop:
#     x=10
#     def __init__(self,name):
#         print(name)

#     @staticmethod
#     def brand():
#         obj = Laptop()
#         print(obj.x)

# Laptop('Dell').brand()


# class Students:
#     total =0
#     def __init__(self,name):
#         Students.total+=1


# obj1 = Students('Ram')
# obj2 = Students('Shyam')
# obj3 = Students('Hari')
# print(obj1.total)


# class Students:
#     x=10
#     @classmethod
#     def test(cls):
#         print(f"Value of x is {cls.x}")


# name ='ram'
# # print(type(name))
# print(dir(name))
   

# class MyClass:
#     price = 1000
#     def intUpper(self,name):
#         print(name.upper())


# obj = MyClass()
# print(dir(obj))


# class Demo:
#     pass


# obj = Demo()
# obj.name = 'Ram'
# obj.address = 'Kathmandu'

# print(obj.name)
# print(obj.address)

# sqlite3
# mysql