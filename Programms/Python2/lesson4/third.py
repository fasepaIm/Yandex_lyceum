import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Миникалькулятор')
        self.setFixedSize(450, 145)

        self.first_input_label = QLabel(self)
        self.first_input_label.setText('Первое число(целое):')
        self.first_input_label.move(10, 10)

        self.first_input_value = QLineEdit(self)
        self.first_input_value.move(10, 25)
        self.first_input_value.resize(120, 20)

        self.second_input_label = QLabel(self)
        self.second_input_label.setText('Второе число(целое):')
        self.second_input_label.move(10, 80)

        self.second_input_value = QLineEdit(self)
        self.second_input_value.move(10, 95)
        self.second_input_value.resize(120, 20)

        self.blink_button = QPushButton(self)
        self.blink_button.setText('->')
        self.blink_button.move(155, 45)
        self.blink_button.resize(100, 30)
        self.blink_button.clicked.connect(self.count)

        self.LCD_count1_label = QLabel(self)
        self.LCD_count1_label.setText('Сумма:')
        self.LCD_count1_label.move(290, 20)

        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(335, 10)
        self.LCD_count1.resize(105, 30)

        self.LCD_count2_label = QLabel(self)
        self.LCD_count2_label.setText('Разность:')
        self.LCD_count2_label.move(266, 53)

        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(335, 42)
        self.LCD_count2.resize(105, 30)

        self.LCD_count3_label = QLabel(self)
        self.LCD_count3_label.setText('Произведение:')
        self.LCD_count3_label.move(235, 86)

        self.LCD_count3 = QLCDNumber(self)
        self.LCD_count3.move(335, 74)
        self.LCD_count3.resize(105, 30)

        self.LCD_count4_label = QLabel(self)
        self.LCD_count4_label.setText('Частное:')
        self.LCD_count4_label.move(274, 119)

        self.LCD_count4 = QLCDNumber(self)
        self.LCD_count4.move(335, 106)
        self.LCD_count4.resize(105, 30)

    def count(self):
        self.LCD_count1.display(int(self.first_input_value.text()) + int(self.second_input_value.text()))

        self.LCD_count2.display(int(self.first_input_value.text()) - int(self.second_input_value.text()))

        self.LCD_count3.display(int(self.first_input_value.text()) * int(self.second_input_value.text()))

        if int(self.second_input_value.text()) == 0:
            self.LCD_count4.display('Error')
        else:
            self.LCD_count4.display(int(self.first_input_value.text()) / int(self.second_input_value.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
