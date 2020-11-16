import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)
        self.flag = ['Синий', 'Синий', 'Синий']
        self.buttonGroup.buttonClicked.connect(self.first_colour)
        self.buttonGroup_2.buttonClicked.connect(self.second_colour)
        self.buttonGroup_3.buttonClicked.connect(self.third_colour)
        self.pushButton.clicked.connect(self.make_flag)

    def first_colour(self, button):
        self.flag[0] = button.text()

    def second_colour(self, button):
        self.flag[1] = button.text()

    def third_colour(self, button):
        self.flag[2] = button.text()

    def make_flag(self):
        self.label.setText(f'Цвета: {self.flag[0]}, {self.flag[1]} и {self.flag[2]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
