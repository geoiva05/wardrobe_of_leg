import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from registration_Teacher import Registration_Teacher
from registration_Student import Registration_Student


class Check_entrance(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('data/check.ui', self)
        self.center()
        self.btn_like_teacher.setText('Войти как учитель')
        self.btn_like_student.setText('Войти как ученик')
        self.btn_like_student.clicked.connect(self.entrance_like_student)
        self.btn_like_teacher.clicked.connect(self.entrance_like_teacher)
        self.btn_back.clicked.connect(self.back)

    def entrance_like_teacher(self):
        pass

    def entrance_like_student(self):
        pass

    def back(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())