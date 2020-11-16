import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Ним наносит ответный удар')
        self.setFixedSize(300, 300)

        self.end_game = 0

        self.result_label = QLabel(self)
        self.result_label.setText('')
        self.result_label.move(0, 0)
        self.result_label.hide()

        self.plus_button = QPushButton(self)
        self.plus_button.setText(f'+{random.randint(1, 10)}')
        self.plus_button.move(30, 55)
        self.plus_button.resize(100, 30)
        self.plus_button.clicked.connect(self.count)

        self.minus_button = QPushButton(self)
        self.minus_button.setText(f'{random.randint(-10, -1)}')
        self.minus_button.move(170, 55)
        self.minus_button.resize(100, 30)
        self.minus_button.clicked.connect(self.count)

        self.first_label = QLabel(self)
        self.first_label.setText('Осталось ходов')
        self.first_label.move(15, 100)

        self.second_label = QLabel(self)
        self.second_label.setText('Текущее число')
        self.second_label.move(15, 150)

        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.display('10')
        self.LCD_count1.move(190, 100)
        self.LCD_count1.resize(70, 20)

        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.display(random.randint(1, 50))
        self.LCD_count2.move(190, 150)
        self.LCD_count2.resize(70, 20)

    def new_game(self):
        self.end_game = 1
        self.plus_button.setText(f'+{random.randint(1, 10)}')
        self.minus_button.setText(f'{random.randint(-10, -1)}')
        self.LCD_count1.display(10)
        self.LCD_count2.display(random.randint(1, 50))
        self.result_label.show()

    def count(self):
        if self.end_game == 1:
            self.result_label.setText('')
            self.result_label.hide()

        if self.LCD_count1.value() > 1:
            if eval(f'{self.LCD_count2.value()}{self.sender().text()}') != 0:
                self.LCD_count1.display(self.LCD_count1.value() - 1)
                self.LCD_count2.display(eval(f'{self.LCD_count2.value()}{self.sender().text()}'))
            else:
                self.result_label.setText('Вы победили, начинаем новую игру')
                self.new_game()
        else:
            if eval(f'{self.LCD_count2.value()}{self.sender().text()}') != 0:
                    self.result_label.setText('Вы проиграли, начинаем новую игру')
                    self.new_game()
            else:
                self.result_label.setText('Вы победили, начинаем новую игру')
                self.new_game()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

