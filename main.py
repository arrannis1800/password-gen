import os
import password_gen as pg
import password_db as pdb


def main_menu():
    print('''Hello, It's password gen. Few questions before\n''')

    while True:
        menu = input(
            '''\nWhat do you want to do?\n1. Create a new pass\n2. Show passwords\n\nq - for quit\n>> ''').lower()
        if menu in ('q', 'quit'):
            print('''Good bye!''')
            break
        elif menu in ('1', 'create'):
            num_char, chars, upper_chars, spec_chars = asking_params()
            password_gened = pg.generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                              spec_chars=spec_chars)
            while True:
                saving = input('''Do you want to save it? [Y|n]\n>> ''').lower()
                if saving in ('y', 'yes'):
                    name, login = pg.gen_pass_record()
                    pdb.save_pass(name=name, login=login, password=password_gened)
                    break
                elif saving in ('n', 'no'):
                    print('''Ok''')
                    break
                else:
                    print('''Can't understand. Please write Yes or No''')
        elif menu in ('2', 'show'):
            show_pass()


def updating_pass():
    while True:

        pass_id = input('''What password do you want to update [id]\nOr 'q' for quit\n>> ''').lower()
        if pass_id in ('q', 'quit'):
            return
        else:
            index_pass = pdb.find_pass(int(pass_id))
            if index_pass:
                break

    while True:
        update = input(
            '''What do you want to update\n1. Name of record.    2. Login.    3. Password\n'q' for quit\n>> ''').lower()
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
            new_type = pg.generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                        spec_chars=spec_chars)
        pdb.update_pass(index_pass=index_pass, index_in_row=index_in_row, new_type=new_type)
        break


def show_pass():
    print('''\nYour passwords list''')

    reader = pdb.open_csv('r')
    pages = int(-(-((len(reader) - 2) / 10) // 1))
    cur_page = 0

    while True:
        pdb.show_csv(reader, cur_page)

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
                    updating_pass()
                case _:
                    print('''Please, try again''')
            continue
        break


def asking_params():
    while True:
        try:
            num_char = int(input('''How long pass do you need?\n>> '''))
            break
        except:
            print('''Please, write a number\n''')

    while True:
        char_input = input('''Do you need letters in pass? [Y|n]\n>> ''').lower()
        if char_input in ('y', 'yes'):
            chars = True
            while True:
                upper_char_input = input('''Do you need capital letters in pass? [Y|n]\n>> ''').lower()
                if upper_char_input in ('y', 'yes'):
                    upper_chars = True
                    break
                elif upper_char_input in ('n', 'no'):
                    upper_chars = False
                    break
                else:
                    print('''Can't understand. Please write Yes or No''')
                    continue
        elif char_input in ('n', 'no'):
            chars = False
            upper_chars = False
            break
        else:
            print('''Can't understand. Please write Yes or No''')
            continue
        break

    while True:
        spec_char_input = input('''Do you need special chars in pass? [Y|n]\n>> ''').lower()
        if spec_char_input in ('y', 'yes'):
            spec_chars = True
            break
        elif spec_char_input in ('n', 'no'):
            spec_chars = False
            break
        else:
            print('''Can't understand. Please write Yes or No''')

    return num_char, chars, upper_chars, spec_chars


def main():
    pdb.create_csv()  # if not exist, create csv file for passwords
    os.system("cls")
    main_menu()  # opens main menu


if __name__ == '__main__':
    main()
    os.system("cls")
