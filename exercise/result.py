num_of_students = int(input("Enter number of students: "))
increment = 1

students_marks = []

while increment <= num_of_students:
    print(f"======Student {increment} ========")
    for mark in range(1):
        nep = int(input("Enter nep: "))
        eng = int(input("Enter eng: "))
        mat = int(input("Enter mat: "))
        sic = int(input("Enter sic: "))
        pop = int(input("Enter pop: "))
        msk = [nep, eng, mat, sic, pop]
        students_marks.append(msk)
    increment += 1

total_marks = []

for subject_mark in students_marks:
    sn_s_m = 0
    for sub_mark in subject_mark:
        sn_s_m += sub_mark

    total_marks.append(sn_s_m)

for tot in total_marks:
    percentage = tot / 5

    if percentage > 35 and percentage <= 45:
        print("third")

    elif percentage > 45 and percentage <= 60:
        print("second")
    elif percentage > 60 and percentage <= 75:
        print("first")

    elif percentage > 75 and percentage <= 100:
        print("top")

    else:
        print("study pugena")
