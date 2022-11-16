from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os
from password_db import *




class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("app.ui", self)

        self.passwords = csv_to_dist(open_csv())

        # hide random pass button
        self.Random_pass.hide()

        # disable texts
        # self.Pass_name.setEnabled(False)
        self.update_list()

        self.list_of_passwords.itemClicked.connect(self.clicked)

    def update_list(self):
        lis = [[x, y['name']] for x, y in self.passwords.items()]
        for el in lis:
            self.list_of_passwords.addItem(f'{el[0]}. {el[1]}')

    def clicked(self):
        item = self.list_of_passwords.currentItem()
        values = self.passwords[item.text().split('.')[0]]
        self.Pass_name.setText(values['name'])
        self.Pass_login.setText(values['login'])
        self.Pass_pass.setText(values['password'])
        self.Pass_created.setText(values['created_at'])
        self.Pass_updated.setText(values['updated_at'])
        print(values)


app = QApplication([])
window = UI()
window.show()
app.exec()

print('goodbye')
