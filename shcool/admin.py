import os


def show_teachers():
    with open('data\Teachers_subject', 'r', encoding='utf-8') as file:
        teachers = eval(file.read())
    for i in teachers:
        print(i + ' - ' + teachers.get(i) + '\n')


def add_teacher():
    with open('data\Teachers_subject', 'r', encoding='utf-8') as file:
        teachers_subject = eval(file.read())
    with open('data\Teachers', 'r', encoding='utf-8') as file:
        teachers = eval(file.read())
    name = input('Введите логин: ')
    password = input('Введите пароль: ')
    subject = input('Введите предмет: ')
    teachers_subject[name] = subject
    teachers[name] = password
    with open('data\Teachers_subject', 'w', encoding='utf-8') as file:
        file.write(str(teachers_subject))
    with open('data\Teachers', 'w', encoding='utf-8') as file:
        file.write(str(teachers))
    with open('data\students', 'r', encoding='utf-8') as file:
        tmp = eval(file.read())
        for item in tmp.keys():
            with open(f'data\students_grade\{item}', 'r', encoding='utf-8') as file:
                grades = eval(file.read())
                grades.append([f'{subject}: '])
            with open(f'data\students_grade\{item}', 'w', encoding='utf-8') as file:
                file.write(str(grades))


def delete_teacher():
    with open('data\Teachers_subject', 'r', encoding='utf-8') as file:
        teachers_subject = eval(file.read())
    with open('data\Teachers', 'r', encoding='utf-8') as file:
        teachers = eval(file.read())
    name = input('Введите логин: ')
    subject = input('Введите предмет: ')
    try:
        del teachers[name]
        del teachers_subject[name]
    except KeyError:
        pass
    with open('data\Teachers_subject', 'w', encoding='utf-8') as file:
        file.write(str(teachers_subject))
    with open('data\Teachers', 'w', encoding='utf-8') as file:
        file.write(str(teachers))
    with open('data\students', 'r', encoding='utf-8') as file:
        tmp = eval(file.read())
        for item in tmp.keys():
            with open(f'data\students_grade\{item}', 'r', encoding='utf-8') as file:
                grades = eval(file.read())
                for j, jitem in enumerate(grades):
                    if jitem[0] == f'{subject}: ':
                        grades.pop(j)
            with open(f'data\students_grade\{item}', 'w', encoding='utf-8') as file:
                file.write(str(grades))


groups = []


def show_groups():
    with open('data\groups\groups', 'r', encoding='utf-8') as file:
        global groups
        groups = eval(file.read())
        print('\n\t' + '*' * 3 + f' Выберите группу ' + '*' * 3 + '\n')
        for i, item in enumerate(groups):
            print(str(i + 1) + '. ' + item)


def show_group_students(x):
    with open(f'data\groups\{x}', 'r', encoding='utf-8') as file:
        students = eval(file.read())
        for i, item in enumerate(students):
            print(f'{i+1}. {item}')


def add_student():
    name = input('Введите логин: ')
    password = input('Введите пароль: ')
    class_ = input('Введите класс: ')
    with open('data\groups\groups', 'r', encoding='utf-8') as file:
        groups_ = eval(file.read())
        if class_ not in groups_:
            groups_.append(class_)
            with open(f'data\groups\{class_}', 'w', encoding='utf-8') as file:
                file.write('[]')
    with open('data\students', 'r', encoding='utf-8') as file:
        student_password = eval(file.read())
        student_password[name] = password
    with open(f'data\groups\{class_}', 'r', encoding='utf-8') as file:
        group = eval(file.read())
        group.append(name)
    with open('data\students', 'w', encoding='utf-8') as file:
        file.write(str(student_password))
    with open('data\groups\groups', 'w', encoding='utf-8') as file:
        file.write(str(groups_))
    with open(f'data\groups\{class_}', 'w', encoding='utf-8') as file:
        file.write(str(group))
    with open(f'data\students_grade\{name}', 'w', encoding='utf-8') as file:
        file.write('[]')


def delete_student():
    class_ = input('Введите класс: ')
    name = input('Введите логин: ')
    os.remove(f'data\students_grade\{name}')
    with open('data\students', 'r', encoding='utf-8') as file:
        student_password = eval(file.read())
    with open(f'data\groups\{class_}', 'r', encoding='utf-8') as file:
        group_ = eval(file.read())
    try:
        group_.remove(name)
        del student_password[name]
    except KeyError:
        pass
    with open('data\students', 'w', encoding='utf-8') as file:
        file.write(str(student_password))
    with open(f'data\groups\{class_}', 'w', encoding='utf-8') as file:
        file.write(str(group_))
    with open(f'data\groups\{class_}', 'r', encoding='utf-8') as file:
        data = file.read()
    if data == '[]':
        os.remove(f'data\groups\{class_}')
        with open(f'data\groups\groups', 'r', encoding='utf-8') as file:
            tmp = eval(file.read())
            tmp.remove(class_)
        with open(f'data\groups\groups', 'w', encoding='utf-8') as file:
            file.write(str(tmp))
