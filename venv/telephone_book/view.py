def user_input():
    ask = int(input('Выбери ниже\n 1-записать пользователя в телефонную книгу\n 2-поиск по имени\n '
                    '3-отсортировать справочник по имени\n 4-вывод только имён\n'
                    ' 5-вывод всего справочника\n 6-изменить данные\n'
                    ' 7-удалить данные \n 8-выход\n'))
    return ask

def input_man():
    name = input('Введите имя: ')
    family = input('Введите фамилию: ')
    telephone = input('Введите дату номер телефона: ')
    data = name + ' ' + family + ' ' + telephone + ' ' + '\n'
    return data.lower()

def search_name():
    str_search = input('Введите имя для поиска: ').lower()
    return str_search

def select_number():
    num = int(input('Выбери строчку для изменения: '))
    return num


