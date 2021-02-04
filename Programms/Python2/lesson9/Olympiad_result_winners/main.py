import csv
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        with open('rez.csv', encoding='utf8') as csvfile:
            results = csv.DictReader(csvfile, delimiter=',')
            schools = set()
            classes = set()
            for i in results:
                schools.add(i['login'].split('-')[2])
                classes.add(i['login'].split('-')[3])
            self.comboBox.addItems(sorted(list(schools)))
            self.comboBox_2.addItems(sorted(list(classes)))
        self.pushButton.clicked.connect(self.check)
        self.comboBox.currentTextChanged.connect(self.update_combo_box_1)

    def check(self):
        schools_value = self.comboBox.currentText()
        classes_value = self.comboBox_2.currentText()
        people = {}
        logins = {}
        with open('rez.csv', encoding="utf8") as csvfile:
            results = csv.DictReader(csvfile, delimiter=',')
            for i in results:
                if schools_value == 'Все':
                    if classes_value == 'Все':
                        if i['Score'] not in people:
                            people[i['Score']] = [i['user_name'].split()[-2]]
                        else:
                            people[i['Score']] += [i['user_name'].split()[-2]]

                    else:
                        if i['login'].split('-')[3] == classes_value:
                            if i['Score'] not in people:
                                people[i['Score']] = [i['user_name'].split()[-2]]
                            else:
                                people[i['Score']] += [i['user_name'].split()[-2]]
                else:
                    if classes_value == 'Все':
                        if i['login'].split('-')[2] == schools_value:
                            if i['Score'] not in people:
                                people[i['Score']] = [i['user_name'].split()[-2]]
                            else:
                                people[i['Score']] += [i['user_name'].split()[-2]]

                    else:
                        if i['login'].split('-')[3] == classes_value and i['login'].split('-')[2] == schools_value:
                            if i['Score'] not in people:
                                people[i['Score']] = [i['user_name'].split()[-2]]
                            else:
                                people[i['Score']] += [i['user_name'].split()[-2]]
                logins[i['user_name'].split()[-2]] = i['login']
            for i in people:
                surnames = sorted(people[i], reverse=True)
            row_color = 0
            row = 0
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            for score in people:
                for surname in range(len(people[score])):
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    self.tableWidget.setItem(
                        row, 0, QTableWidgetItem(people[score][surname]))
                    self.tableWidget.setItem(
                        row, 1, QTableWidgetItem(score))
                    self.tableWidget.setItem(
                        row, 2, QTableWidgetItem(logins[people[score][surname]]))
                    if row_color == 0:
                        self.color_row(row, QColor(224, 214, 0))
                    elif row_color == 1:
                        self.color_row(row, QColor(180, 181, 189))
                    elif row_color == 2:
                        self.color_row(row, QColor(155, 82, 33))
                    row += 1
                row_color += 1
        self.tableWidget.resizeColumnsToContents()

    def update_combo_box_1(self, event):
        with open('rez.csv', encoding='utf8') as csvfile:
            results = csv.DictReader(csvfile, delimiter=',')
            classes = set()
            if self.comboBox_2.currentText() == 'Все':
                for i in results:
                    if event == 'Все':
                        classes.add(i['login'].split('-')[3])
                    else:
                        if i['login'].split('-')[2] == event:
                            classes.add(i['login'].split('-')[3])
                self.comboBox_2.clear()
                self.comboBox_2.addItem('Все')
                self.comboBox_2.addItems(sorted(list(classes)))

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
