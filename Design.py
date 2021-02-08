import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from check_teacher import Check_teacher
from chech_entrance import Check_entrance


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
        self.ch = Check_entrance()
        self.ch.show()

    def Regist(self):
        self.ch = Check_teacher()
        self.ch.show()

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
