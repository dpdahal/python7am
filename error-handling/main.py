# try:
#     x
#
# except Exception as e:
#     print(e)
#
# finally:
#     print("done")

def add(x, y):
    if y == 0:
        raise Exception("Y is zero")

    return x + y


try:
    print(add(10, 0))

except Exception as e:
    print(e)
