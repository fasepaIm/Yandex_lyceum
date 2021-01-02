import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.show_result)
        
    def show_result(self):
        first_text = self.plainTextEdit.toPlainText().split('\n')
        second_text = self.plainTextEdit_2.toPlainText().split('\n')
        c = len(list(set(first_text) & set(second_text)))
        need = self.doubleSpinBox.value()
        result = round(c * 2 / (len(set(first_text)) + len(set(second_text))) * 100, 2)
        self.statusBar().showMessage(f'Код похож на {str(result)}%')
        if result >= need:
            self.statusBar().setStyleSheet("""QStatusBar {
                                              color: rgb(0, 0, 0);
                                              background-color: rgb(255, 0, 0);}""")
        else:
            self.statusBar().setStyleSheet("""QStatusBar {
                                              color: rgb(0, 0, 0);
                                              background-color: rgb(0, 255, 0);}""") 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
