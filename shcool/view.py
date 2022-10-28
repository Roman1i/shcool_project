import admin
import login


def login_screen():
    print('\n\t' + '*' * 3 + ' Вход в учетную запись ' + '*' * 3 + '\n')
    print('1. Преподаватель ')
    print('2. Студент')
    print('3. Администратор')
    x = input()
    if x == '1':
        login.login_process(login.teachers)
    elif x == '2':
        login.login_process(login.students)
    elif x == '3':
        login.login_process(login.admin)


def teacher_menu(login_, subject):
    print('\n\t' + '*' * 3 + f' Личный кабинет {login_} ' + '*' * 3 + '')
    print(f'\t {subject}\n')
    print('1. учить ')
    print('2. учить')
    print('3. учить')


def student_menu(login_, group):
    print('\n\t' + '*' * 3 + f' Личный кабинет {login_} ' + '*' * 3 + '')
    print(f'\t Ученик {group} класса\n')
    print('1. учиться ')
    print('2. учиться')
    print('3. учиться')


def admin_menu():
    print('\n\t' + '*' * 3 + f' Режим администратора ' + '*' * 3 + '\n')
    print('1. Учителя')
    print('2. Студенты')
    print('3. Выйти')
    x = input()
    if x == '1':
        admin_teacher_menu()
    if x == '2':
        admin_student_menu()
    if x == '3':
        login_screen()


def admin_teacher_menu():
    print('\n\t' + '*' * 3 + f' Учителя ' + '*' * 3 + '\n')
    print('1. Просмотр')
    print('2. Добавить')
    print('3. Удалить')
    print('4. Назад')
    x = input()
    if x == '1':
        admin.show_teachers()
        admin_teacher_menu()
    if x == '2':
        admin.add_teacher()
        admin_teacher_menu()
    if x == '3':
        admin.delete_teacher()
        admin_teacher_menu()
    if x == '4':
        admin_menu()


def admin_student_menu():
    print('\n\t' + '*' * 3 + f' Студенты ' + '*' * 3 + '\n')
    print('1. Просмотр')
    print('2. Добавить')
    print('3. Удалить')
    print('4. Назад')
    x = input()
    if x == '1':
        admin.show_groups()
        y = input()
        admin.show_group_students(admin.groups[int(y) - 1])
        admin_student_menu()
    if x == '2':
        admin.add_student()
        admin_student_menu()
    if x == '3':
        admin.delete_student()
        admin_student_menu()
    if x == '4':
        admin_menu()






