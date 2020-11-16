import csv
import sys
import random

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QSizePolicy, QHeaderView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.loadTable('Data.csv')
        self.tableWidget.cellChanged.connect(self.result)
        self.update.clicked.connect(self.up)

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
                    if elem.isdigit() and elem != '0':
                        self.tableWidget.setItem(
                          i, j, QTableWidgetItem(f'     {elem}'[-5:]))
                    else:
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(elem))
        self.tableWidget.sortItems(1, QtCore.Qt.DescendingOrder)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.draw()

    def up(self):
        self.draw()
        self.result()

    def draw(self):
        for i in range(5):
            self.color_row(i, QColor(random.randint(0, 255), 
                           random.randint(0, 255),  random.randint(0, 255)))

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

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

