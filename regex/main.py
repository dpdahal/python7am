# what is regex?
# regex is a sequence of characters that define a search pattern.
# It is mainly used for string searching and manipulation.

# data ="h8i 10"
# print(data[1])

import re 

name ='ram'
patterns ='^[a-zA-Z]*$'
if re.match(patterns,name):
    print('valid')
else:
    print('invalid')


# class User:
#     phone = 9876987

#     def info(self):
#         return f"I am info method"
    

# obj = User()
# print(obj.phone)
# print(obj.info())
