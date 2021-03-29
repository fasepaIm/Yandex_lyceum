import sys
import os
import requests

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


SCREEN_SIZE = [600, 450]


class MapScreen(QMainWindow):
    def __init__(self, x_line, y_line, scales_line):
        super().__init__()
        self.x_line = x_line
        self.y_line = y_line
        self.scales_line = scales_line
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        self.getImage()
        self.show_map()

    def getImage(self):
        search_api_server = "https://static-maps.yandex.ru/1.x/"
        api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

        address_ll = ','.join([self.y_line, self.x_line])
        z = self.scales_line
        if not z:
            z = "0"

        self.search_params = {
            "ll": address_ll,
            "l": "map",
            "z": z
        }
        response = requests.get(search_api_server, params=self.search_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)


    def show_map(self):
        # Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if not self.scales_line:
            self.scales_line = "0"
        if event.key() == Qt.Key_PageUp:
            if int(self.scales_line) < 17:
                self.scales_line = int(self.scales_line) + 1
        elif event.key() == Qt.Key_PageDown:
            if int(self.scales_line) > 0:
                self.scales_line = int(self.scales_line) - 1
        os.remove(self.map_file)
        self.getImage()
        self.show_map()


    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.show_map_button.clicked.connect(self.show_map)

    def show_map(self):
        self.window = MapScreen(self.x_line.text(), self.y_line.text(), self.scales_line.text())
        self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
