import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.setFixedSize(380, 350)
        self.do_paint = False
        self.show_me.clicked.connect(self.color)

    def paint(self):
        # self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def color(self):
        self.colors, self.ok_pressed = QInputDialog.getInt(
            self, "Введите количество цветов", "Сколько цветов?",
            1, 1, 10, 1)
        self.do_paint = True
        self.paint()
        self.do_paint = False

    def draw_flag(self, qp):
        if self.ok_pressed:
            self.y = 90
            for i in range(self.colors):
                qp.setBrush(
                    QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                qp.setPen(QColor(0, 0, 0))
                qp.drawRect(110, self.y, 120, 30)
                self.y += 30


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
