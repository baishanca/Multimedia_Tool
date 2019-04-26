# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\马东徽\Desktop\new\new13\childrenform2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os #导入os模块，建立文件夹储存截图
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time

class Ui_ChildrenForm2(object):
    def setupUi(self, ChildrenForm2):
        ChildrenForm2.setObjectName("ChildrenForm2")
        ChildrenForm2.resize(1011, 698)

        self.label = QtWidgets.QLabel(ChildrenForm2)
        self.label.setGeometry(QtCore.QRect(310, 60, 511, 321))
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(ChildrenForm2)
        self.label_2.setGeometry(QtCore.QRect(310, 440, 291, 201))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(ChildrenForm2)
        self.label_3.setGeometry(QtCore.QRect(640, 440, 291, 201))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(ChildrenForm2)
        self.label_5.setGeometry(QtCore.QRect(750, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.playbutton = QtWidgets.QPushButton(ChildrenForm2)
        self.playbutton.setGeometry(QtCore.QRect(100, 60, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.playbutton.setFont(font)
        self.playbutton.setObjectName("playbutton")
        self.playbutton.clicked.connect(ChildrenForm2.PlayVedio) #设置播放视频的槽连接

        self.framebutton = QtWidgets.QPushButton(ChildrenForm2)
        self.framebutton.setGeometry(QtCore.QRect(100, 245, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.framebutton.setFont(font)
        self.framebutton.setObjectName("framebutton")
        self.framebutton.clicked.connect(ChildrenForm2.FreVedio) #设置视频取帧槽连接

        self.displaybutton = QtWidgets.QPushButton(ChildrenForm2)
        self.displaybutton.setGeometry(QtCore.QRect(100, 430, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.displaybutton.setFont(font)
        self.displaybutton.setObjectName("displaybutton")
        self.displaybutton.clicked.connect(ChildrenForm2.Display_Img) #设置打开图片槽连接

        self.closebutton = QtWidgets.QPushButton(ChildrenForm2)
        self.closebutton.setGeometry(QtCore.QRect(100, 560, 91, 41))
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(ChildrenForm2.close) #最小化窗口槽连接

        self.retranslateUi(ChildrenForm2)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm2)

    def PlayVedio(self): 
        global videoName #在这里设置全局变量以便在线程中使用
        videoName,videoType= QFileDialog.getOpenFileName(self, "打开视频")
        #cap = cv.VideoCapture(str(videoName))
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def FreVedio(self):
        os.mkdir(r'D:/vedioshut/') #在D盘建立目录vedioshut储存截取图像
        vc = cv.VideoCapture(videoName) #读入视频文件
        times = 0
        timeF = 15

        while True:
            times+=1
            res, image = vc.read()
            if not res:
                print('not res , not image')
                break
            if times%timeF == 0:
                cv.imwrite('D:\\vedioshut\\' + str(times)+'.jpg', image)
                print('D:\\vedioshut\\' + str(times)+'.jpg')
        print('图片提取结束')

    def Display_Img(self): #打开截图并展示
        imgName,imgType= QFileDialog.getOpenFileName(self, '打开图片','D:\\vedioshut\\')
        if imgName:
            self.captured = cv.imread(str(imgName))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)
            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            png = QPixmap.fromImage(QImg).scaled(self.label_3.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label_3.setPixmap(png)



    def retranslateUi(self, ChildrenForm2):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm2.setWindowTitle(_translate("ChildrenForm2", "Form"))


        self.label_5.setText(_translate("ChildrenForm2", "按帧截图"))
        self.playbutton.setText(_translate("ChildrenForm2", "播放视频"))
        self.framebutton.setText(_translate("ChildrenForm2", "按帧截取"))
        self.displaybutton.setText(_translate("ChildrenForm2", "显示图片"))
        self.closebutton.setText(_translate("ChildrenForm2", "最小化窗口"))

    

class Thread(QThread):#采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)
    def run(self):
        cap = cv.VideoCapture(videoName)
        while (cap.isOpened()==True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)#在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(511,321, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.changePixmap.emit(p)
                time.sleep(0.01) #控制视频播放的速度
            else:
                break