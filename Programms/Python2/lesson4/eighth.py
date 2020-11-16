import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLabel, QCheckBox, QVBoxLayout, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Заказ в Макдональдсе')
        self.setFixedSize(350, 400)

        self.buttons = []

        def buttons_factory(name, w, h, button_name):
            name = QCheckBox(button_name, self)
            name.move(w, h)
            name.toggle()
            self.buttons.append(name)
            name.stateChanged.connect(self.hide)

        buttons_factory('cb1', 10, 5, 'Чизбургер')
        buttons_factory('cb2', 10, 35, 'Гамбургер')
        buttons_factory('cb3', 10, 65, 'Кока-кола')
        buttons_factory('cb4', 10, 95, 'Нагетсы')

        self.button1, self.button2, self.button3, self.button4 = 1, 1, 1, 1

        self.button_buy = QPushButton(self)
        self.button_buy.setText('Заказать')
        self.button_buy.move(12, 135)
        self.button_buy.resize(100, 30)
        self.button_buy.clicked.connect(self.buy)

        self.editor = QPlainTextEdit(self)
        #self.editor.insertPlainText('')
        self.editor.move(10, 180)
        self.editor.resize(290, 190)
        self.editor.setEnabled(False)

    def buy(self):
        bob = []
        if self.button1:
                bob.append(self.buttons[0].text())
        if self.button2:
                bob.append(self.buttons[1].text())
        if self.button3:
                bob.append(self.buttons[2].text())
        if self.button4:
                bob.append(self.buttons[3].text())

        self.editor.setPlainText('Ваш заказ:')
        self.editor.appendPlainText('')

        for i in range(len(bob)):
            self.editor.appendPlainText(bob[i])

    def hide(self):
        if self.sender().text() == 'Чизбургер':
            if self.button1 == 1:
                self.button1 = 0
            else:
                self.button1 = 1

        if self.sender().text() == 'Гамбургер':
            if self.button2 == 1:
                self.button2 = 0
            else:
                self.button2 = 1

        if self.sender().text() == 'Кока-кола':
            if self.button3 == 1:
                self.button3 = 0
            else:
                self.button3 = 1

        if self.sender().text() == 'Нагетсы':
            if self.button4 == 1:
                self.button4 = 0
            else:
                self.button4 = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

