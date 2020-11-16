import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plan.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.added)

    def added(self):
        self.listWidget.setSortingEnabled(True)
        self.listWidget.addItem(f'{self.calendarWidget.selectedDate().toPyDate()} {self.timeEdit.time().toString()} - {self.lineEdit.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
