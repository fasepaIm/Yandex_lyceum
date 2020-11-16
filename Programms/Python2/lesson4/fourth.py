import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QCheckBox
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Прятки для виджетов')
        self.setFixedSize(450, 145)

        def buttons_factory(name, w, h, button_name):
            name = QCheckBox(button_name, self)
            name.move(w, h)
            name.toggle()
            name.stateChanged.connect(self.hide)

        buttons_factory('cb1', 20, 10, 'edit1')
        buttons_factory('cb2', 20, 40, 'edit2')
        buttons_factory('cb3', 20, 70, 'edit3')
        buttons_factory('cb4', 20, 100, 'edit4')

        self.button1, self.button2, self.button3, self.button4 = 0, 0, 0, 0

        self.first_input_value = QLineEdit(self)
        self.first_input_value.setText('Поле edit1')
        self.first_input_value.move(100, 10)
        self.first_input_value.resize(120, 20)

        self.second_input_value = QLineEdit(self)
        self.second_input_value.setText('Поле edit2')
        self.second_input_value.move(100, 40)
        self.second_input_value.resize(120, 20)

        self.third_input_value = QLineEdit(self)
        self.third_input_value.setText('Поле edit3')
        self.third_input_value.move(100, 70)
        self.third_input_value.resize(120, 20)

        self.fourth_input_value = QLineEdit(self)
        self.fourth_input_value.setText('Поле edit4')
        self.fourth_input_value.move(100, 100)
        self.fourth_input_value.resize(120, 20)

    def hide(self):
        if self.sender().text() == 'edit1':
            if self.button1 == 0:
                self.first_input_value.hide()
                self.button1 = 1
            else:
                self.first_input_value.show()
                self.button1 = 0

        if self.sender().text() == 'edit2':
            if self.button2 == 0:
                self.second_input_value.hide()
                self.button2 = 1
            else:
                self.second_input_value.show()
                self.button2 = 0

        if self.sender().text() == 'edit3':
            if self.button3 == 0:
                self.third_input_value.hide()
                self.button3 = 1
            else:
                self.third_input_value.show()
                self.button3 = 0

        if self.sender().text() == 'edit4':
            if self.button4 == 0:
                self.fourth_input_value.hide()
                self.button4 = 1
            else:
                self.fourth_input_value.show()
                self.button4 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
