import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        #self.setFixedSize(670, 500)
        self.coeff = self.smile_size.value()
        self.smile_size.valueChanged.connect(self.smile)

    def paint(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_smile(qp)
        qp.end()

    def smile(self):
        self.coeff = self.smile_size.value()
        self.paint()

    def draw_smile(self, qp):
        size = 9 * self.coeff
        qp.setPen(QColor(255, 51, 102))
        qp.drawEllipse(0, 0, size, size)
        qp.drawEllipse(int(size / 5), int(size / 5), int(size / 5), int(size / 5))
        qp.drawEllipse(int(size / 1.655), int(size / 5), int(size / 5), int(size / 5))
        qp.drawArc(int(size / 4.3), int(size / 1.55), int(size / 1.8), int(size / 5.63), -30 * 16, -120 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

