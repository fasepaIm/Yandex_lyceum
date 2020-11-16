import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Арифмометр')
        self.setFixedSize(300, 65)

        self.first_input_value = QLineEdit(self)
        self.first_input_value.setText('0')
        self.first_input_value.move(5, 5)
        self.first_input_value.resize(60, 30)

        self.second_input_value = QLineEdit(self)
        self.second_input_value.setText('0')
        self.second_input_value.move(154, 5)
        self.second_input_value.resize(60, 30)

        self.result_output_value = QLineEdit(self)
        self.result_output_value.setText('0')
        self.result_output_value.setEnabled(False)
        self.result_output_value.move(225, 5)
        self.result_output_value.resize(60, 30)

        self.label1 = QLabel(self)
        self.label1.setText('=')
        self.label1.move(215, 14)

        def button_factory(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            name.clicked.connect(self.count)

        button_factory('button1', '+', 67, 6, 27, 27)
        button_factory('button2', '-', 96, 6, 27, 27)
        button_factory('button3', '*', 125, 6, 27, 27)

    def count(self):
        if self.sender().text() == '+':
            self.result_output_value.setText(str(int(self.first_input_value.text()) + int(self.second_input_value.text())))
        if self.sender().text() == '-':
            self.result_output_value.setText(str(int(self.first_input_value.text()) - int(self.second_input_value.text())))
        if self.sender().text() == '*':
            self.result_output_value.setText(str(int(self.first_input_value.text()) * int(self.second_input_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

