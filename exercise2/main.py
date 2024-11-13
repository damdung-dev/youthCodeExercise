import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise2 import Ui_MainWindow
from functools import cache
@cache

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.calculateButton.clicked.connect(self.calculate)

    def calculate(self):
        xa=float(self.uic.xA.toPlainText())
        ya=float(self.uic.yA.toPlainText())
        xb=float(self.uic.xB.toPlainText())
        yb=float(self.uic.yB.toPlainText())
        ab=abs((xb-xa)**2+(yb-ya)**2)
        self.uic.result.setText(str(ab))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())