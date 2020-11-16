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
            lines = data.readlines()
            lines2 = []
            for i in lines:
                g = ' '.join(i.split())
                if not ''.join(g.split()).isdigit() and g != '':
                    self.label_5.setText(f"В файле '{self.lineEdit.text()}' содержатся некорректные данные")
                    return 0
                else:
                    if g == '':
                        self.label_5.setText(f"Файл '{self.lineEdit.text()}' - пустой")
                        max_f, min_f, med_f = '', '', ''
                    else:
                        lines2 += [int(t) for t in g.split()]
                        max_f = str(max(lines2))
                        min_f = str(min(lines2))
                        med_f = str(round(sum(lines2) / len(lines2), 2))
            self.lineEdit_2.setText(max_f)
            self.lineEdit_3.setText(min_f)
            self.lineEdit_4.setText(med_f)
            data.close()

            out = open(f'output.txt', mode='w')
            out.write(f'Максимальное значение: {max_f}\n')
            out.write(f'Минимальное значение: {min_f}\n')
            out.write(f'Среднее значение: {med_f}\n')

        except FileNotFoundError:
            self.label_5.setText(f"Файл '{self.lineEdit.text()}' не найден")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
