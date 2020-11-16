import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clck = 0

    def initUI(self):
        self.setWindowTitle('Вычисление выражений')
        self.setFixedSize(270, 70)

        self.input_label = QLabel(self)
        self.input_label.setText('Выражение:')
        self.input_label.move(10, 10)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 25)
        self.input_value.resize(100, 30)

        self.blink_button = QPushButton(self)
        self.blink_button.setText('->')
        self.blink_button.move(120, 25)
        self.blink_button.resize(30, 30)
        self.blink_button.clicked.connect(self.count)

        self.output_label = QLabel(self)
        self.output_label.setText('Результат:')
        self.output_label.move(160, 10)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.move(160, 25)
        self.output_value.resize(100, 30)

    def count(self):
        self.output_value.setText(str(eval(self.input_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
