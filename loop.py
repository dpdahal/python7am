"""
for
while
nested loop
"""

# users = ['ram', 'sita', 'gita', 'hari']
#
# for user in users:
#     print(user)

# users = [
#     ['ram', 'sita', 'gita', 'hari'],
#     ['gopal', 'madan', 'laxmi', 'kalpana'],
#     ['a', 'c', 'f', 'h']
#
# ]
#
#
# for user in users:
#     for name in user:
#         print(name)

# if x%2==0

# x = 1
#
# while x <= 10:
#     print(x)
#     x += 1


# num = int(input("Enter any number: "))
# x = 1
#
# total_even = 0
# total_odd = 0
# total_num = []
# while x <= num:
#     if x % 2 == 0:
#         total_even += x
#         total_num.append(x)
#         print(f"Even {x}")
#     else:
#         total_odd += x
#         print(f"Odd: {x}")
#
#     x += 1
#
# print(f"Total Even: {total_even} total Odd: {total_odd}")
#
# print(len(total_num))


num_of_students = int(input("Enter number of students: "))
x = 1

marks=[[],[]]

while x <= num_of_students:
    print(f"========Students: {x}===========")
    for a in range(1):
        nep = int(input("Enter nepali mark: "))
        eng = int(input("Enter english mark: "))
    x += 1
