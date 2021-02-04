import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('films_db.sqlite')
        self.load_genres()
        self.filtrationButton.clicked.connect(self.filter)

    def filter(self):
        query = f"""SELECT * FROM Films 
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == '{self.comboBox.currentText()}')"""
        result = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j in range(0, 3):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(row[j + 1])))

    def load_genres(self):
        query = """SELECT title FROM genres"""
        result = [i[0] for i in self.connection.cursor().execute(query).fetchall()]
        self.comboBox.addItems(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

