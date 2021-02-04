import sys
import sqlite3


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


SQL_WORDS = ['like', 'in', 'not in', 'not like']


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("films_db.sqlite")
        self.prepare_table()
        self.searchButton.clicked.connect(self.search)


    def prepare_table(self):
        names = [i[1] for i in self.connection.cursor().execute('pragma table_info(films)').fetchall()]
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(names)

    def search(self):
        self.tableWidget.clearContents()
        try:
            if (len(self.year.text()) != 0 and
                    len(self.title.text()) != 0 and len(self.duration.text()) != 0):
                sql = False
                if any(self.title.text().lower().find(i) == 0 for i in SQL_WORDS):
                    sql = True
                if self.year.text().isdigit() and not sql and self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year == {int(self.year.text())} AND title == '{self.title.text()}'
                        AND duration == {int(self.duration.text())}"""

                elif not self.year.text().isdigit() and sql and not self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year {self.year.text()} AND title {self.title.text()}
                        AND duration {self.duration.text()}"""

                elif not self.year.text().isdigit() and not sql and self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films
                        WHERE year {self.year.text()} AND title == '{self.title.text()}'
                        AND duration == {int(self.duration.text())}"""

                elif self.year.text().isdigit() and sql and self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films
                        WHERE year == {int(self.year.text())} AND title {self.title.text()}
                        AND duration == {int(self.duration.text())}"""

                elif self.year.text().isdigit() and not sql and not self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films
                        WHERE year == {int(self.year.text())} AND title == '{self.title.text()}'
                        AND duration {self.duration.text()}"""

                elif not self.year.text().isdigit() and sql and self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year {self.year.text()} AND title {self.title.text()}
                        AND duration == {int(self.duration.text())}"""

                elif not self.year.text().isdigit() and not sql and not self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year {int(self.year.text())} AND title == '{self.title.text()}'
                        AND duration {self.duration.text()}"""

                elif self.year.text().isdigit() and sql and not self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year == {int(self.year.text())} AND title {self.title.text()}
                        AND duration {int(self.duration.text())}"""

            elif len(self.year.text()) != 0 and len(self.title.text()) != 0:
                sql = False
                if any(self.title.text().lower().find(i) == 0 for i in SQL_WORDS):
                    sql = True
                if self.year.text().isdigit():
                    if not sql:
                        query = f"""SELECT * FROM Films 
                            WHERE year == {int(self.year.text())} AND title == '{self.title.text()}'"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE year == {int(self.year.text())} AND title {self.title.text()}"""
                else:
                    if not sql:
                        query = f"""SELECT * FROM Films 
                            WHERE year {self.year.text()} AND title == '{self.title.text()}'"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE year {self.year.text()} AND title {self.title.text()}"""

            elif len(self.year.text()) != 0 and len(self.duration.text()) != 0:
                if self.year.text().isdigit():
                    if self.duration.text().isdigit():
                        query = f"""SELECT * FROM Films 
                            WHERE year == {int(self.year.text())} AND duration == {int(self.duration.text())}"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE year == {int(self.year.text())} AND duration {self.duration.text()}"""
                else:
                    if self.duration.text().isdigit():
                        query = f"""SELECT * FROM Films 
                            WHERE year {self.year.text()} AND duration == {int(self.duration.text())}"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE year {self.year.text()} AND duration {self.duration.text()}"""

            elif len(self.title.text()) != 0 and len(self.duration.text()) != 0:
                sql = False
                if any(self.title.text().lower().find(i) == 0 for i in SQL_WORDS):
                    sql = True
                if not sql:
                    if self.duration.text().isdigit():
                        query = f"""SELECT * FROM Films 
                            WHERE title == '{self.title.text()}' AND duration == {int(self.duration.text())}"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE title == '{self.title.text()}' AND duration {self.duration.text()}"""
                else:
                    if self.duration.text().isdigit():
                        query = f"""SELECT * FROM Films 
                            WHERE title {self.title.text()} AND duration == {int(self.duration.text())}"""
                    else:
                        query = f"""SELECT * FROM Films 
                            WHERE title {self.title.text()} AND duration {self.duration.text()}"""

            elif len(self.year.text()) != 0:
                if self.year.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE year == {int(self.year.text())}"""
                else:
                    query = f"""SELECT * FROM Films 
                        WHERE year {self.year.text()}"""

            elif len(self.title.text()) != 0:
                sql = False
                if any(self.title.text().lower().find(i) == 0 for i in SQL_WORDS):
                    sql = True
                if not sql:
                    query = f"""SELECT * FROM Films
                        WHERE title == '{self.title.text()}'"""
                else:
                    query = f"""SELECT * FROM Films
                        WHERE title {self.title.text()}"""

            elif len(self.duration.text()) != 0:
                if self.duration.text().isdigit():
                    query = f"""SELECT * FROM Films 
                        WHERE duration == {int(self.duration.text())}"""
                else:
                    query = f"""SELECT * FROM Films 
                        WHERE duration {self.duration.text()}"""

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

        except Exception:
            self.statusBar().showMessage('Неверный формат ввода')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
