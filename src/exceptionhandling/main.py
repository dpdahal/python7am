# what is exception handling?
# Exception handling is a process of handling the error and exception in a program.
# It is used to handle the runtime errors so that normal flow of the program can be maintained.

# try:
#     print(10/0)
# except Exception as e:
#     print("Error: ", e)

# print("we are learning exception handling")



def add(x,y):
    if y==0:
        raise Exception("y ko value 0 nai rakhna")
    return x+y


try:
    print(add(10,0))
except Exception as e:
    print("Error: ", e)
finally:
    print("finally block")



print("we are learning exception handling")