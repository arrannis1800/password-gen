import os
import csv
from datetime import datetime as dt


def create_csv():
    if 'passwords.csv' not in os.listdir():
        headers = ['id', 'name', 'login', 'password', 'created_at', 'updated_at']
        with open('passwords.csv', 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print('''>> CSV file created \n''')


def open_csv(mode):
    with open("passwords.csv", mode, encoding="utf-8") as file:
        return file.readlines()


def show_csv(file, cur_page=0):
    print(file[0].replace(',', '   |  '))
    for row in file[cur_page * 10 + 2:min(cur_page * 10 + 12, len(file))]:
        print(row.replace(',', '   |  '), end='')


def save_pass(name='', login='', password=''):
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
    reader = open_csv('r')

    try:
        pass_id = int(pass_id)
    except:
        print('''Something was wrong try again to type a password id''')
        return

    row_num = 0
    for i, row in enumerate(reader):
        row_id = row.split(',')[0]
        if str(pass_id) == row_id:
            row_num = i
            break
    if row_num != 0:
        return row_num
    print('''Can't find a pass with this id''')


def update_pass(index_pass, index_in_row, new_type):

    with open('passwords.csv', 'r') as readFile, open('passwords.csv'.replace('.csv', '_new.csv'), 'w') as writeFile:
        for i, row in enumerate(readFile):
            if i == index_pass:
                row = row.split(',')
                row[index_in_row] = new_type
                row[5] = dt.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'
                writeFile.write(','.join(row))
            else:
                writeFile.write(row)

    os.remove('passwords.csv')
    os.rename('passwords_new.csv', 'passwords.csv')