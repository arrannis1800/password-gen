import os
import csv
import password_gen as pg



def create_csv():
    if 'passwords.csv' not in os.listdir():
        headers = ['id', 'name', 'login', 'password', 'created_at', 'updated_at']
        with open('passwords.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print('''>> CSV file created \n''')


def main_menu():
    print('''Hello, It's password gen. Few questions before\n''')

    while True:
        menu = input(
            '''\nWhat do you want to do?\n1. Create a new pass\n2. Show passwords\n\nq - for quit\n>> ''').lower()
        if menu in ('q', 'quit'):
            print('''Good bye!''')
            break
        elif menu in ('1', 'create'):
            num_char, chars, upper_chars, spec_chars = pg.asking_params()
            password_gened = pg.generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                           spec_chars=spec_chars)
            while True:
                saving = input('''Do you want to save it? [Y|n]\n>> ''').lower()
                if saving in ('y', 'yes'):
                    name = input('''How to name it?\n>> ''')
                    login = input('''And what login?\n>> ''')
                    pg.save_pass(name=name, login=login, password=password_gened)
                    break
                elif saving in ('n', 'no'):
                    print('''Ok''')
                    break
                else:
                    print('''Can't understand. Please write Yes or No''')
        elif menu in ('2', 'show'):
            show_pass()


def updating_pass():
    with open("passwords.csv", 'r') as file:
        reader = file.readlines()
        while True:

            pass_id = input('''What password do you want to update [id]\nOr 'q' for quit\n>> ''').lower()
            if pass_id in ('q', 'quit'):
                return
            else:
                try:
                    pass_id = int(pass_id)
                except:
                    print('''Something was wrong try again to type a password id''')
                    continue
            row_num = 0
            for i, row in enumerate(reader):
                row_id = row.split(',')[0]
                if str(pass_id) == row_id:
                    row_num = i
                    break
            if row_num != 0:
                break
            print('''Can't find a pass with this id''')

        while True:
            update = input('''What do you want to update\n1. Name of record.    2. Login.    3. Password\n'q' for quit\n>> ''').lower()
            match update:
                case 'q' | 'quit':
                    return
                case '1' | 'name':
                    index_in_row = 1
                case '2' | 'login':
                    index_in_row = 2
                case '3' | 'pass' | 'password':
                    index_in_row = 3
                case _:
                    continue
            string = '''Type a new one'''
            if index_in_row == 3:
                string += ''' or autogenerate [g]'''
            string += '''\n>> '''
            new_type = input(string)
            if new_type in ('g', 'generate', 'autogenerate'):
                num_char, chars, upper_chars, spec_chars = asking_params()
                new_type = generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                               spec_chars=spec_chars)
            break


def show_pass():
    print('''\nYour passwords list''')
    with open("passwords.csv", 'r') as file:
        reader = file.readlines()
        pages = int(-(-((len(reader) - 2) / 10) // 1))
        cur_page = 0
        while True:
            print(reader[0].replace(',', '   |  '))
            for row in reader[cur_page * 10 + 2:min(cur_page * 10 + 12, len(reader))]:
                print(row.replace(',', '   |  '), end='')
            if pages > 1:
                print(f'''\nIt's {cur_page + 1} page of {pages}''')
                string = ''
                if cur_page != 0:
                    string += '''For move on previous page type "<". '''
                if cur_page != pages - 1:
                    string += '''For move on next page type ">". '''
                if len(reader) > 2:
                    string += '''\nFor update pass type "u". '''
                string += '''\nTo return to main menu type "q". \n>> '''
                action = input(string).lower()
                match action:
                    case 'q' | 'quit':
                        break
                    case '>':
                        if cur_page != pages - 1:
                            cur_page += 1
                    case '<':
                        if cur_page != 0:
                            cur_page -= 1
                    case 'u' | 'update':
                        file.close()
                        pg.updating_pass()
                        return show_pass()
                    case _:
                        print('''Please, try again''')
                continue
            break






def main():
    create_csv()  # if not exist, create csv file for passwords
    os.system("cls")
    main_menu()  # opens main menu


if __name__ == '__main__':
    main()
    os.system("cls")

