import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        self.rocks = 0
        super().__init__()
        uic.loadUi('alias.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.input1)
        self.pushButton_2.clicked.connect(self.result)

    def input1(self):
        self.rocks = self.spinBox.value()
        self.lcdNumber.display(self.spinBox.value())
        self.label_3.setText('')
        self.listWidget.clear()
        self.spinBox_2.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        win = 0

    def result(self):
        self.rocks -= self.spinBox_2.value()
        self.lcdNumber.display(self.rocks)
        self.listWidget.addItem(f'Игрок взял - {self.spinBox_2.value()}')
        if self.rocks == 0:
            self.label_3.setText('Победа игрока!')
            self.block()
            win = 1
        else:
            if self.rocks % 4 == 0:
                self.rocks -= 1
                self.listWidget.addItem('Компьютер взял - 1')
            else:
                get = self.rocks % 4
                self.rocks -= get
                self.listWidget.addItem(f'Компьютер взял - {get}')
            if self.rocks == 0:
                self.label_3.setText('Победа компьютера!')
                self.block()
                win = 1
            self.lcdNumber.display(self.rocks)

    def block(self):
        self.spinBox_2.setEnabled(False)
        self.pushButton_2.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
