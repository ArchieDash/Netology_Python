students = [
    {
        "Name": "Владимир Кондратенко",
        "Gender": "M",
        "Experience": "N",
        "Home_Work": (8, 7, 5, 5, 7),
        "Exam": 6
    },
    {
        "Name": "Мария Панфилова",
        "Gender": "F",
        "Experience": "N",
        "Home_Work": (9, 8, 5, 6, 0),
        "Exam": 5
    },
    {
        "Name": "Игорь Соколов",
        "Gender": "M",
        "Experience": "N",
        "Home_Work": (4, 6, 8, 0, 0),
        "Exam": 8
    },
    {
        "Name": "Сергей Федяев",
        "Gender": "M",
        "Experience": "Y",
        "Home_Work": (10, 10, 7, 8, 9),
        "Exam": 8
    },
    {
        "Name": "Вера Филина",
        "Gender": "F",
        "Experience": "N",
        "Home_Work": (6, 7, 7, 8, 8),
        "Exam": 8
    },
    {
        "Name": "Игорь Соколов",
        "Gender": "M",
        "Experience": "Y",
        "Home_Work": (9, 8, 8, 9, 10),
        "Exam": 10
    },
    {
        "Name": "Алина Полякова",
        "Gender": "F",
        "Experience": "N",
        "Home_Work": (10, 8, 6, 4, 8),
        "Exam": 7
    },
    {
        "Name": "Вероника Найдёнова",
        "Gender": "F",
        "Experience": "Y",
        "Home_Work": (10, 9, 10, 9, 10),
        "Exam": 9
    },
    {
        "Name": "Николай Назаров",
        "Gender": "M",
        "Experience": "N",
        "Home_Work": (8, 8, 8, 7, 6),
        "Exam": 8
    },
    {
        "Name": "Анастасия Ермакова",
        "Gender": "F",
        "Experience": "Y",
        "Home_Work": (9, 7, 7, 8, 9),
        "Exam": 8
    }
]


def average(var):
    avg = sum(var) / len(var)
    return avg


def avg_group_task(task):
    avg_students = []
    for student in students:
        if task == "Home_Work":
            avg_students.append(average(student["Home_Work"]))
        elif task == "Exam":
            avg_students.append(student["Exam"])
    if task == "Home_Work":
        print("Средняя оценка по группе за домашние задания:", round(average(avg_students), 2))
    elif task == "Exam":
        print("Средняя оценка по группе за экзамен:", round(average(avg_students), 2))


def avg_task_by_gender(task, gender):
    avg_students = []
    for student in students:
        if student["Gender"] == gender:
            if task == "Home_Work":
                avg_students.append(average(student["Home_Work"]))
            elif task == "Exam":
                avg_students.append(student["Exam"])
    if gender == "M" and task == "Home_Work":
        print("Средняя оценка за домашние задания у мужчин:", round(average(avg_students), 2))
    elif gender == "F" and task == "Home_Work":
        print("Средняя оценка за домашние задания у женщин:", round(average(avg_students), 2))
    elif gender == "M" and task == "Exam":
        print("Средняя оценка за экзамен у мужчин:", round(average(avg_students), 2))
    elif gender == "F" and task == "Exam":
        print("Средняя оценка за экзамен у женщин:", round(average(avg_students), 2))


def avg_task_by_exp(task, exp):
    avg_students = []
    for student in students:
        if student["Experience"] == exp:
            if task == "Home_Work":
                avg_students.append(average(student["Home_Work"]))
            elif task == "Exam":
                avg_students.append(student["Exam"])
    if exp == "Y" and task == "Home_Work":
        print("Средняя оценка по группе за домашние задания у студентов с опытом:", round(average(avg_students), 2))
    elif exp == "N" and task == "Home_Work":
        print("Средняя оценка по группе за домашние задания у студентов без опыта:", round(average(avg_students), 2))
    elif exp == "Y" and task == "Exam":
        print("Средняя оценка за экзамен у студентов с опытом::", round(average(avg_students), 2))
    elif exp == "N" and task == "Exam":
        print("Средняя оценка за экзамен у студентов без опыта:", round(average(avg_students), 2))


def best_students():
    marks = []
    results = []
    for student in students:
        mark = 0.6 * average(student["Home_Work"]) + 0.4 * (student["Exam"])
        results.append(mark)
        student_mark = dict.fromkeys(["Name"], ["Mark"])
        student_mark["Name"] = student["Name"]
        student_mark["Mark"] = mark
        marks.append(student_mark)
    for student in marks:
        best = []
        if student["Mark"] == max(results):
            best.append(student["Name"])
            if len(best) == 1:
                print("Лучший студент -", best[0], "с интегральной оценкой:", student["Mark"])
            elif len(best) > 1:
                print("Лучшие студенты -", best[0:], "с интегральной оценкой:", student["Mark"])


def main():
    print("Система учета успеваемости студентов\n\n")
    print("1 - Средняя оценка по группе за домашние задания\n2 - Средняя оценка по группе за экзамен\n3 - Средняя оценка за домашние задания у мужчин\n4 - Средняя оценка за домашние задания у женщин\n5 - Средняя оценка за экзамен у мужчин\n6 - Средняя оценка за экзамен у женщин\n7 - Средняя оценка за домашние задания у студентов с опытом\n8 - Средняя оценка за домашние задания у студентов без опыта\n9 - Средняя оценка за экзамен у студентов с опытом\n10 - Средняя оценка за экзамен у студентов без опыта\n11 - Лучшие студенты\n0 - завершение программы")

    while True:
        console = input()
        if console == "1":
            avg_group_task("Home_Work")
        elif console == "2":
            avg_group_task("Exam")
        elif console == "3":
            avg_task_by_gender("Home_Work", "M")
        elif console == "4":
            avg_task_by_gender("Home_Work", "F")
        elif console == "5":
            avg_task_by_gender("Exam", "M")
        elif console == "6":
            avg_task_by_gender("Exam", "F")
        elif console == "7":
            avg_task_by_exp("Home_Work", "Y")
        elif console == "8":
            avg_task_by_exp("Home_Work", "N")
        elif console == "9":
            avg_task_by_exp("Exam", "Y")
        elif console == "10":
            avg_task_by_exp("Exam", "N")
        elif console == "11":
            best_students()
        elif console == "0":
            break


main()