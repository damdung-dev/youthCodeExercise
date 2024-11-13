import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercise7 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.sortButton.clicked.connect(self.calculate)
    
    def calculate(self):
        a=float(self.uic.before_sorting.toPlainText())
        b=float(self.uic.before_sorting_2.toPlainText())
        self.uic.after_sorting.setText(str(-b/a))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())