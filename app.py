from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6 import uic
from password_db import *
from password_gen import *


class UI(QMainWindow):
    def __init__(self):
        super().__init__()



        # loading the ui file with uic module
        self.passwords = None
        uic.loadUi("app.ui", self)

        self.settings = QSettings('MyQtApp', 'App1')
        try:
            self.length_num.setText(str(self.settings.value('num_char')))
            self.length_pass.setValue(self.settings.value('num_char'))
            self.low_case.setChecked(eval(self.settings.value('chars').capitalize()))
            self.spec_symb.setChecked(eval(self.settings.value('spec_chars').capitalize()))
            self.upper_case.setChecked(eval(self.settings.value('upper_chars').capitalize()))
        except Exception as e:
            print(e)

        self.Pass_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        # hide random pass button
        self.Random_pass.hide()
        self.Dismiss_button.hide()
        self.Pass_id.hide()

        self.Menu_pass.hide()

        self.length_num.hide()
        self.length_pass.hide()
        self.low_case.hide()
        self.spec_symb.hide()
        self.upper_case.hide()

        # show passwords
        self.update_list()

        self.list_of_passwords.itemClicked.connect(self.clicked_item_in_list)
        self.Reveal_pass.clicked.connect(self.reveal_pass)
        self.Update_button.clicked.connect(self.clicked_update_pass)
        self.Dismiss_button.clicked.connect(self.clicked_dismiss_pass)
        self.Random_pass.clicked.connect(self.generate_pass)
        self.Menu_pass.clicked.connect(self.show_popup)
        self.length_pass.valueChanged.connect(self.set_num_length_pass)

    def set_num_length_pass(self):
        self.length_num.setText(str(self.length_pass.value()))

    def show_popup(self,checked):
        if checked:
            self.length_num.show()
            self.length_pass.show()
            self.low_case.show()
            self.spec_symb.show()
            self.upper_case.show()
        else:
            self.length_num.hide()
            self.length_pass.hide()
            self.low_case.hide()
            self.spec_symb.hide()
            self.upper_case.hide()

    def generate_pass(self):
        num_char = self.length_pass.value()
        chars = self.low_case.isChecked()
        upper_chars = self.upper_case.isChecked()
        spec_chars = self.spec_symb.isChecked()
        self.Pass_pass.setText(generate_pass(num_char=num_char, chars=chars, upper_chars=upper_chars,
                                             spec_chars=spec_chars))

    def update_list(self):
        self.passwords = csv_to_dist(open_csv())
        lis = [[x, y['name']] for x, y in self.passwords.items()]
        for el in lis:
            self.list_of_passwords.addItem(f'{el[0]}. {el[1]}')

    def clicked_update_pass(self, checked):
        button = self.Update_button
        if checked:
            button.setText('Save')
            self.Pass_name.setReadOnly(False)
            self.Pass_login.setReadOnly(False)
            self.Pass_pass.setReadOnly(False)
            self.Random_pass.show()
            self.Dismiss_button.show()
            self.Menu_pass.show()
        elif not checked:
            button.setText('Update')
            self.Pass_name.setReadOnly(True)
            self.Pass_login.setReadOnly(True)
            self.Pass_pass.setReadOnly(True)
            self.Random_pass.hide()
            self.Dismiss_button.hide()
            self.Menu_pass.hide()

            update_pass(index_pass=self.Pass_id.text(), new_row=[self.Pass_name.text(), self.Pass_login.text(),
                                                                 self.Pass_pass.text(), self.Pass_created.text()])
            self.update_list()
            self.clicked_item_in_list()

    def clicked_dismiss_pass(self):
        button = self.Update_button

        button.setChecked(False)
        button.setText('Update')
        self.Pass_name.setReadOnly(True)
        self.Pass_login.setReadOnly(True)
        self.Pass_pass.setReadOnly(True)
        self.Random_pass.hide()
        self.Dismiss_button.hide()
        self.Menu_pass.hide()
        self.length_num.hide()
        self.length_pass.hide()
        self.low_case.hide()
        self.spec_symb.hide()
        self.upper_case.hide()

    def clicked_item_in_list(self):
        self.Update_button.setEnabled(True)
        self.Reveal_pass.setEnabled(True)
        self.Menu_pass.setEnabled(True)
        item = self.list_of_passwords.currentItem()
        values = self.passwords[item.text().split('.')[0]]
        self.Pass_id.setText(item.text().split('.')[0])
        self.Pass_name.setText(values['name'])
        self.Pass_login.setText(values['login'])
        self.Pass_pass.setText(values['password'])
        self.Pass_created.setText(values['created_at'])
        self.Pass_updated.setText(values['updated_at'])

    def reveal_pass(self, checked):
        if checked:
            self.Pass_pass.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.Pass_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

    def closeEvent(self, event):
        self.settings.setValue('num_char',self.length_pass.value())
        self.settings.setValue('chars', self.low_case.isChecked())
        self.settings.setValue('upper_chars', self.upper_case.isChecked())
        self.settings.setValue('spec_chars', self.spec_symb.isChecked())
        keys = self.settings.allKeys()
        print(keys)
        for key in keys:
            print(self.settings.value(key))





def app_exec():
    app = QApplication([])

    window = UI()
    window.show()
    app.exec()


if __name__ == '__main__':
    create_csv()

    app_exec()
