import random
import os
import csv
from datetime import datetime as dt


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
        main_menu = input(
            '''\nWhat do you want to do?\n1. Create a new pass\n2. Show passwords\n\nq - for quit\n>> ''').lower()
        if main_menu in ('q', 'quit'):
            print('''Good bye!''')
            break
        elif main_menu in ('1', 'create'):
            num_char, chars, upper_chars, spec_chars = asking_params()
            password_gened = generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                           spec_chars=spec_chars)
            while True:
                saving = input('''Do you want to save it? [Y|n]\n>> ''').lower()
                if saving in ('y', 'yes'):
                    save_pass(password_gened)
                    break
                elif saving in ('n', 'no'):
                    print('''Ok''')
                    break
                else:
                    print('''Can't understand. Please write Yes or No''')
        elif main_menu in ('2', 'show'):
            show_pass()


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


def generate_pass(num_char=20, chars=True, upper_chars=True, spec_chars=True):
    acceptable_chars = [i for i in range(48, 58)]  # nums
    if chars:
        acceptable_chars += [i for i in range(97, 123)]  # lowercase letters
    if upper_chars:
        acceptable_chars += [i for i in range(65, 91)]  # uppercase letter
    if spec_chars:
        acceptable_chars += [i for i in range(34, 48)] \
                            + [i for i in range(58, 65)] \
                            + [i for i in range(91, 97)] \
                            + [i for i in range(123, 127)]  # special characters

    password = ''.join(chr(int(random.choice(acceptable_chars))) for i in range(num_char))
    print('''Your password is >>>''', password)

    return password


def save_pass(password):
    name = input('''How to name it?\n>> ''')
    login = input('''And what login?\n>> ''')
    curtime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("passwords.csv", 'r') as file:
        reader = file.readlines()
        try:
            pass_id = int(reader[-1].split(',')[0]) + 1
        except:
            pass_id = 1
        new_row = [pass_id, name, login, password, curtime, curtime]

    with open('passwords.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

    print('''It was saved in csv file''')


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
                string += '''\nTo return to main menu type "q". \n>> '''
                action = input(string).lower()
                match action:
                    case 'q':
                        break
                    case '>':
                        if cur_page != pages - 1: cur_page += 1
                    case '<':
                        if cur_page != 0: cur_page -= 1
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
