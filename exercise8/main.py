import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise8 import Ui_MainWindow
import math

def delta(a,b,c):
    return b**2-4*a*c

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.sortButton.clicked.connect(self.calculate)

    def calculate(self):
        a=float(self.uic.before_sorting.toPlainText())
        b=float(self.uic.before_sorting_2.toPlainText())
        c=float(self.uic.before_sorting_3.toPlainText())
        delta(a,b,c)
        if delta(a,b,c)>0:
            self.uic.after_sorting.setText(str((-b+math.sqrt(delta(a,b,c)))/(2*a)))
            self.uic.after_sorting_2.setText(str((-b-math.sqrt(delta(a,b,c)))/(2*a)))
        elif delta(a,b,c)==0:
            self.uic.after_sorting_2.setText(str((-b)/(2*a)))
            self.uic.after_sorting.setText(str((-b)/(2*a)))
        else:
            self.uic.after_sorting_2.setText("wrong entry, please check again")
            self.uic.after_sorting.setText("wrong entry, please check again")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

