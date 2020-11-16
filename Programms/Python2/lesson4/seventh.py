import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber, QRadioButton, QVBoxLayout, QButtonGroup
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')
        self.setFixedSize(320, 400)

        self.label1 = QLabel(self)
        self.label1.setText('')
        self.label1.move(150, 310)

        # Кнопки
        self.radio_button_1 = QRadioButton('X')
        self.radio_button_1.setChecked(True)

        self.radio_button_2 = QRadioButton('0')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)

        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        layout = QVBoxLayout()
        #layout.addWidget(self.label1)
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)

        self.setLayout(layout)

        # Остальное
        self.clicks = ['X']
        self.buttons = []
        self.run = 'X'
        self.first = 'X'
        def button_factory(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            self.buttons.append(name)
            name.clicked.connect(self.clck)

        button_factory('button11', '', 50, 50, 80, 80)
        button_factory('button21', '', 135, 50, 80, 80)
        button_factory('button31', '', 220, 50, 80, 80)
        button_factory('button12', '', 50, 135, 80, 80)
        button_factory('button22', '', 135, 135, 80, 80)
        button_factory('button32', '', 220, 135, 80, 80)
        button_factory('button13', '', 50, 220, 80, 80)
        button_factory('button23', '', 135, 220, 80, 80)
        button_factory('button33', '', 220, 220, 80, 80)

        self.button_game = QPushButton(self)
        self.button_game.setText('Новая игра')
        self.button_game.move(100, 350)
        self.button_game.resize(150, 30)
        self.button_game.clicked.connect(self.new_game)

        self.button11, self.button21, self.button31, self.button12, self.button22, self.button32, self.button13,\
            self.button23, self.button33 = self.buttons[0], self.buttons[1], self.buttons[2], self.buttons[3],\
            self.buttons[4], self.buttons[5], self.buttons[6], self.buttons[7], self.buttons[8]

    def new_game(self):
        for i in self.buttons:
            i.setText('')
            self.label1.setText('')
            self.unblock()
            self.run = self.first

    def _on_radio_button_clicked(self, button):
        if self.clicks[0] != button.text():
            self.clicks[0] = button.text()
            self.run = button.text()
            self.first = button.text()
            self.new_game()

    def block(self):
        for i in self.buttons:
            i.setEnabled(False)

    def unblock(self):
        for i in self.buttons:
            i.setEnabled(True)

    def clck(self):
        if self.sender().text() == '':
            self.sender().setText(self.run)
            if self.run == 'X':
                self.run = '0'
            else:
                self.run = 'X'
        buts = []
        for i in self.buttons:
            buts.append(i.text())
        if len(''.join(buts)) == 9:
            self.label1.setText('Ничья!')
            return 0

        # 1 горизонталь
        if self.button11.text() == self.button21.text() == self.button31.text() != '':
            self.label1.setText(f'Выиграл {self.button21.text()}!')
            self.block()
            return 0

        # 2 горизонталь
        elif self.button12.text() == self.button22.text() == self.button32.text() != '':
            self.label1.setText(f'Выиграл {self.button22.text()}!')
            self.block()
            return 0

        # 3 горизонталь
        elif self.button13.text() == self.button23.text() == self.button33.text() != '':
            self.label1.setText(f'Выиграл {self.button23.text()}!')
            self.block()
            return 0

        # 1 вертикаль
        elif self.button11.text() == self.button12.text() == self.button13.text() != '':
            self.label1.setText(f'Выиграл {self.button12.text()}!')
            self.block()
            return 0

        # 2 вертикаль
        elif self.button21.text() == self.button22.text() == self.button23.text() != '':
            self.label1.setText(f'Выиграл {self.button22.text()}!')
            self.block()
            return 0

        # 3 вертикаль
        elif self.button31.text() == self.button32.text() == self.button33.text() != '':
            self.label1.setText(f'Выиграл {self.button33.text()}!')
            self.block()
            return 0

        # диагональ вл нп
        elif self.button11.text() == self.button22.text() == self.button33.text() != '':
            self.label1.setText(f'Выиграл {self.button22.text()}!')
            self.block()
            return 0

        # диагональ вл нп
        elif self.button31.text() == self.button22.text() == self.button13.text() != '':
            self.label1.setText(f'Выиграл {self.button22.text()}!')
            self.block()
            return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
