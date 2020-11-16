import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLabel, QCheckBox, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Заказ в Макдональдсе - 2')
        self.setFixedSize(350, 400)

        # Цена еды
        self.Cheeseburger = 150
        self.Hamburger = 200
        self.Coca_cola = 50
        self.Nuggets = 100

        # Чекбоксы
        self.buttons = []

        def buttons_factory(name, w, h, button_name):
            name = QCheckBox(button_name, self)
            name.move(w, h)
            self.buttons.append(name)
            name.stateChanged.connect(self.click)

        buttons_factory('cb1', 10, 5, 'Чизбургер')
        buttons_factory('cb2', 10, 35, 'Гамбургер')
        buttons_factory('cb3', 10, 65, 'Кока-кола')
        buttons_factory('cb4', 10, 95, 'Нагетсы')

        self.button1, self.button2, self.button3, self.button4 = 0, 0, 0, 0

        # количество товара
        self.first_input_value = QLineEdit(self)
        self.first_input_value.setText('0')
        self.first_input_value.move(120, 5)
        self.first_input_value.resize(30, 20)
        self.first_input_value.setEnabled(False)

        self.second_input_value = QLineEdit(self)
        self.second_input_value.setText('0')
        self.second_input_value.move(120, 35)
        self.second_input_value.resize(30, 22)
        self.second_input_value.setEnabled(False)

        self.third_input_value = QLineEdit(self)
        self.third_input_value.setText('0')
        self.third_input_value.move(120, 65)
        self.third_input_value.resize(30, 22)
        self.third_input_value.setEnabled(False)

        self.fourth_input_value = QLineEdit(self)
        self.fourth_input_value.setText('0')
        self.fourth_input_value.move(120, 95)
        self.fourth_input_value.resize(30, 22)
        self.fourth_input_value.setEnabled(False)

        # кнопка заказа

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
        end1 = int(self.first_input_value.text()) * self.Cheeseburger
        if self.button1:
            bob.append(f'{self.buttons[0].text()}----{self.first_input_value.text()}----{str(end1)}')
        end2 = int(self.second_input_value.text()) * self.Hamburger
        if self.button2:
            bob.append(f'{self.buttons[1].text()}----{self.second_input_value.text()}----{str(end2)}')
        end3 = int(self.third_input_value.text()) * self.Coca_cola
        if self.button3:
            bob.append(f'{self.buttons[2].text()}----{self.third_input_value.text()}----{str(end3)}')
        end4 = int(self.fourth_input_value.text()) * self.Nuggets
        if self.button4:
            bob.append(f'{self.buttons[3].text()}----{self.fourth_input_value.text()}----{str(end4)}')

        self.editor.setPlainText('Ваш заказ:')
        self.editor.appendPlainText('')

        for i in range(len(bob)):
            self.editor.appendPlainText(bob[i])

        self.editor.appendPlainText('')
        self.editor.appendPlainText(f'Итого: {end1 + end2 + end3 + end4}')

    def click(self):
        if self.sender().text() == 'Чизбургер':
            if self.button1 == 1:
                self.button1 = 0
                self.first_input_value.setEnabled(False)
                self.first_input_value.setText('0')
            else:
                self.button1 = 1
                self.first_input_value.setEnabled(True)
                self.first_input_value.setText('1')

        if self.sender().text() == 'Гамбургер':
            if self.button2 == 1:
                self.button2 = 0
                self.second_input_value.setEnabled(False)
                self.second_input_value.setText('0')
            else:
                self.button2 = 1
                self.second_input_value.setEnabled(True)
                self.second_input_value.setText('1')

        if self.sender().text() == 'Кока-кола':
            if self.button3 == 1:
                self.button3 = 0
                self.third_input_value.setEnabled(False)
                self.third_input_value.setText('0')
            else:
                self.button3 = 1
                self.third_input_value.setEnabled(True)
                self.third_input_value.setText('1')

        if self.sender().text() == 'Нагетсы':
            if self.button4 == 1:
                self.button4 = 0
                self.fourth_input_value.setEnabled(False)
                self.fourth_input_value.setText('0')
            else:
                self.button4 = 1
                self.fourth_input_value.setEnabled(True)
                self.fourth_input_value.setText('1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


