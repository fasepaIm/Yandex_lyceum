import sys
import random
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.random_return)

    def random_return(self):
        with open('lines.txt', encoding='utf-8') as opened_file:
            if os.path.getsize('lines.txt') > 0:
                self.textBrowser.setPlainText(random.choice(opened_file.readlines()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
