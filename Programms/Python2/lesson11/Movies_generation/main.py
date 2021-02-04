import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("films_db.sqlite")
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemClicked.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.change_results)
        self.result = []
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM films WHERE id=?",
                             (item_id := self.plainTextEdit.toPlainText().split()[-1], )).fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.result = []

    def item_changed(self, item):
        self.tableWidget.selectRow(item.row())
        self.id = self.tableWidget.item(0, 0).text()
        cur = self.con.cursor()
        self.result = cur.execute("SELECT * FROM films WHERE id=?",
                            (item_id := self.id, )).fetchall()

    def change_results(self):
        if self.result:
            valid = QMessageBox.question(
                self, '', "Действительно заменить элементы с id " + ",".join(self.id),
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                que = f"""UPDATE films SET
                        title = '{self.result[0][1][::-1]}',
                        year = '{self.result[0][2] + 1000}',
                        duration = {self.result[0][-1] * 2} """
                que += "WHERE id = ?"
                cur.execute(que, (self.id,))
                self.con.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
