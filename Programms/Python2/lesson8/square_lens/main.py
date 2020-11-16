import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class BigCoeff(Exception):
    pass


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.setFixedSize(460, 480)
        self.do_paint = False
        self.show_me.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        try:
            if float(self.coeff.text()) <= 1:
                self.errors.setText('')
                pen = QPen(Qt.red)
                qp.setPen(pen)
                x, y = 230, 300
                side = int(self.side.text())
                for i in range(int(self.nn.text())):
                    qp.drawLine(x - (side // 2), y - (side // 2), x + (side // 2), y - (side // 2))
                    qp.drawLine(x + (side // 2), y - (side // 2), x + (side // 2), y + (side // 2))
                    qp.drawLine(x - (side // 2), y + (side // 2), x + (side // 2), y + (side // 2))
                    qp.drawLine(x - (side // 2), y + (side // 2), x - (side // 2), y - (side // 2))
                    side *= float(self.coeff.text())
            else:
                raise BigCoeff()

        except ValueError:
            self.errors.setText('Некорректный ввод')

        except BigCoeff:
            self.errors.setText('Коэффициент больше 1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
