# Въвеждане на броя на студентите
num_students = int(input())

# Инициализация на броячите за всяка категория оценки
top_students = 0
grade_4_to_4_99 = 0
grade_3_to_3_99 = 0
fail_students = 0

# Променлива за сумата на всички оценки
total_grades = 0

# Обхождаме всеки студент
for _ in range(num_students):
    grade = float(input())  # Четем оценката на текущия студент
    total_grades += grade   # Добавяме оценката към общата сума

    # Разпределяме оценката в съответната категория
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        grade_4_to_4_99 += 1
    elif 3.00 <= grade <= 3.99:
        grade_3_to_3_99 += 1
    else:  # grade < 3.00
        fail_students += 1

# Изчисляваме процента студенти във всяка категория
top_students_percent = (top_students / num_students) * 100
grade_4_to_4_99_percent = (grade_4_to_4_99 / num_students) * 100
grade_3_to_3_99_percent = (grade_3_to_3_99 / num_students) * 100
fail_students_percent = (fail_students / num_students) * 100

# Изчисляваме средния успех
average_grade = total_grades / num_students

# Принтираме резултатите, форматирани до втория знак след десетичната запетая
print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {grade_4_to_4_99_percent:.2f}%")
print(f"Between 3.00 and 3.99: {grade_3_to_3_99_percent:.2f}%")
print(f"Fail: {fail_students_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
