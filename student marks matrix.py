marks = []

for i in range(3):
    student_marks = []

    print("Enter marks for Student", i + 1)

    for j in range(3):
        mark = float(input("Enter subject marks: "))

        if mark < 0 or mark > 100:
            print("Invalid marks")
            quit()

        student_marks.append(mark)

    marks.append(student_marks)

print("\nStudent Marks Analysis")

for i in range(3):
    total = sum(marks[i])
    average = total / 3

    print("Student", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
