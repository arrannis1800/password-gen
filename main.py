import random
import os
import csv
from datetime import datetime as dt


def create_csv():
    if 'passwords.csv' not in os.listdir():
        headers = ['id', 'password', 'datetime']
        with open('passwords.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(headers)


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
        acceptable_chars += [i for i in range(34, 48)]  # special numbers
        acceptable_chars += [i for i in range(58, 65)]
        acceptable_chars += [i for i in range(91, 97)]
        acceptable_chars += [i for i in range(123, 127)]

    password = ''.join(chr(int(random.choice(acceptable_chars))) for i in range(num_char))
    print('''Your password is >>>''', password)

    return password


def save_pass(password):
    with open("passwords.csv", 'r') as file:
        reader = file.readlines()
        new_row = [1 if len(reader) == 1 else int(reader[-1].split(',')[0]) + 1, password, dt.now().strftime("%Y-%m-%d %H:%M:%S")]

    with open('passwords.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)


def main():
    create_csv()

    os.system("cls")
    print('''Hello, It's password gen. Few questions before\n''')

    while True:
        menu_1 = input('''What do you want to do?\n1. Create a new pass\n\nq - for quit\n>> ''').lower()
        if menu_1 in ('q', 'quit'):
            break
        elif menu_1 in ('1', 'pass', 'password', 'create'):
            num_char, chars, upper_chars, spec_chars = asking_params()
            password_gened = generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                           spec_chars=spec_chars)
            while True:
                saving = input('''Do you want to save it? [Y|n]\n>> ''').lower()
                if saving in ('y', 'yes'):
                    save_pass(password_gened)
                    print('''It was saved in csv file''')
                    break
                elif saving in ('n', 'no'):
                    print('''Ok''')
                    break
                else:
                    print('''Can't understand. Please write Yes or No''')




if __name__ == '__main__':
    main()
