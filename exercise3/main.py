import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.calculateButton.clicked.connect(self.calculate)
    def calculate(self):
        xc=float(self.uic.xC.toPlainText())
        yc=float(self.uic.yC.toPlainText())
        r=float(self.uic.R.toPlainText())
        xm=float(self.uic.xM.toPlainText())
        ym=float(self.uic.yM.toPlainText())
        cm=abs((xm-xc)**2+(ym-yc)**2)
        if r==cm:
            self.uic.label_8.setText("M on the circle")
        elif r<cm:
            self.uic.label_8.setText("M outside of the circle")
        else:
            self.uic.label_8.setText("M inside of the circle")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())