# what is function?
# function is a block of code that performs a specific task and returns a value.
#  function only runs when it is called.
# tyes of function:
# 1. Built-in function: print(), input(), len(), range(), etc.
# 2. User-defined function: we can create our own function.


# def message():
#     print("we are learning python function")

# message() 
# message()

# function with parameter

# def message(name):
#     print("Hello",name)

# message('ram')
# message('shyam')


# def add(x,y):
#     print(x+y)

# add(10,20)
# add(30,40)
# add(50,60)

# optional parameter

# def users(name,age=0,address=''):
#     print("Name:",name)
#     print("Age:",age)

# users('ram',30)


# def total(*numbers):
#     print(numbers)

# total(10,20,30,40,50)


# function retur value


# def add(x,y):
#     return x+y


# print(add(10,20))


# def add(x,y):
#     return x+y


# def total():
#     print(add(10,20))

# total()


# def add(x,y):
#     return x+y


# def total(a,b,callback):
#     print(callback(a,b))

# total(6,7,add)

# total = lambda x,y:x+y
# print(total(10,20))

# global variable
# local variable

# def test():
#     x=10
#     print(x)
   

# test()

# a =7


# def test():
#     global a
#     a= a+700
#     print(a)

# test()
# print(a)

# module


def take_value():
    p = int(input("Enter the principal amount:"))
    t = int(input("Enter the time period:"))
    r = int(input("Enter the rate of interest:"))
    return [p,t,r]

def calculate():
    p,t,r = take_value()
    return p*t*r/100


def display():
    print("The simple interest is:",calculate())

display()