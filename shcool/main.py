with open('groups\groups', 'r', encoding='utf-8') as file:
    lst_ = eval(file.read())

if input() in lst_:
    print('True')
else:
    print('False')
