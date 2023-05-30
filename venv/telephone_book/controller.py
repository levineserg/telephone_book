import view
import database

def main():
    while True:
        ask = view.user_input()
        print(ask)
        if ask == 1:
            data = view.input_man()
            database.add_dat(data)
        elif ask == 2:
            name = view.search_name()
            database.search_name(name)
        elif ask == 3:
            database.sort_db_name()
        elif ask == 4:
            database.print_name()
        elif ask == 5:
            database.print_db()
        elif ask == 6:
            name = view.search_name()
            list_name = database.select(name)
            num = view.select_number()
            new_name = view.input_man()
            database.change(list_name[num - 1], new_name)
        elif ask == 7:
            name = view.search_name()
            list_name = database.select(name)
            num = view.select_number()
            database.delete(list_name[num - 1])
        elif ask == 8:
            print('Справочник закрыт')
            break
main()

