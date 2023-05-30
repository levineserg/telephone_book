import view

def add_dat(data):
    with open('db.txt', 'a') as file:
        file.write(data)
    print('Телефонная книга обновлена\n')

def search_name(name):
    with open('db.txt', 'r') as file:
        data = file.readlines()
        flag = False

        for i in data:
            if name in i:
                print(i.strip())
                flag = True
        if flag == False:
            print('Абонент не найден\n')

def sort_db_name():
    with open('db.txt', 'r') as file:
        data = file.readlines()
        data.sort()
    with open('db.txt', 'w') as file:
        file.writelines(data)

def print_name():
    with open('db.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            print(i.split()[0])

def print_db():
    with open('db.txt', 'r') as file:
        print(file.read())

def select(name):
    list_data = []
    count = 1
    with open('db.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            if name in i:
                print(f"{count}) {i.strip()}")
                count += 1
                list_data.append(i)
    return list_data

def delete(name):
    with open('db.txt', 'r') as file:
        full_list = file.readlines()
    with open('db.txt', 'w') as file:
        for i in full_list:
            if name == i:
                continue
            file.write(i)
    print('Запись удалена')

def change(old_str, new_str):
    with open('db.txt', 'r',) as file:
        full_list = file.readlines()
    with open('db.txt', 'w') as file:
        for i in full_list:
            if i == old_str:
                file.write(new_str)
                continue
            file.write(i)
    print('Запись изменена')

