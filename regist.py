import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Registration(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("project.db")
        self.cur = self.films.cursor()
        super().__init__()
        uic.loadUi('design_regist.ui', self)
        self.initUI()

    def initUI(self):
        self.btn_regist.clicked.connect(self.registra)
        self.btn_go_back.clicked.connect(self.back)

    def registra(self):
        self.surname = self.edit_surname.text()
        self.name = self.edit_name.text()
        self.city = self.edit_city.text()
        self.school = self.edit_school.text()
        self.school_class = self.edit_class.text()
        self.login = self.edit_login.text()
        self.password = self.edit_password.text()
        self.role = self.edit_role.text()
        My_sql_query = """SELECT * from Users where Login = ? """
        self.cur.execute(My_sql_query, (self.login,))
        record = len(self.cur.fetchall())
        if self.role == 'Учитель':
            if (self.surname != '') and (self.name != '') and (self.login != '') and (self.password != '') and \
                    (self.school != '') and (self.school_class != '') and (self.city != ''):
                if (record == 0) and (self.vvod_password.text() == self.repitin_password.text()):
                    self.cur.execute("INSERT INTO users students(?, ?, ?, ?, ?, ?, ?)",
                                     (self.surname, self.name, self.city, self.school, self.school_class, self.login,
                                      self.password, ''))
                    self.films.commit()
                elif record != 0:
                    reply = QMessageBox.about(self, 'Error',
                                              "Такой логин уже существует, придумайте новый.")

                elif (self.vvod_password.text() != self.repit_password.text()):
                    reply = QMessageBox.about(self, 'Error',
                                              "Пароли не совпадают.")
            else:
                reply = QMessageBox.about(self, 'Error',
                                          "Заполните пустые строки.")
        elif self.role == 'Ученик':
            if (self.surname != '') and (self.name != '') and (self.login != '') and (self.password != '') and \
                    (self.school != '') and (self.school_class != '') and (self.city != ''):
                if (record == 0) and (self.vvod_password.text() == self.repitin_password.text()):
                    self.cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)",
                                     (self.surname, self.name, self.city, self.school, self.school_class, self.login,
                                      self.password, ''))
                    self.films.commit()
                elif record != 0:
                    reply = QMessageBox.about(self, 'Error',
                                              "Такой логин уже существует, придумайте новый.")

                elif (self.vvod_password.text() != self.repit_password.text()):
                    reply = QMessageBox.about(self, 'Error',
                                              "Пароли не совпадают.")
            else:
                reply = QMessageBox.about(self, 'Error',
                                          "Заполните пустые строки.")
