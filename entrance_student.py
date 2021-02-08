import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Entrance_Student(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("data/project.db")
        self.cur = self.polz.cursor()
        super().__init__()
        uic.loadUi('data/design_ent_check.ui', self)
        self.initUI()

    def initUI(self):
        pass
