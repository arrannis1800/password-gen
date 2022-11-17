from PyQt6.QtWidgets import QApplication, QMainWindow,QLineEdit
from PyQt6 import uic
import os
from password_db import *




class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("app.ui", self)

        self.Pass_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        # hide random pass button
        self.Random_pass.hide()
        self.Dismiss_button.hide()
        self.Pass_id.hide()

        # disable texts
        # self.Pass_name.setEnabled(False)
        self.update_list()

        self.list_of_passwords.itemClicked.connect(self.clicked_item_in_list)
        self.Reveal_pass.clicked.connect(self.reveal_pass)
        self.Update_button.clicked.connect(self.clicked_update_pass)
        self.Dismiss_button.clicked.connect(self.clicked_dismiss_pass)

    def update_list(self):
        self.passwords = csv_to_dist(open_csv())
        lis = [[x, y['name']] for x, y in self.passwords.items()]
        for el in lis:
            self.list_of_passwords.addItem(f'{el[0]}. {el[1]}')

    def clicked_update_pass(self,checked):
        button = self.Update_button
        if checked:
            button.setText('Save')
            self.Pass_name.setReadOnly(False)
            self.Pass_login.setReadOnly(False)
            self.Pass_pass.setReadOnly(False)
            self.Random_pass.show()
            self.Dismiss_button.show()
        elif not checked:
            button.setText('Update')
            self.Pass_name.setReadOnly(True)
            self.Pass_login.setReadOnly(True)
            self.Pass_pass.setReadOnly(True)
            self.Random_pass.hide()
            self.Dismiss_button.hide()


            update_pass(index_pass=self.Pass_id.text(), new_row=[self.Pass_name.text(), self.Pass_login.text(),
                                                                    self.Pass_pass.text(), self.Pass_created.text()])
            self.update_list()
            self.clicked_item_in_list()

    def clicked_dismiss_pass(self, checked):
        button = self.Update_button

        button.setChecked(False)
        button.setText('Update')
        self.Pass_name.setReadOnly(True)
        self.Pass_login.setReadOnly(True)
        self.Pass_pass.setReadOnly(True)
        self.Random_pass.hide()
        self.Dismiss_button.hide()

    def clicked_item_in_list(self):
        self.Update_button.setEnabled(True)
        self.Reveal_pass.setEnabled(True)
        item = self.list_of_passwords.currentItem()
        values = self.passwords[item.text().split('.')[0]]
        self.Pass_id.setText(item.text().split('.')[0])
        self.Pass_name.setText(values['name'])
        self.Pass_login.setText(values['login'])
        self.Pass_pass.setText(values['password'])
        self.Pass_created.setText(values['created_at'])
        self.Pass_updated.setText(values['updated_at'])

    def reveal_pass(self,checked):
        if checked:
            self.Pass_pass.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.Pass_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)


app = QApplication([])
window = UI()
window.show()
app.exec()

print('goodbye')
