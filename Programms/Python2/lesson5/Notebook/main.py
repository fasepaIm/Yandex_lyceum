import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('note.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.write)

    def write(self):
        self.listWidget.addItem(f'{self.lineEdit.text()} {self.lineEdit_2.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
