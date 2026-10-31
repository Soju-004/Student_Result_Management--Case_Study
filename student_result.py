from result_system import student_summary, check_result, print_report, update_marks, add_student, remove_student, class_statistics

students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}


print("Task 1: One student")
print(student_summary(students["S101"]))
print(check_result(students["S102"]["marks"]))
print(check_result(students["S102"]["marks"], pass_mark=35))
print(check_result(students["S102"]["marks"], 35))

print("\nTask 2: Report")
print_report(students)


print("\nTask 3: Update marks")
print(update_marks(students, "S102", Maths=55))
print(update_marks(students, "S999", Maths=50))

corrections = {"Python": 50, "Stats": 58}
print(update_marks(students, "S102", **corrections))
print(student_summary(students["S102"]))

print("\nTask 4: Add student")
print(add_student(
        students,
        "S106",
        "Farhan",
        Python=70,
        Maths=35,
        Stats=74
    ))
print(add_student(
        students,
        "S101",
        "Zara",
        Python=80,
        Maths=80,
        Stats=80
    ))
print(students["S106"])


print("\nTask 5: Remove student")
print(remove_student(students, "S104"))
print(remove_student(students, "S104"))
print(len(students))


print("\nTask 6: Final report and statistics")
print_report(students)

stats = class_statistics(students)
print("Topper:", stats["topper"])
print("Pass percentage:", stats["pass_percentage"])
print("Subject averages:", stats["subject_averages"])

selected_stats = class_statistics(students, "Python", "Stats")
print("Python and Stats only:", selected_stats["subject_averages"])
