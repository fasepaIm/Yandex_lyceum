import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('films_db.sqlite')
        self.searchButton.clicked.connect(self.search)

    def search(self):
        selected_value = self.comboBox.currentText()
        self.statusBar().showMessage('')
        self.id.clear()
        self.title.clear()
        self.year.clear()
        self.genre.clear()
        self.duration.clear()

        try:
            if selected_value == 'Год выпуска':
                query = f"""SELECT * FROM Films 
                    WHERE year == {int(self.lineEdit.text())}"""
            elif selected_value == 'Продолжительность':
                query = f"""SELECT * FROM Films 
                    WHERE duration == {int(self.lineEdit.text())}"""
            elif selected_value == 'Название':
                query = f"""SELECT * FROM Films 
                    WHERE title == '{self.lineEdit.text()}'"""
            result = self.connection.cursor().execute(query).fetchone()
            if result:
                self.id.setText(str(result[0]))
                self.title.setText(str(result[1]))
                self.year.setText(str(result[2]))
                self.genre.setText(str(result[3]))
                self.duration.setText(str(result[4]))
            else:
                self.statusBar().showMessage('Ничего не найдено')
        except Exception:
            self.statusBar().showMessage('Неправильный запрос')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
