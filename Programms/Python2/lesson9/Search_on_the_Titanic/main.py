import csv
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.loadTable('titanic.csv', 0)
        self.lineEdit.textChanged.connect(self.search)

    def search(self):
        if len(self.lineEdit.text()) >= 3:
            self.loadTable('titanic.csv', 1)
        else:
            self.loadTable('titanic.csv', 0)

    def loadTable(self, table_name, search_code):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            if search_code == 0:
                for i, row in enumerate(reader):
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(elem))
                    if row[-2] == '1':
                        self.color_row(i, QColor(0, 255, 0))
                    else:
                        self.color_row(i, QColor(255, 0, 0))
            else:
                i = 0
                for row in reader:
                    if self.lineEdit.text().lower() in row[1].lower():
                        self.tableWidget.setRowCount(
                            self.tableWidget.rowCount() + 1)
                        for j, elem in enumerate(row):
                            self.tableWidget.setItem(
                                i, j, QTableWidgetItem(elem))
                        if row[-2] == '1':
                            self.color_row(i, QColor(0, 255, 0))
                        else:
                            self.color_row(i, QColor(255, 0, 0))
                        i += 1
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
