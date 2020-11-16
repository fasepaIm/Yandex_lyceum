import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import sqrt, factorial


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.text_box = ''
        self.big_box = '0'
        self.new = 0

        self.btn0.clicked.connect(self.numbers)
        self.btn1.clicked.connect(self.numbers)
        self.btn2.clicked.connect(self.numbers)
        self.btn3.clicked.connect(self.numbers)
        self.btn4.clicked.connect(self.numbers)
        self.btn5.clicked.connect(self.numbers)
        self.btn6.clicked.connect(self.numbers)
        self.btn7.clicked.connect(self.numbers)
        self.btn8.clicked.connect(self.numbers)
        self.btn9.clicked.connect(self.numbers)
        self.btn_dot.clicked.connect(self.numbers)
        self.btn_clear.clicked.connect(self.maid)
        self.btn_plus.clicked.connect(self.count)
        self.btn_minus.clicked.connect(self.count)
        self.btn_mult.clicked.connect(self.count)
        self.btn_div.clicked.connect(self.count)
        self.btn_pow.clicked.connect(self.count)
        self.btn_sqrt.clicked.connect(self.sqrt_f)
        self.btn_eq.clicked.connect(self.result)
        self.btn_fact.clicked.connect(self.fact_f)

    def fact_f(self):
        if self.table.value() < 0:
            self.table.display('ERROR')
        else:
            self.big_box = factorial(self.table.value())
            self.table.display(self.big_box)
        self.new = 1

    def sqrt_f(self):
        if str(self.table.value())[0].isdigit() and self.table.value() >= 0 and len(self.big_box) != '0':
            if self.table.value() == 0:
                self.big_box = '0'
            else:
                res = sqrt(self.table.value())
                if '.' in str(res):
                    res = round(res, 1)
                self.big_box = str(res)
            self.table.display(self.big_box)
        else:
           self.table.display('ERROR')
        self.new = 1

    def numbers(self):
        if self.new == 1:
            self.table.display('')
            self.big_box = ''
            self.new = 0
        if len(self.big_box) == 1 and self.big_box[0] == '0':
            if self.sender().text() == '0':
                return 0
            else:
                if self.sender().text() != '.':
                    self.big_box = ''
        if self.sender().text() == '.':
            if '.' in self.big_box:
                return 0
            else:
                self.big_box += self.sender().text()
                self.table.display(self.big_box)
                return 0
        self.big_box += self.sender().text()
        self.table.display(self.big_box)

    def maid(self):
        self.text_box = ''
        self.table.display(0)
        self.big_box = '0'

    def count(self):
        if self.big_box != '-':
            if self.sender().text() == '-' or self.big_box or self.text_box:
                x = self.sender().text()
                if x == '^':
                    x = '**'
                if len(self.text_box) > 0:
                    if not self.text_box[-1].isdigit():
                        if x == '**':
                            self.text_box = self.text_box[:-2]
                        else:
                            self.text_box = self.text_box[:-1]
                if not self.text_box and self.big_box == '0' and x == '-':
                    self.big_box = '-'
                    self.table.display(self.big_box)
                else:
                    self.text_box = str(self.table.value()) + x
                    self.big_box = ''
                    self.new = 1

    def result(self):
        if self.text_box and self.table.value() != '':
            if self.text_box[-1] == '/' and self.big_box == '0':
                self.table.display('ERROR')
                return 0
            self.text_box += self.big_box
            res = eval(self.text_box)
            if '.' in str(res):
                res = round(res, 1)
            self.table.display(res)
            self.text_box = ''
            self.big_box = str(res)
            self.new = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
