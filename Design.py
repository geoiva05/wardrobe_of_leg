import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from registration_Teacher import Registration_Teacher


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class apposition(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Enter_or_regist.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.btn_enter.clicked.connect(self.Entrance)
        self.btn_regist.clicked.connect(self.Regist)

    def Entrance(self):
        uic.loadUi('data/check.ui', self)
        self.btn_like_teacher.setText('Войти как учитель')
        self.btn_like_student.setText('Войти как ученик')

        self.btn_like_student.clicked.connect(self.entrance_like_student)
        self.btn_like_teacher.clicked.connect(self.entrance_like_teacher)
        self.btn_back.clicked.connect(self.back)

    def entrance_like_teacher(self):
        pass

    def entrance_like_student(self):
        pass

    def Regist(self):
        uic.loadUi('data/check.ui', self)

        self.btn_like_student.clicked.connect(self.regist_like_student)
        self.btn_like_teacher.clicked.connect(self.regist_like_teacher)
        self.btn_back.clicked.connect(self.back)

    def regist_like_student(self):
        pass

    def regist_like_teacher(self):
        self.reg = Registration_Teacher()
        self.reg.show()


    def back(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = apposition()
    ex.show()
    sys.exit(app.exec())
