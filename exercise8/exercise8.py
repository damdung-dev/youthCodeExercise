# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise8.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.before_sorting_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.before_sorting_2.setGeometry(QtCore.QRect(300, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.before_sorting_2.setFont(font)
        self.before_sorting_2.setObjectName("before_sorting_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 210, 16, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 71, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.after_sorting = QtWidgets.QLabel(self.centralwidget)
        self.after_sorting.setGeometry(QtCore.QRect(200, 280, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.after_sorting.setFont(font)
        self.after_sorting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.after_sorting.setText("")
        self.after_sorting.setObjectName("after_sorting")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 210, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 591, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.sortButton = QtWidgets.QPushButton(self.centralwidget)
        self.sortButton.setGeometry(QtCore.QRect(70, 390, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.sortButton.setFont(font)
        self.sortButton.setObjectName("sortButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.before_sorting = QtWidgets.QTextEdit(self.centralwidget)
        self.before_sorting.setGeometry(QtCore.QRect(110, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.before_sorting.setFont(font)
        self.before_sorting.setObjectName("before_sorting")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 210, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 210, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.before_sorting_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.before_sorting_3.setGeometry(QtCore.QRect(470, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.before_sorting_3.setFont(font)
        self.before_sorting_3.setObjectName("before_sorting_3")
        self.after_sorting_2 = QtWidgets.QLabel(self.centralwidget)
        self.after_sorting_2.setGeometry(QtCore.QRect(200, 340, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.after_sorting_2.setFont(font)
        self.after_sorting_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.after_sorting_2.setText("")
        self.after_sorting_2.setObjectName("after_sorting_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "+"))
        self.label_5.setText(_translate("MainWindow", "Result"))
        self.label_6.setText(_translate("MainWindow", "= 0"))
        self.label_2.setText(_translate("MainWindow", "Write a program to solve the quadratic equation: ax2 + bx + c = 0 (a, b, c are entered from the keyboard). Consider all possible cases."))
        self.sortButton.setText(_translate("MainWindow", " Calculate"))
        self.label.setText(_translate("MainWindow", "Exercise 8"))
        self.label_3.setText(_translate("MainWindow", "x^2"))
        self.label_7.setText(_translate("MainWindow", "x +"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
