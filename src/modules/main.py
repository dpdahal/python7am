# import calculator as cal

# print(calculator.add(1, 2))

# print(cal.add(1, 2))

# from calculator import *

# print(add(1, 2))

# import math

# print(math.pi)
# print(math.sqrt(4))

# import calendar

# print(calendar.calendar(2026))


# import datetime
# # print(datetime.datetime.now())
# today = datetime.datetime.now() 
# b_date = datetime.datetime(1998, 1, 1)
# print(today - b_date)

# new_date ="2021-01-01"
# new_date = datetime.datetime.strptime(new_date, "%Y-%m-%d")
# print(new_date)
import datetime
jobs=[
    {'title':"python developer",'exp_date':'2025-03-25'},
    {'title':"java developer",'exp_date':'2023-11-25'},
    {'title':"javascript developer",'exp_date':'2022-12-25'},
    {'title':"c# developer",'exp_date':'2026-06-25'},
]

for job in jobs:
    exp = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
    today = datetime.datetime.now()
    if exp > today:
        print(job['title'], "is active")
    else:
        print(job['title'], "is expired")