# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created: Mon Mar 20 10:35:23 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from math import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(498, 539)
        MainWindow.setMaximumSize(QtCore.QSize(11111111, 11111111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_16 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout.addWidget(self.pushButton_16, 4, 5, 1, 1)
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout.addWidget(self.pushButton_17, 5, 5, 1, 1)
        self.pushButton_18 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_18.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout.addWidget(self.pushButton_18, 6, 5, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout.addWidget(self.pushButton_13, 5, 4, 1, 1)
        self.tan = QtGui.QPushButton(self.centralwidget)
        self.tan.setObjectName(_fromUtf8("tan"))
        self.gridLayout.addWidget(self.tan, 1, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("color:\"purple\""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 6)
        self.tanh = QtGui.QPushButton(self.centralwidget)
        self.tanh.setObjectName(_fromUtf8("tanh"))
        self.gridLayout.addWidget(self.tanh, 1, 5, 1, 1)
        self.acos = QtGui.QPushButton(self.centralwidget)
        self.acos.setObjectName(_fromUtf8("acos"))
        self.gridLayout.addWidget(self.acos, 2, 1, 1, 1)
        self.asinh = QtGui.QPushButton(self.centralwidget)
        self.asinh.setObjectName(_fromUtf8("asinh"))
        self.gridLayout.addWidget(self.asinh, 2, 3, 1, 1)
        self.cosh = QtGui.QPushButton(self.centralwidget)
        self.cosh.setObjectName(_fromUtf8("cosh"))
        self.gridLayout.addWidget(self.cosh, 1, 4, 1, 1)
        self.acos_2 = QtGui.QPushButton(self.centralwidget)
        self.acos_2.setObjectName(_fromUtf8("acos_2"))
        self.gridLayout.addWidget(self.acos_2, 2, 2, 1, 1)
        self.acosh = QtGui.QPushButton(self.centralwidget)
        self.acosh.setObjectName(_fromUtf8("acosh"))
        self.gridLayout.addWidget(self.acosh, 2, 4, 1, 1)
        self.cos = QtGui.QPushButton(self.centralwidget)
        self.cos.setObjectName(_fromUtf8("cos"))
        self.gridLayout.addWidget(self.cos, 1, 1, 1, 1)
        self.sinh = QtGui.QPushButton(self.centralwidget)
        self.sinh.setObjectName(_fromUtf8("sinh"))
        self.gridLayout.addWidget(self.sinh, 1, 3, 1, 1)
        self.asin = QtGui.QPushButton(self.centralwidget)
        self.asin.setObjectName(_fromUtf8("asin"))
        self.gridLayout.addWidget(self.asin, 2, 0, 1, 1)
        self.sin = QtGui.QPushButton(self.centralwidget)
        self.sin.setObjectName(_fromUtf8("sin"))
        self.gridLayout.addWidget(self.sin, 1, 0, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout.addWidget(self.pushButton_15, 4, 4, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 6, 3, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 5, 3, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 5, 2, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 6, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 60))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 5, 1, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(30, 60))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 4, 3, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout.addWidget(self.pushButton_14, 6, 4, 1, 1)
        self.atanh = QtGui.QPushButton(self.centralwidget)
        self.atanh.setObjectName(_fromUtf8("atanh"))
        self.gridLayout.addWidget(self.atanh, 2, 5, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 60))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 4, 2, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 6, 1, 1, 1)
        self.sin_2 = QtGui.QPushButton(self.centralwidget)
        self.sin_2.setObjectName(_fromUtf8("sin_2"))
        self.gridLayout.addWidget(self.sin_2, 7, 1, 1, 1)
        self.sin_3 = QtGui.QPushButton(self.centralwidget)
        self.sin_3.setObjectName(_fromUtf8("sin_3"))
        self.gridLayout.addWidget(self.sin_3, 7, 2, 1, 1)
        self.sin_4 = QtGui.QPushButton(self.centralwidget)
        self.sin_4.setObjectName(_fromUtf8("sin_4"))
        self.gridLayout.addWidget(self.sin_4, 7, 3, 1, 1)
        self.sin_5 = QtGui.QPushButton(self.centralwidget)
        self.sin_5.setObjectName(_fromUtf8("sin_5"))
        self.gridLayout.addWidget(self.sin_5, 7, 4, 1, 1)
        self.sin_6 = QtGui.QPushButton(self.centralwidget)
        self.sin_6.setObjectName(_fromUtf8("sin_6"))
        self.gridLayout.addWidget(self.sin_6, 7, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(MainWindow)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.sin)
        MainWindow.setTabOrder(self.sin, self.cos)
        MainWindow.setTabOrder(self.cos, self.tan)
        MainWindow.setTabOrder(self.tan, self.sinh)
        MainWindow.setTabOrder(self.sinh, self.cosh)
        MainWindow.setTabOrder(self.cosh, self.tanh)
        MainWindow.setTabOrder(self.tanh, self.asin)
        MainWindow.setTabOrder(self.asin, self.acos)
        MainWindow.setTabOrder(self.acos, self.acos_2)
        MainWindow.setTabOrder(self.acos_2, self.asinh)
        MainWindow.setTabOrder(self.asinh, self.acosh)
        MainWindow.setTabOrder(self.acosh, self.atanh)
        MainWindow.setTabOrder(self.atanh, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_15)
        MainWindow.setTabOrder(self.pushButton_15, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.pushButton_18)
        MainWindow.setTabOrder(self.pushButton_18, self.sin_2)
        MainWindow.setTabOrder(self.sin_2, self.sin_3)
        MainWindow.setTabOrder(self.sin_3, self.sin_4)
        MainWindow.setTabOrder(self.sin_4, self.sin_5)
        MainWindow.setTabOrder(self.sin_5, self.sin_6)
        
##Methods for the buttons
        self.pushButton_1.clicked.connect(self.one_clicked)
        self.pushButton_2.clicked.connect(self.two_clicked)
        self.pushButton_3.clicked.connect(self.three_clicked)
        self.pushButton_4.clicked.connect(self.four_clicked)
        self.pushButton_5.clicked.connect(self.five_clicked)
        self.pushButton_6.clicked.connect(self.six_clicked)
        self.pushButton_7.clicked.connect(self.seven_clicked)
        self.pushButton_8.clicked.connect(self.eight_clicked)
        self.pushButton_9.clicked.connect(self.nine_clicked)
        self.pushButton_10.clicked.connect(self.zero_clicked)
        self.pushButton_12.clicked.connect(self.addi_clicked)
        self.pushButton_11.clicked.connect(self.equal_clicked)
        self.sin.clicked.connect(self.sin_clicked)
        self.pushButton_13.clicked.connect(self.multiply_clicked)
        self.asin.clicked.connect(self.asin_clicked)
        self.acos.clicked.connect(self.acos_pressed)
        self.cos.clicked.connect(self.cos_pressed)
        self.sin_2.clicked.connect(self.clear_clicked)
        self.pushButton_15.clicked.connect(self.div_clicked)
        self.pushButton_17.clicked.connect(self.pi_clicked)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator*", None))
        self.pushButton_16.setText(_translate("MainWindow", "-", None))
        self.pushButton_17.setText(_translate("MainWindow", "pi", None))
        self.pushButton_18.setText(_translate("MainWindow", "rt(#,power)", None))
        self.pushButton_13.setText(_translate("MainWindow", "*", None))
        self.tan.setText(_translate("MainWindow", "tan", None))
        self.tanh.setText(_translate("MainWindow", "tanh", None))
        self.acos.setText(_translate("MainWindow", "acos", None))
        self.asinh.setText(_translate("MainWindow", "asinh", None))
        self.cosh.setText(_translate("MainWindow", "cosh", None))
        self.acos_2.setText(_translate("MainWindow", "atan", None))
        self.acosh.setText(_translate("MainWindow", "acosh", None))
        self.cos.setText(_translate("MainWindow", "cos", None))
        self.sinh.setText(_translate("MainWindow", "sinh", None))
        self.asin.setText(_translate("MainWindow", "asin", None))
        self.sin.setText(_translate("MainWindow", "sin", None))
        self.pushButton_15.setText(_translate("MainWindow", "/", None))
        self.pushButton_10.setText(_translate("MainWindow", "0", None))
        self.pushButton_12.setText(_translate("MainWindow", "+", None))
        self.pushButton_8.setText(_translate("MainWindow", "8", None))
        self.pushButton_9.setText(_translate("MainWindow", "9", None))
        self.pushButton_2.setText(_translate("MainWindow", "2", None))
        self.pushButton_5.setText(_translate("MainWindow", "5", None))
        self.pushButton_1.setText(_translate("MainWindow", "1", None))
        self.pushButton_4.setText(_translate("MainWindow", "4", None))
        self.pushButton_11.setText(_translate("MainWindow", "=", None))
        self.pushButton_14.setText(_translate("MainWindow", "^", None))
        self.atanh.setText(_translate("MainWindow", "atanh", None))
        self.pushButton_3.setText(_translate("MainWindow", "3", None))
        self.pushButton_7.setText(_translate("MainWindow", "7", None))
        self.pushButton_6.setText(_translate("MainWindow", "6", None))
        self.sin_2.setText(_translate("MainWindow", "clear", None))
        self.sin_3.setText(_translate("MainWindow", "store", None))
        self.sin_4.setText(_translate("MainWindow", "x", None))
        self.sin_5.setText(_translate("MainWindow", "y", None))
        self.sin_6.setText(_translate("MainWindow", "reset", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "Instructions", None))
        self.actionAbout_2.setText(_translate("MainWindow", "About", None))
        
####THESE ARE THE FUNCTIOMS FOR THE BUTTONS###
    def two_clicked(self, MainWindow):
        self.lineEdit.insert('2')
        return 0;


    def one_clicked(self, MainWindow):
        self.lineEdit.insert('1')
        return 0;


    def three_clicked(self, MainWindow):
        self.lineEdit.insert('3')
        return 0;

    def four_clicked(self, MainWindow):
        self.lineEdit.insert('4')
        return 0;

    def five_clicked(self, MainWindow):
        self.lineEdit.insert('5')
        return 0;

    def six_clicked(self, MainWindow):
        self.lineEdit.insert('6')
        return 0;

    def seven_clicked(self, MainWindow):
        self.lineEdit.insert('7')
        return 0;

    def eight_clicked(self, MainWindow):
        self.lineEdit.insert('8')
        return 0;

    def nine_clicked(self, MainWindow):
        self.lineEdit.insert('9')
        return 0;

    def zero_clicked(self, MainWindow):
        self.lineEdit.insert('0')
        return 0;
    
    def addi_clicked(self, MainWindow):
        self.lineEdit.insert(' + ')
        return 0,

    def equal_clicked(self, MainWindow):
        step1 = self.lineEdit.text()
        print eval(str(step1))
        self.lineEdit.setText(str(eval(str(step1))))
        return 0,

    def sin_clicked(self, MainWindow):
        self.lineEdit.insert(' sin() ')
        return 0;

    def asin_clicked(self, MainWindow):
        self.lineEdit.insert(' asin() ')
        return 0;

    def multiply_clicked(self, MainWindow):
        self.lineEdit.insert(' * ')
        return 0;

    def acos_pressed(self, MainWindow):
        self.lineEdit.insert(' acos()')

    def cos_pressed(self, MainWindow):
        self.lineEdit.insert(' cos() ')

    def clear_clicked(self, MainWindow):
        self.lineEdit.clear()
       
       
        

    def div_clicked(self, MainWindow):
        self.lineEdit.insert(' / ')

    def pi_clicked(self, MainWindow):
        self.lineEdit.insert(' pi ')



    
    
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
