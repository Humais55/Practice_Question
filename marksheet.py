def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'A-'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    else:
        return 'F'

def marksheet(name, roll, marks):
    total = sum(marks)
    average = total/len(marks)
    overall_grade = grade(average)

    print("---------Marksheet---------")
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print("Subject Marks:\n")
    for i, subject in enumerate(subjects):
        subject_mark = marks[i]
        print(f"{subject}: {subject_mark}")
    print(f"\nTotal Marks: {total}")
    print(f"\nAverage Marks: {average:.2f}")
    print(f"\nGrade: {overall_grade}")
    print("-------------------------------")


name = input("Enter your damn Name: ")
roll_num = int(input("Enter your roll no: "))

marks = []
subjects = ["Math", "Eng", "Urdu", "Sci", "Comp"]

print("\n")
for subject in subjects:
    x= float(input(f"Enter marks for {subject}: "))
    marks.append(x)


marksheet(name, roll_num, marks)