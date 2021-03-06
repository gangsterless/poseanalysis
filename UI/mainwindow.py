# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import time
import webbrowser as browser
from UI.help import help_Ui_Form
from Utils.GenerateJson import generatefile,webcam,killopenpose
from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime , QObject
from win32process import SuspendThread, ResumeThread
import ctypes
#这个线程用来生成json文件
class BackendThread(QObject):

    def run(self,path):
        generatefile(r'D:\big3data\down\wulian\mydataset\testdance', 'video.mp4')
class camThread(QObject):

    def run(self):
        webcam()

    def __del__(self):
        print("del")

class Ui_MainWindow(object):
    def __init__(self):
        self.video = ''



        # helpform.setupUi(self.main)
        # helpform.show()


    def open_webcam(self):
        if self.pushButton_8.text()=='打开摄像头':

            self.pushButton_8.setText('关闭摄像头')
            self.webcam = camThread()
            # 连接信号
            self.thread = QThread()
            self.webcam.moveToThread(self.thread)
            # 开始线程
            self.thread.started.connect(self.webcam.run)
            self.thread.start()
        elif self.pushButton_8.text()=='关闭摄像头':
            self.pushButton_8.setText('打开摄像头')
            killopenpose()
        # 访问openpose官网
    def choose_openpose(self):
        dir = QFileDialog.getOpenFileName(filter='OpenPoseDemo.exe')[0]
        self.label.setText(dir)
    def visit_openpose(self):
        browser.open("https://github.com/CMU-Perceptual-Computing-Lab/openpose")

    def choose_path_video(self):
        dir = QFileDialog.getOpenFileName(filter='*.mp4')[0]

        dirls = dir.split('/')
        videoname = dirls[-1]
        del dirls[-1]
        videordir = '/'.join(dirls)
        print(videordir)
        print(videoname)
        self.label_2.setText(videoname)
        return (videordir, videoname)

    def generatefile_bt(self):
        print('hahahha')
        if self.video == '':
            QMessageBox.warning(self.main, "警告对话框", "路径信息为空，请先选择一个视频")
            return

        self.pushButton.setText('已经调用了openpose')
        # 创建线程
        self.backend = BackendThread()
        # 连接信号
        self.thread = QThread()
        self.backend.moveToThread(self.thread)
        # 开始线程
        self.thread.started.connect(self.backend.run)
        self.thread.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("动作识别分析系统")
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
        self.comboBox.setGeometry(QtCore.QRect(490, 170, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 100, 141, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(500, 240, 121, 19))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 20, 51, 51))
        self.pushButton_3.setStyleSheet("border-image: url(./UI/pic/question.png);\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 280, 121, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 320, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 230, 101, 28))
        self.pushButton_5.setStyleSheet("background-color:rgb(255,0,255)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 230, 256, 30))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 380, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 440, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(660, 530, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 500, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
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



        self.pushButton_9.clicked.connect(self.visit_openpose)
        self.pushButton_2.clicked.connect(self.choose_openpose)
        self.pushButton.clicked.connect(self.choose_path_video)
        self.pushButton_8.clicked.connect(self.open_webcam)
        # self.pushButton_3.clicked.connect(self.helpform.show)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "动作识别分析系统"))
        self.pushButton.setText(_translate("MainWindow", "输入视频路径"))
        self.pushButton_2.setText(_translate("MainWindow", "openpose路径"))
        self.comboBox.setItemText(0, _translate("MainWindow", "手部模型"))
        self.comboBox.setItemText(1, _translate("MainWindow", "身体部分模型"))
        self.label_3.setText(_translate("MainWindow", "预训练模型选择"))
        self.checkBox.setText(_translate("MainWindow", "是否检测手部"))
        self.checkBox_2.setText(_translate("MainWindow", "是否检测身体"))
        self.pushButton_4.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_5.setText(_translate("MainWindow", "直接导入json"))
        self.pushButton_6.setText(_translate("MainWindow", "合成视频"))
        self.pushButton_8.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_9.setText(_translate("MainWindow", "访问openpose"))
        self.pushButton_10.setText(_translate("MainWindow", "导出3d数据"))

