import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.mix)

    def mix(self):
        self.plainTextEdit.setPlainText('')
        with open('text.txt', encoding='utf-8') as text:
            string = text.readlines()
            for i in range(0, len(string), 2):
                self.plainTextEdit.appendPlainText(string[i].rstrip())
            for i in range(1, len(string), 2):
                self.plainTextEdit.appendPlainText(string[i].rstrip())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
