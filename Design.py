import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from enter_or_reg import enter_or_regist


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
        uic.loadUi('', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.zapusk = enter_or_regist()
        self.zapusk.show()

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
