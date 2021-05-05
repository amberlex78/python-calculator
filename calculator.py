# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.lbl_display = QtWidgets.QLabel(self.CentralWidget)
        self.lbl_display.setGeometry(QtCore.QRect(0, 0, 400, 100))
        self.lbl_display.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.lbl_display.setFont(font)
        self.lbl_display.setStyleSheet("color: rgb(0, 128, 0);border-color: rgb(0, 128, 0);")
        self.lbl_display.setLineWidth(1)
        self.lbl_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_display.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_display.setObjectName("lbl_display")
        self.btn_0 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_0.setGeometry(QtCore.QRect(110, 410, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_2.setGeometry(QtCore.QRect(110, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_3.setGeometry(QtCore.QRect(210, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 210, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_5.setGeometry(QtCore.QRect(110, 210, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_6.setGeometry(QtCore.QRect(210, 210, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 110, 80, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_8.setGeometry(QtCore.QRect(110, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_8.setFlat(False)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_9.setGeometry(QtCore.QRect(210, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_9.setObjectName("btn_9")
        self.btn_divide = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_divide.setGeometry(QtCore.QRect(310, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_multiply = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_multiply.setGeometry(QtCore.QRect(310, 210, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_minus = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_minus.setGeometry(QtCore.QRect(310, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_plus.setGeometry(QtCore.QRect(310, 410, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_equal = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_equal.setGeometry(QtCore.QRect(210, 410, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_clear = QtWidgets.QPushButton(self.CentralWidget)
        self.btn_clear.setGeometry(QtCore.QRect(10, 410, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("color: rgb(235, 235, 235);background-color: rgb(88, 88, 88);")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lbl_display.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_multiply.setText(_translate("MainWindow", "x"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_clear.setText(_translate("MainWindow", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
