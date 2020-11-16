import sys
from PIL import Image, ImageQt

from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        # Изображение
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.im = Image.open(self.fname)
        self.pixmap = QPixmap(self.fname)
        self.label.setPixmap(self.pixmap)
        self.transparency_slider.valueChanged.connect(self.transparency)

    def transparency(self):
        self.im.putalpha(self.transparency_slider.value())
        #myQtImage = ImageQt.ImageQt(self.im)
        #pixmap = QtGui.QPixmap.fromImage(myQtImage)
        pixmap = ImageQt.toqpixmap(self.im)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
