import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('films_db.sqlite')
        self.buttonGroup.buttonClicked.connect(self.search)

    def search(self, event):
        query = f"""SELECT * FROM Films 
                WHERE title LIKE '{event.text()}%'"""
        result = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setRowCount(0)
        if len(result) == 0:
            self.statusBar().showMessage('К сожалению, ничего не нашлось')
        else:
            self.statusBar().showMessage(f'Нашлось {len(result)} записей')
            for i, row in enumerate(result):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
