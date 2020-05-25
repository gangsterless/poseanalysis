# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 652)
        MainWindow.setStyleSheet("background-image:url(./UI/pic/bk.png)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 101, 28))
        self.pushButton.setStyleSheet("background-color:rgb(255,0,255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 100, 30))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 110, 256, 30))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 170, 256, 30))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 170, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 110, 141, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(600, 250, 121, 19))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 10, 51, 51))
        self.pushButton_3.setStyleSheet("border-image: url(./UI/pic/question.png);\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(600, 290, 121, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
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
        self.pushButton.setText(_translate("MainWindow", "输入视频路径"))
        self.pushButton_2.setText(_translate("MainWindow", "openpose路径"))
        self.comboBox.setItemText(0, _translate("MainWindow", "手部模型"))
        self.comboBox.setItemText(1, _translate("MainWindow", "身体部分模型"))
        self.label_3.setText(_translate("MainWindow", "预训练模型选择"))
        self.checkBox.setText(_translate("MainWindow", "是否检测手部"))
        self.checkBox_2.setText(_translate("MainWindow", "是否检测身体"))

