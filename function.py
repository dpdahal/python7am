"""
Types of function in python:
1. inbuilt function : print(), len()
2. user define function

"""


# # define function
# def message():
#     # function body part
#     print("Welcome ")
#
#
# # calling function
# message()


# def add():
#     x = 10
#     y = 20
#     print(x + y)
#
#
# add()


# def add(x, y):
#     print(x + y)
#
#
# add(10, 20)

# def user(name='abc', age=0):
#     print(name)
#     print(age)
#
#
# user('ram', 20)

# function return value: not a variable
# def add(x, y):
#     tot = x + y
#     sub = x - y
#     return [tot, sub]
#
#
# res = add(20, 20)
# print(res[0])
# print(res[1])


# def test():
#     print("test function")
#
#
# def demo():
#     test()
#
#
# demo()


# def take_value():
#     pass
#
#
# def calculate():
#     pass
#
#
# def display():
#     pass

# function scope : local, global

# def test():
#     x = 10
#     print(x)
#
#
# test()


# x = 10
#
#
# def test():
#     global x
#     x = x + 10
#     print(x)
#
#
# test()

# args: *
# krgs: **

# def numbers(*data, **d1):
#     print(data)
#     print(d1)
#
#
# numbers(1, 2, 3, 4, 5, name='ram', age=30)
#
# def test():
#     """
#     """
#
#
#
# print()

# print(print.__doc__)

# def connection():
#     """
#     this is database connection method
#     :return:
#     """
#     return "database was connected"
#
#
# # print(dir(connection))
# print(connection.__name__)
# print(connection())


# add = lambda x, y: x + y
#
# def myrep(data, times):
#     pass
#
#
# myrep('ram',50)

#
# def dell():
#     pass
#
# def mac():
#     pass
#
# def toshiba():
#     pass
#


# def user():
#     def name(new_name):
#         return f"My name is {new_name}"
#
#     return name
#
#
# obj = user()
# print(obj('sophia'))


#  function recrusion

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# print(factorial(5))


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter any number"))
print(factorial(num))
