import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Азбука Морзе 2')
        self.setFixedSize(300, 90)

        self.first_input_value = QLineEdit(self)
        self.first_input_value.move(5, 47)
        self.first_input_value.resize(270, 22)

        def button_factory(name, text, mov1, mov2, res1, res2):
            name = QPushButton(self)
            name.setText(text)
            name.move(mov1, mov2)
            name.resize(res1, res2)
            name.clicked.connect(self.comeback)

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        mov11, mov22 = 5, 5

        for i in range(26):
            if i <= 12:
                button_factory(f'button_{letters[i]}', letters[i], mov11, 5, 20, 20)
                mov11 += 21
            else:
                button_factory(f'button_{letters[i]}', letters[i], mov22, 26, 20, 20)
                mov22 += 21

    def comeback(self):
        morze = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--','z': '--..'
        }
        self.first_input_value.setText(
            self.first_input_value.text() + morze[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
