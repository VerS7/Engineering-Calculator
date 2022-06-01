# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EngCalculatorUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1071, 528)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(27, 27, 27);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(10, 180, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.Clear.setObjectName("Clear")
        self._7 = QtWidgets.QPushButton(self.centralwidget)
        self._7.setGeometry(QtCore.QRect(10, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._7.setFont(font)
        self._7.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._7.setObjectName("_7")
        self.Cals = QtWidgets.QLabel(self.centralwidget)
        self.Cals.setGeometry(QtCore.QRect(10, 80, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(45)
        self.Cals.setFont(font)
        self.Cals.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);\n"
"border-right-radius: 10px;\n"
"border-radius: 10px;")
        self.Cals.setText("")
        self.Cals.setAlignment(QtCore.Qt.AlignCenter)
        self.Cals.setObjectName("Cals")
        self._8 = QtWidgets.QPushButton(self.centralwidget)
        self._8.setGeometry(QtCore.QRect(80, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._8.setFont(font)
        self._8.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._8.setObjectName("_8")
        self._9 = QtWidgets.QPushButton(self.centralwidget)
        self._9.setGeometry(QtCore.QRect(150, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._9.setFont(font)
        self._9.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._9.setObjectName("_9")
        self._4 = QtWidgets.QPushButton(self.centralwidget)
        self._4.setGeometry(QtCore.QRect(10, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._4.setFont(font)
        self._4.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._4.setObjectName("_4")
        self._5 = QtWidgets.QPushButton(self.centralwidget)
        self._5.setGeometry(QtCore.QRect(80, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._5.setFont(font)
        self._5.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._5.setObjectName("_5")
        self._6 = QtWidgets.QPushButton(self.centralwidget)
        self._6.setGeometry(QtCore.QRect(150, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._6.setFont(font)
        self._6.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._6.setObjectName("_6")
        self._1 = QtWidgets.QPushButton(self.centralwidget)
        self._1.setGeometry(QtCore.QRect(10, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._1.setFont(font)
        self._1.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._1.setObjectName("_1")
        self._2 = QtWidgets.QPushButton(self.centralwidget)
        self._2.setGeometry(QtCore.QRect(80, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._2.setFont(font)
        self._2.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._2.setObjectName("_2")
        self._3 = QtWidgets.QPushButton(self.centralwidget)
        self._3.setGeometry(QtCore.QRect(150, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._3.setFont(font)
        self._3.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._3.setObjectName("_3")
        self._0 = QtWidgets.QPushButton(self.centralwidget)
        self._0.setGeometry(QtCore.QRect(10, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self._0.setFont(font)
        self._0.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self._0.setObjectName("_0")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(80, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(150, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.plus.setObjectName("plus")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(220, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.divide.setFont(font)
        self.divide.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.divide.setObjectName("divide")
        self.root = QtWidgets.QPushButton(self.centralwidget)
        self.root.setGeometry(QtCore.QRect(220, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.root.setFont(font)
        self.root.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.root.setObjectName("root")
        self.ClearForOne = QtWidgets.QPushButton(self.centralwidget)
        self.ClearForOne.setGeometry(QtCore.QRect(150, 180, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.ClearForOne.setFont(font)
        self.ClearForOne.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.ClearForOne.setObjectName("ClearForOne")
        self.Pi = QtWidgets.QPushButton(self.centralwidget)
        self.Pi.setGeometry(QtCore.QRect(220, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.Pi.setFont(font)
        self.Pi.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.Pi.setObjectName("Pi")
        self.Exp = QtWidgets.QPushButton(self.centralwidget)
        self.Exp.setGeometry(QtCore.QRect(290, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(40)
        self.Exp.setFont(font)
        self.Exp.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.Exp.setObjectName("Exp")
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(290, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.mult.setFont(font)
        self.mult.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.mult.setObjectName("mult")
        self.factorial = QtWidgets.QPushButton(self.centralwidget)
        self.factorial.setGeometry(QtCore.QRect(290, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(30)
        self.factorial.setFont(font)
        self.factorial.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.factorial.setObjectName("factorial")
        self.degree2 = QtWidgets.QPushButton(self.centralwidget)
        self.degree2.setGeometry(QtCore.QRect(290, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.degree2.setFont(font)
        self.degree2.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.degree2.setObjectName("degree2")
        self.Persentage = QtWidgets.QPushButton(self.centralwidget)
        self.Persentage.setGeometry(QtCore.QRect(220, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(35)
        self.Persentage.setFont(font)
        self.Persentage.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.Persentage.setObjectName("Persentage")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(290, 180, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.Calculate.setFont(font)
        self.Calculate.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(89, 89, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.Calculate.setObjectName("Calculate")
        self.log = QtWidgets.QPushButton(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(360, 250, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.log.setFont(font)
        self.log.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(68, 68, 68);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.log.setObjectName("log")
        self.log2 = QtWidgets.QPushButton(self.centralwidget)
        self.log2.setGeometry(QtCore.QRect(360, 320, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.log2.setFont(font)
        self.log2.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(68, 68, 68);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.log2.setObjectName("log2")
        self.log8 = QtWidgets.QPushButton(self.centralwidget)
        self.log8.setGeometry(QtCore.QRect(360, 390, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.log8.setFont(font)
        self.log8.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(68, 68, 68);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.log8.setObjectName("log8")
        self.lg10 = QtWidgets.QPushButton(self.centralwidget)
        self.lg10.setGeometry(QtCore.QRect(360, 460, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.lg10.setFont(font)
        self.lg10.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(68, 68, 68);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.lg10.setObjectName("lg10")
        self.PrevCals = QtWidgets.QLabel(self.centralwidget)
        self.PrevCals.setGeometry(QtCore.QRect(10, 10, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(45)
        self.PrevCals.setFont(font)
        self.PrevCals.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(180, 180, 180);\n"
"border-right-radius: 10px;\n"
"border-radius: 10px;")
        self.PrevCals.setText("")
        self.PrevCals.setAlignment(QtCore.Qt.AlignCenter)
        self.PrevCals.setObjectName("PrevCals")
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(480, 120, 581, 401))
        self.graph.setStyleSheet("background-color: rgb(37, 37, 37);")
        self.graph.setObjectName("graph")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 60, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.y_label = QtWidgets.QLabel(self.centralwidget)
        self.y_label.setGeometry(QtCore.QRect(480, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        self.y_label.setFont(font)
        self.y_label.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);\n"
"border-right-radius: 10px;\n"
"border-radius: 10px;")
        self.y_label.setObjectName("y_label")
        self.graphbuildlabel = QtWidgets.QLabel(self.centralwidget)
        self.graphbuildlabel.setGeometry(QtCore.QRect(490, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.graphbuildlabel.setFont(font)
        self.graphbuildlabel.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")
        self.graphbuildlabel.setObjectName("graphbuildlabel")
        self.graph_build = QtWidgets.QPushButton(self.centralwidget)
        self.graph_build.setGeometry(QtCore.QRect(960, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.graph_build.setFont(font)
        self.graph_build.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")
        self.graph_build.setObjectName("graph_build")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(830, 60, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Инженерный Калькулятор"))
        self.Clear.setText(_translate("MainWindow", "Очистить"))
        self._7.setText(_translate("MainWindow", "7"))
        self._8.setText(_translate("MainWindow", "8"))
        self._9.setText(_translate("MainWindow", "9"))
        self._4.setText(_translate("MainWindow", "4"))
        self._5.setText(_translate("MainWindow", "5"))
        self._6.setText(_translate("MainWindow", "6"))
        self._1.setText(_translate("MainWindow", "1"))
        self._2.setText(_translate("MainWindow", "2"))
        self._3.setText(_translate("MainWindow", "3"))
        self._0.setText(_translate("MainWindow", "0"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.root.setText(_translate("MainWindow", "√"))
        self.ClearForOne.setText(_translate("MainWindow", "<"))
        self.Pi.setText(_translate("MainWindow", "𝛑"))
        self.Exp.setText(_translate("MainWindow", "e"))
        self.mult.setText(_translate("MainWindow", "×"))
        self.factorial.setText(_translate("MainWindow", "n!"))
        self.degree2.setText(_translate("MainWindow", "x^2"))
        self.Persentage.setText(_translate("MainWindow", "%"))
        self.Calculate.setText(_translate("MainWindow", "Рассчитать"))
        self.log.setText(_translate("MainWindow", "log2"))
        self.log2.setText(_translate("MainWindow", "log4"))
        self.log8.setText(_translate("MainWindow", "log8"))
        self.lg10.setText(_translate("MainWindow", "log10"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите функцию"))
        self.y_label.setText(_translate("MainWindow", " y = "))
        self.graphbuildlabel.setText(_translate("MainWindow", "Построение графиков"))
        self.graph_build.setText(_translate("MainWindow", "Построить"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Интервал"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())