print("===========Students Result===============")
num =int(input("Enter the number of students: "))
students_marks=[]
x=1
while x<=num:
    print(f"==========Sid: {x}==========")
    nep = int(input("Enter the marks of Nepali: "))
    eng = int(input("Enter the marks of English: "))
    math = int(input("Enter the marks of Math: "))
    sci = int(input("Enter the marks of Science: "))
    soc = int(input("Enter the marks of Social: "))
    total = nep+eng+math+sci+soc
    students_marks.append(total)
    x+=1
for total in students_marks:
    per = total/5
    grade =''
    if per>=80:
        grade = 'A'
    elif per>=60:
        grade = 'B'
    elif per>=40:
        grade = 'C'
    else:
        grade = 'D'
    print(f"Total Marks: {total} Percentage: {per} Grade: {grade}")