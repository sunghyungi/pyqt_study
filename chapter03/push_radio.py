from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QHeaderView


class PushRadioUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("push_radio_btns.ui")
        self.ui.show()
        self.ui.btn_OK.pressed.connect(self.clickshow)
        self.ui.btn_Cancel.pressed.connect(self.clickshow2)
        self.ui.Man.clicked.connect(self.checkshow)
        self.ui.Woman.clicked.connect(self.checkshow2)
        self.tbl_widget = self.ui.tableWidget
        self.tbl_widget.setItem(0, 0, QTableWidgetItem("cell(0,0)"))

        item = QTableWidgetItem("cell(0,1)")
        item.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(0,1,item)

        item2 = QTableWidgetItem("cell(0,2)")
        item2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tbl_widget.setItem(0, 2, item2)

        table_header = ["첫번째", "두번째", "세번째"]
        self.tbl_widget.setHorizontalHeaderLabels(table_header)


        self.ui.btn_del.clicked.connect(self.tbl_del_item)

        self.ui.btn_input.clicked.connect(self.input_tble_item)

        # row 단위 선택
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 수정 불가능 하게
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일한 간격으로 재배치
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def tbl_del_item(self):
        selectionIdx = self.tbl_widget.selectedIndexes()[0]
        print(selectionIdx.row(), " ", selectionIdx.column())
        self.tbl_widget.removeRow(selectionIdx.row())

    def input_tble_item(self):
        item = QTableWidgetItem("cell(0,1)")
        item.setTextAlignment(Qt.AlignCenter)
        currentRowCount = self.tbl_widget.rowCount()
        self.tbl_widget.insertRow(currentRowCount)
        v1 = self.ui.le_01.text()
        v2 = self.ui.le_02.text()
        v3 = self.ui.le_03.text()

        item01 = QTableWidgetItem(v1)
        item01.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(currentRowCount, 0, item01)
        self.tbl_widget.setItem(currentRowCount, 1, QTableWidgetItem(v2))
        self.tbl_widget.setItem(currentRowCount, 2, QTableWidgetItem(v3))


    def clickshow(self):
        self.ui.lbl_push_res.setText(self.ui.btn_OK.text())

    def clickshow2(self):
        self.ui.lbl_push_res.setText(self.ui.btn_Cancel.text())

    def checkshow(self):
        self.ui.lbl_rb_res.setText(self.ui.Man.text())

    def checkshow2(self):
        self.ui.lbl_rb_res.setText(self.ui.Woman.text())


if __name__ == "__main__":
    app = QApplication([])
    w = PushRadioUI()
    app.exec_()