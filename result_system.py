def calculate_total(marks):
    return sum(marks.values())

def calculate_average(marks):
    return round(calculate_total(marks) / len(marks), 2)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def check_result(marks, pass_mark=40):
    for mark in marks.values():
        if mark < pass_mark:
            return "Fail"
    return "Pass"

def student_summary(student):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)

    return {
        "name": student["name"],
        "total": total,
        "average": average,
        "grade": get_grade(average),
        "result": check_result(marks)
    }

def add_student(data, student_id, name, **marks):
    if student_id in data:
        return False

    data[student_id] = {
        "name": name,
        "marks": marks
    }
    return True

def update_marks(data, student_id, **changes):
    if student_id not in data:
        return False

    data[student_id]["marks"].update(changes)
    return True

def remove_student(data, student_id):
    if student_id not in data:
        return False

    data.pop(student_id)
    return True

def print_report(data):
    ranking = []

    for student_id, student in data.items():
        average = calculate_average(student["marks"])
        ranking.append((average, student_id))

    ranking.sort(reverse=True)

    print(f"{'ID':6}{'Name':8}{'Total':6}{'Avg':8}{'Grade':7}  Result")
    print("-" * 42)

    for average, student_id in ranking:
        student = data[student_id]
        summary = student_summary(student)

        print(
            f"{student_id:6}"
            f"{summary['name']:8}"
            f"{summary['total']:<6}"
            f"{summary['average']:<8.2f}"
            f"{summary['grade']:7}  "
            f"{summary['result']}"
        )

def class_statistics(data, *subjects):
    if not data:
        return {
            "topper": None,
            "pass_percentage": 0.0,
            "subject_averages": {}
        }

    topper = None
    highest_average = -1
    pass_count = 0

    for student in data.values():
        summary = student_summary(student)

        if summary["average"] > highest_average:
            highest_average = summary["average"]
            topper = student["name"]

        if summary["result"] == "Pass":
            pass_count += 1

    pass_percentage = round((pass_count / len(data)) * 100, 1)

    if not subjects:
        subjects = tuple(next(iter(data.values()))["marks"].keys())

    subject_averages = {}

    for subject in subjects:
        marks = [
            student["marks"][subject]
            for student in data.values()
            if subject in student["marks"]
        ]

        if marks:
            subject_averages[subject] = round(sum(marks) / len(marks), 1)

    return {
        "topper": topper,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }