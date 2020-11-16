import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Фокус со словами')
        self.setFixedSize(270, 70)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(100, 30)

        self.blink_button = QPushButton(self)
        self.blink_button.setText('->')
        self.blink_button.move(120, 10)
        self.blink_button.resize(30, 30)
        self.blink_button.clicked.connect(self.fly)

        self.output_value = QLineEdit(self)
        self.output_value.move(160, 10)
        self.output_value.resize(100, 30)

    def fly(self):
        if self.clck == 0:
            self.output_value.setText(self.input_value.text())
            self.input_value.setText('')
            self.blink_button.setText('<-')
            self.clck = 1
        else:
            self.input_value.setText(self.output_value.text())
            self.output_value.setText('')
            self.blink_button.setText('->')
            self.clck = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
