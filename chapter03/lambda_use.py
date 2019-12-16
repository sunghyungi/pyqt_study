from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class LambdaUse(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("lambda_use.ui")
        self.ui.show()
        self.ui.btn_ok.clicked.connect(lambda stat, button=self.ui.btn_ok: self.showLabel(stat, button))
        self.ui.btn_yes.pressed.connect(lambda text=self.ui.btn_yes.text(): self.showLabelText(text))

    def showLabelText(self, text):
        QMessageBox.information(self, 'btn', text, QMessageBox.Ok)
        self.ui.lbl_res.setText(text)

    def showLabel(self, stat, btn):
        message = btn.text()
        QMessageBox.information(self, 'btn', message, QMessageBox.Ok)
        self.ui.lbl_res.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    w = LambdaUse()
    app.exec_()