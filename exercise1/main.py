import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise1 import Ui_MainWindow
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.calculateButton.clicked.connect(self.calculate)
    def calculate(self):
        s=float(self.uic.textEdit.toPlainText())
        r=math.sqrt(s/(4.0*3.14))
        v=4/3*3.14*r**3
        self.uic.result.setText(str(v))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())