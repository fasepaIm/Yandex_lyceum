import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.new_file.clicked.connect(self.new_f)
        self.save_file.clicked.connect(self.save_f)
        self.open_file.clicked.connect(self.open_f)

    def new_f(self):
        self.label.setText('')
        self.editor.setPlainText('')

    def save_f(self):
        self.label.setText('')
        try:
            self.text = open(f'{self.name.text()}', encoding='utf-8', mode='w')
            text_box = [i for i in self.editor.toPlainText().split(r'\n')]
            for i in text_box:
                self.text.write(i)
            self.text.close()
        except FileNotFoundError:
            self.label.setText('Укажите имя файла')

    def open_f(self):
        self.label.setText('')
        try:
            self.text = open(f'{self.name.text()}', encoding='utf-8')
            self.strings = self.text.readlines()
            self.editor.setPlainText('')
            for i in self.strings:
                self.editor.appendPlainText(i.rstrip())
            self.text.close()
        except FileNotFoundError:
            self.label.setText('Файл не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
