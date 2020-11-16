import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('wid.ui', self)  # Загружаем дизайн
        self.art()

    def art(self):
        print('Введите значения ячеек в формате 10x10')
        count = []
        for i in range(10):
            count.append(input().split())
        for x in range(10):
            for y in range(10):
                if count[x][y] == '1':
                    s = eval(f'self.pushButton_{y}{x}')
                    s.setText('*')
                else:
                    s = eval(f'self.pushButton_{y}{x}')
                    s.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
