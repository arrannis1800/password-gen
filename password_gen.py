import random
from datetime import datetime as dt
import csv
import os

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
        acceptable_chars += [i for i in range(34, 44)] \
                            + [i for i in range(45, 48)] \
                            + [i for i in range(58, 65)] \
                            + [i for i in range(91, 97)] \
                            + [i for i in range(123, 127)]  # special characters

    password = ''.join(chr(int(random.choice(acceptable_chars))) for i in range(num_char))
    print('''Your password is >>>''', password)

    return password


def save_pass(name='', login='',password=''):
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


def find_pass(pass_id):
    with open("passwords.csv", 'r') as file:
        reader = file.readlines()



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



    with open('passwords.csv', 'r') as readFile, open('passwords.csv'.replace('.csv', '_new.csv'), 'w') as writeFile:
        for i, row in enumerate(readFile):
            if i == row_num:
                row = row.split(',')
                row[index_in_row] = new_type
                row[5] = dt.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'
                writeFile.write(','.join(row))
            else:
                writeFile.write(row)

    os.remove('passwords.csv')
    os.rename('passwords_new.csv', 'passwords.csv')

