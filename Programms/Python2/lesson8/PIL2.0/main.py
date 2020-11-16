import sys
from PIL import Image, ImageQt

from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.setFixedSize(610, 465)
        # Изображение
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.im = Image.open(self.fname)
        self.routate_img = Image.open(self.fname)
        self.pixmap = QPixmap(self.fname)
        self.label.setPixmap(self.pixmap)
        self.buttonGroup.buttonClicked.connect(self.rgb)
        self.buttonGroup_2.buttonClicked.connect(self.routate_im)

    def rgb(self, but):
        name = but.text()
        if but.text() == 'ALL':
            self.im = self.routate_img.copy()
        else:
            self.im = self.routate_img.copy()
            pixels = self.im.load()
            x, y = self.im.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j][0:3]
                    if name == 'R':
                        pixels[i, j] = r, 0, 0
                    elif name == 'G':
                        pixels[i, j] = 0, g, 0
                    else:
                        pixels[i, j] = 0, 0, b
        #myQtImage = ImageQt.ImageQt(self.im)
        #pixmap = QtGui.QPixmap.fromImage(myQtImage)
        pixmap = ImageQt.toqpixmap(self.im)
        self.label.setPixmap(pixmap)

    def routate_im(self, but):
        if but.text() == 'По часовой стрелке':
            self.im = self.im.transpose(Image.ROTATE_270)
            self.routate_img = self.routate_img.transpose(Image.ROTATE_270)
        if but.text() == 'Против часовой стрелки':
            self.im = self.im.transpose(Image.ROTATE_90)
            self.routate_img = self.routate_img.transpose(Image.ROTATE_90)
        #myQtImage = ImageQt.ImageQt(self.im)
        #pixmap = QtGui.QPixmap.fromImage(myQtImage)
        pixmap = ImageQt.toqpixmap(self.im)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
