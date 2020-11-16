import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber, QRadioButton, QVBoxLayout, QButtonGroup
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setFixedSize(282, 405)

        self.label1 = QLabel(self)
        self.label1.move(1, 0)
        self.label1.resize(282, 30)
        self.label1.setAlignment(Qt.AlignRight)

        self.label2 = QLabel(self)
        self.label2.move(0, 30)
        self.label2.resize(282, 58)
        self.label2.setText('0')
        self.label2.setFont(QtGui.QFont('SansSerif', 28))
        self.label2.setAlignment(Qt.AlignRight)

        self.text_box = ''
        self.big_box = '0'
        self.cleaner = 0

        self.new = 1

        # Кнопки для цифр и точки

        def button_factory_numbers(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            name.clicked.connect(self.numbers)

        button_factory_numbers('button0', '0', 71, 277, 70, 65)
        button_factory_numbers('button1', '1', 1, 214, 70, 65)
        button_factory_numbers('button2', '2', 71, 214, 70, 65)
        button_factory_numbers('button3', '3', 141, 214, 70, 65)
        button_factory_numbers('button4', '4', 1, 151, 70, 65)
        button_factory_numbers('button5', '5', 71, 151, 70, 65)
        button_factory_numbers('button6', '6', 141, 151, 70, 65)
        button_factory_numbers('button7', '7', 1, 89, 70, 65)
        button_factory_numbers('button8', '8', 71, 89, 70, 65)
        button_factory_numbers('button9', '9', 141, 89, 70, 65)
        button_factory_numbers('button_t', '.', 1, 340, 70, 65)

        def button_factory_clear(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            name.clicked.connect(self.cleared)

        # Кнопки C и CE

        button_factory_clear('button_C', 'C', 1, 277, 70, 65)
        button_factory_clear('button_CE', 'CE', 141, 277, 70, 65)

        # Кнопки алгебраических действий

        def button_factory_zn(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            name.clicked.connect(self.count)

        button_factory_zn('button_del', '/', 211, 89, 70, 65)
        button_factory_zn('button_um', '*', 211, 151, 70, 65)
        button_factory_zn('button_min', '-', 211, 214, 70, 65)
        button_factory_zn('button_pl', '+', 211, 277, 70, 65)

        # Кнопка ±

        self.button_pl_min = QPushButton(self)
        self.button_pl_min.setText('±')
        self.button_pl_min.move(71, 340)
        self.button_pl_min.resize(70, 65)
        self.button_pl_min.clicked.connect(self.plus_minus)

        # Кнопка =

        self.button_res = QPushButton(self)
        self.button_res.setText('=')
        self.button_res.move(141, 340)
        self.button_res.resize(140, 65)
        self.button_res.clicked.connect(self.result)

    def numbers(self):
        if self.new == 1 and self.sender().text() != '0' and self.sender().text() != '.' and len(self.big_box) == 1:
            self.new == 0
            self.big_box = ''
            self.label2.setText('')
        if self.sender().text() == '.' and '.' in self.big_box or\
                len(self.big_box) == 0 and self.sender().text() == '.':
            return 0
        if len(self.big_box) == 1 and self.big_box[0] == '0' and self.sender().text() != '.':
            self.big_box = ''
        self.big_box += self.sender().text()
        self.label2.setText(self.big_box)

    def cleared(self):
        if self.sender().text() == 'C':
            self.text_box = ''
            self.label1.setText('')

        self.label2.setText('0')
        self.big_box = '0'
        self.new = 1

    def count(self):
        if self.label2.text() != '-':
            if self.label2.text() or self.sender().text() == '-' or self.label1.text():
                if len(self.text_box) > 0:
                    if not self.text_box[-1].isdigit() and len(self.big_box) == 0:
                        self.text_box = self.text_box[:-1]
                if not self.label1.text() and not self.label2.text() and self.sender().text() == '-':
                    self.big_box = '-'
                    self.label2.setText('-')
                else:
                    self.text_box += self.big_box + self.sender().text()
                    self.label1.setText(self.text_box)
                    self.big_box = ''
                    self.label2.setText('')

    def plus_minus(self):
        if self.label2.text() and self.label2.text() != '.':
            self.big_box = str(float(self.label2.text()) * -1)
            self.label2.setText(str(float(self.label2.text()) * -1))

    def result(self):
        if self.label1.text() and self.label2.text():
            if self.label1.text()[-1] == '/' and self.label2.text() == '0':
                self.label2.setText('НЕЛЬЗЯ!')
                return 0
            self.label1.setText('')
            self.text_box += self.label2.text()
            res = eval(self.text_box)
            if '.' in str(res):
                res = round(res, 5)
            self.label2.setText(str(res))
            self.text_box = ''
            self.big_box = str(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

