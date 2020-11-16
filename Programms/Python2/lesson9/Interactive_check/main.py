import csv
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.loadTable('Data.csv')
        self.tableWidget.cellChanged.connect(self.result)

    def loadTable(self, table_name):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader) + ['Количество']
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                row[-1] = '0'
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def result(self):
        price = 0
        for i in range(self.tableWidget.rowCount()):
            price += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.price.setText(str(price))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
