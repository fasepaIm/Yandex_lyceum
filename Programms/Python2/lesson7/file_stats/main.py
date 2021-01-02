import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.return_values)

    def return_values(self):
        self.label_5.setText('')
        try:
            data = open(f'{self.lineEdit.text()}', encoding='utf-8')
            lines = sum([list(map(lambda n: int(n), i.split())) for i in data.readlines()], []) 
            if len(lines) == 0:
                self.label_5.setText(f"Файл '{self.lineEdit.text()}' - пустой")
                max_f, min_f, med_f = '', '', ''
            else:
                max_f = str(max(lines))
                min_f = str(min(lines))
                med_f = str(round(sum(lines) / len(lines), 2))
            self.lineEdit_2.setText(max_f)
            self.lineEdit_3.setText(min_f)
            self.lineEdit_4.setText(med_f)
            data.close()

            out = open(f'output.txt', mode='w')
            out.write(f'Максимальное значение: {max_f}\n')
            out.write(f'Минимальное значение: {min_f}\n')
            out.write(f'Среднее значение: {med_f}\n')

        except ValueError:
            self.label_5.setText(f"В файле '{self.lineEdit.text()}' содержатся некорректные данные")

        except FileNotFoundError:
            self.label_5.setText(f"Файл '{self.lineEdit.text()}' не найден")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
