# x=60
# y=69

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("y is greater than x")

# WAP to enter any number and check whether
#  it is even or odd

# num =5
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# num =int(input("Enter a number: "))
# print(type(num))

# num =input("Enter a number: ")
# num =int(num)
# print(type(num))


# x=80
# y=90
# z=10

# if x>y and x>z:
#     print("x is greater")
# elif y>x and y>z:
#     print("y is greater")
# else:
#     print("z is greater")

# WAP to enter any number and check whether
#  it is divisible by 3 and 5 or not

# WAP to enter age and check whether the person
#  is eligible to vote or not 18> <40

# WAP to enter five subject marks and calculate total,percentage and grade

# nep =int(input("Enter marks of Nepali: "))
# eng =int(input("Enter marks of English: "))
# math =int(input("Enter marks of Math: "))
# sci =int(input("Enter marks of Science: "))
# soc =int(input("Enter marks of Social: "))
# total =nep+eng+math+sci+soc
# per = total/5
# print("Total: ",total)
# print("Percentage: ",per)
# if per>34 and per<45:
#     print("Grade C")
# elif per>44 and per<60:
#     print("Grade B")
# elif per>59 and per<75:
#     print("Grade A")
# elif per>74 and per<100:
#     print("Grade A+")
# else:
#     print("Fail")


# neted if else

# a=8
# b=7
# c=9

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")


# print("1. Add 2.Sub  3.Mul  4.Div")
# option = int(input("Enter your choice: "))
# if option==1:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Sum: ",a+b)
# elif option==2:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Sub: ",a-b)
# elif option==3:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Mul: ",a*b)
# elif option==4:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Div: ",a/b)
# else:
#     print("Invalid choice")


# age = int(input("Enter your age: "))
# if age<18:
#     print("not allowed to the party because you are under age")
# elif age>18 and age<40:
#     print("Welcome to the party")
#     if age>18 and age<25:
#         print("you can drink coke")
#     elif age>25 and age<40:
#         print("you can drink beer")
#     else:
#         print("you can drink whisky")
# else:
#     print("not allowed to the party because you are over age")

# amount=10000
# pin > option withdraw,check balance

# match


language ='chinese'

match language:
    case 'nepali':
        print("Namaste")
    case 'english':
        print("Hello")
    case _:
        print("Invalid language")