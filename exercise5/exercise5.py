# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise5.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 330, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(230, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.result.setText("")
        self.result.setObjectName("result")
        self.xB = QtWidgets.QTextEdit(self.centralwidget)
        self.xB.setGeometry(QtCore.QRect(140, 330, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xB.setFont(font)
        self.xB.setObjectName("xB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 621, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 270, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.yA = QtWidgets.QTextEdit(self.centralwidget)
        self.yA.setGeometry(QtCore.QRect(140, 270, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yA.setFont(font)
        self.yA.setObjectName("yA")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 490, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.xA = QtWidgets.QTextEdit(self.centralwidget)
        self.xA.setGeometry(QtCore.QRect(140, 210, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xA.setFont(font)
        self.xA.setObjectName("xA")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 390, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.yB = QtWidgets.QTextEdit(self.centralwidget)
        self.yB.setGeometry(QtCore.QRect(140, 390, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yB.setFont(font)
        self.yB.setObjectName("yB")
        self.yC_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.yC_2.setGeometry(QtCore.QRect(440, 270, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yC_2.setFont(font)
        self.yC_2.setObjectName("yC_2")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(440, 390, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 390, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 330, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.xM = QtWidgets.QTextEdit(self.centralwidget)
        self.xM.setGeometry(QtCore.QRect(440, 330, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xM.setFont(font)
        self.xM.setObjectName("xM")
        self.yC = QtWidgets.QLabel(self.centralwidget)
        self.yC.setGeometry(QtCore.QRect(370, 270, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yC.setFont(font)
        self.yC.setWordWrap(True)
        self.yC.setObjectName("yC")
        self.xC_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.xC_2.setGeometry(QtCore.QRect(440, 210, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xC_2.setFont(font)
        self.xC_2.setObjectName("xC_2")
        self.xC = QtWidgets.QLabel(self.centralwidget)
        self.xC.setGeometry(QtCore.QRect(370, 210, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xC.setFont(font)
        self.xC.setWordWrap(True)
        self.xC.setObjectName("xC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 26))
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
        self.label_5.setText(_translate("MainWindow", "xB"))
        self.label.setText(_translate("MainWindow", "Exercise 5"))
        self.label_2.setText(_translate("MainWindow", "Write a program to enter the coordinates of the vertices of triangle ABC and of point M. Determine whether point M is inside, on the edge or outside triangle ABC."))
        self.label_4.setText(_translate("MainWindow", "yA"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "xA"))
        self.label_9.setText(_translate("MainWindow", "yB"))
        self.label_10.setText(_translate("MainWindow", "yM"))
        self.label_11.setText(_translate("MainWindow", "xM"))
        self.yC.setText(_translate("MainWindow", "yC"))
        self.xC.setText(_translate("MainWindow", "xC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
