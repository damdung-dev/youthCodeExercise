import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise9 import Ui_MainWindow
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.sortButton.clicked.connect(self.calculate)

    def calculate(self):
        min=float(self.uic.before_sorting.toPlainText())
        degree=min/60
        if degree>=0 and degree<90:
            self.uic.after_sorting.setText("first")
        elif degree>=90 and degree<180:
            self.uic.after_sorting.setText("second")
        elif degree>=180 and degree<270:
            self.uic.after_sorting.setText("third")
        elif degree>=270 and degree<360:
            self.uic.after_sorting.setText("forth")
        else:
            self.uic.after_sorting.setText("error")
        rad=degree*(3.14/180)
        self.uic.after_sorting_2.setText(str(math.cos(rad)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())