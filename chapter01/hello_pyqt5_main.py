import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic

from chapter01 import chap01, hello_pyqt5


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("hello_pyqt5.ui")
        self.ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_pyqt5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # app = QtWidgets.QApplication(sys.argv)
    # w = MyApp()
    # sys.exit(app.exec())

