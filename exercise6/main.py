import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise6 import Ui_MainWindow
   
def swap(remember,i):
    temp=remember[i+1]
    remember[i+1]=remember[i] 
    remember[i]=temp
    
def bubblesort(remember,n):
    print(remember)
    for j in range(0,5):
        for i in range(0,2):
            if remember[i]>remember[i+1]:
                swap(remember,i)
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.sortButton.clicked.connect(self.sort)
        
    def sort(self):
        remember=self.uic.before_sorting.toPlainText()
        remember=remember.split()
        bubblesort(remember,len(remember))
        self.uic.after_sorting.setText(str(remember))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())