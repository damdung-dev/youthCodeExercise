import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise4 import Ui_MainWindow
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.calculate)
        
    def calculate(self):
        a=float(self.uic.textEdit.toPlainText())
        b=float(self.uic.textEdit_2.toPlainText())
        c=float(self.uic.textEdit_3.toPlainText())
        if a+b>c or a+c>b or b+c>a:
            self.uic.trianglesidecheck.setText("3 values edges")
            p=(a+b+c)/2
            s=math.sqrt(p*(p-a)*(p-b)*(p-c))
            self.uic.trianglearea.setText(str(s))
            if a==b and b==c and c==a:
                self.uic.triangletype.setText("Equilateral triangle")
            elif a==b or b==c or c==a:
                self.uic.triangletype.setText("Isoceles triangle")
            elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
                self.uic.triangletype.setText("Right triangle")
            else:
                self.uic.triangletype.setText("Scalene triangle")
        else:
            self.uic.trianglesidecheck.setText("3 wrong edges")

                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())