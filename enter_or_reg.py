import sys
import sqlite3

from PyQt5 import uic
from regist import Registration
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class enter_or_regist(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('Enter_or_regist.ui', self)
        self.initUI()

    def initUI(self):
        self.btn_enter.clicked.connect(self.enter)
        self.btn_regist.clicked.connect(self.regist)

    def enter(self):
        pass

    def regist(self):
        self.wind_reg = Registration()
        self.wind_reg.show()