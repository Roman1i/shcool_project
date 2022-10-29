import os


def get_group(login):
    files = os.listdir('data\groups')
    for item in files:
        with open(f'data\groups\{item}', 'r', encoding='utf-8') as file:
            file_data = eval(file.read())
            if login in file_data:
                return item


def show_grades(login):
    with open(f'data\students_grade\{login}', 'r', encoding='utf-8') as file:
        grades = eval(file.read())
        for item in grades:
            print(*item)
