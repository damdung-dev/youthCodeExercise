import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise5 import Ui_MainWindow

result=0

def area_calculation(xA, yA, xB, yB, xC, yC):
    return 0.5*abs(xA*yB-xB*yA+xB*yC-xC*yB+xC*yA-xA*yC)
def compare(a,aMAB,aMAC,aMBC):
    if a>0:
        result=1
    elif aMAB==0 or aMAC==0 or aMBC==0:
        result=2
    else:
        result=3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        xA=float(self.uic.xA.toPlainText())
        yA=float(self.uic.yA.toPlainText())
        xB=float(self.uic.xB.toPlainText())
        yB=float(self.uic.yB.toPlainText())
        xC=float(self.uic.xC_2.toPlainText())
        yC=float(self.uic.yC_2.toPlainText())
        xM=float(self.uic.xM.toPlainText())
        yM=float(self.uic.textEdit_6.toPlainText())
        aMAB = area_calculation(xM, yM, xA, yA, xB, yB);
        aMAC = area_calculation(xM, yM, xA, yA, xC, yC);
        aMBC = area_calculation(xM, yM, xB, yB, xC, yC);
        aABC = area_calculation(xA, yA, xB, yB, xC, yC);
        a = aMAB+aMAC+aMBC-aABC
        compare(a,aMAB,aMAC,aMBC)
        if a>0:
            self.uic.result.setText("M nam ngoai tam giac ABC")
        elif aMAB==0 or aMAC==0 or aMBC==0:
            self.uic.result.setText("M nam tren canh cua tam giac ABC")
        else:
            self.uic.result.setText("M nam trong tam giac ABC")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())