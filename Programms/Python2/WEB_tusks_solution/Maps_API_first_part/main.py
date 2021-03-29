import sys
import os
import requests

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


SCREEN_SIZE = [600, 450]


class MapScreen(QMainWindow):
    def __init__(self, map_file):
        super().__init__()
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        self.map_file = map_file
        self.show_map()

    def show_map(self):
        # Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.show_map_button.clicked.connect(self.show_map)

    def show_map(self):
        self.getImage()
        self.window = MapScreen(self.map_file)
        self.window.show()

    def getImage(self):
        search_api_server = "https://static-maps.yandex.ru/1.x/"
        api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

        address_ll = ','.join([self.y_line.text(), self.x_line.text()])
        z = self.scales_line.text()
        if not z:
            z = None
            spn = "0.0055,0.0055"
        else:
            spn = None

        search_params = {
            "ll": address_ll,
            "l": "map",
            "spn": spn,
            "z": z
        }
        response = requests.get(search_api_server, params=search_params)
        print(response.url)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
