import view
import teacher
import student
import admin as ad

with open('data\Teachers', 'r', encoding='utf-8') as file:
    teachers = eval(file.read())
with open('data\Teachers_subject', 'r', encoding='utf-8') as file:
    teachers_subject = eval(file.read())
with open('data\students', 'r', encoding='utf-8') as file:
    students = eval(file.read())
#with open('students_group', 'r', encoding='utf-8') as file:
#    students_group = eval(file.read())
admin = {'admin': 'admin'}


def login_process(x):
    login_ = input('Введите логин: ')
    password_ = input('Введите пароль: ')
    while x.get(login_) is None or x.get(login_) != password_:
        print('Указан неверный логин или пароль')
        login_ = input('Введите логин: ')
        password_ = input('Введите пароль: ')
    if x == teachers:
        view.teacher_menu(login_, teachers_subject.get(login_))
    elif x == students:
        view.student_menu(login_, students_group.get(login_))
    elif x == admin:
        view.admin_menu()






