import admin


def journal(subject):
    admin.show_groups()
    group = input('Введите группу: ')
    with open(f'data\groups\{group}', 'r', encoding='utf-8') as file:
        students = eval(file.read())
    for student in students:
        with open(f'data\students_grade\{student}', 'r', encoding='utf-8') as file:
            student_grades = eval(file.read())
            for item in student_grades:
                if item[0] == f'{subject}: ':
                    print(f'{student}: {item[1:]}')


def grade(subject):
    name = input('Введите имя ученика: ')
    digit = input('Оценка: ')
    with open(f'data\students_grade\{name}', 'r', encoding='utf-8') as file:
        subs = eval(file.read())
        for item in subs:
            if item[0] == f'{subject}: ':
                item.append(digit)
    with open(f'data\students_grade\{name}', 'w', encoding='utf-8') as file:
        file.write(str(subs))
