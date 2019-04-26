# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\马东徽\Desktop\new\new12\childrenform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv 
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(1040, 792)

        self.label = QtWidgets.QLabel(ChildrenForm)
        self.label.setGeometry(QtCore.QRect(180, 10, 220, 260))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(ChildrenForm)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 220, 260))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(ChildrenForm)
        self.label_3.setGeometry(QtCore.QRect(270, 290, 220, 260))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(ChildrenForm)
        self.label_4.setGeometry(QtCore.QRect(540, 290, 220, 260))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(ChildrenForm)
        self.label_5.setGeometry(QtCore.QRect(800, 290, 220, 260))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.cannybutton = QtWidgets.QPushButton(ChildrenForm)
        self.cannybutton.setGeometry(QtCore.QRect(320, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cannybutton.setFont(font)
        self.cannybutton.setObjectName("cannybutton")
        self.cannybutton.clicked.connect(ChildrenForm.Can_Image) #定义canny提取轮廓的槽函数

        self.histobutton = QtWidgets.QPushButton(ChildrenForm)
        self.histobutton.setGeometry(QtCore.QRect(590, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.histobutton.setFont(font)
        self.histobutton.setObjectName("histobutton")
        self.histobutton.clicked.connect(ChildrenForm.His_Image) #定义直方图均衡的槽函数

        self.threbutton = QtWidgets.QPushButton(ChildrenForm)
        self.threbutton.setGeometry(QtCore.QRect(880, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.threbutton.setFont(font)
        self.threbutton.setObjectName("threbutton")
        self.threbutton.clicked.connect(ChildrenForm.Thre_Image) #定义阈值分割槽函数

        self.graybutton = QtWidgets.QPushButton(ChildrenForm)
        self.graybutton.setGeometry(QtCore.QRect(50, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.graybutton.setFont(font)
        self.graybutton.setObjectName("graybutton")
        self.graybutton.clicked.connect(ChildrenForm.Gray_Image) #定义转灰度图的槽函数

        self.closebutton = QtWidgets.QPushButton(ChildrenForm)
        self.closebutton.setGeometry(QtCore.QRect(30, 150, 91, 41))
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(ChildrenForm.close)

        self.openbutton = QtWidgets.QPushButton(ChildrenForm)
        self.openbutton.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.openbutton.setObjectName("openbutton")
        self.openbutton.clicked.connect(ChildrenForm.openImage) #自己定义一个打开图片的槽连接

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def openImage(self): #自定义打开图片的槽函数
        imgName,imgType= QFileDialog.getOpenFileName(self, '打开图片')
        if imgName:
            self.captured = cv.imread(str(imgName))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)
            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            png = QPixmap.fromImage(QImg).scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(png)

    def Gray_Image(self): #将图像转换成灰度图
        self.gray = cv.cvtColor(self.captured, cv.COLOR_RGB2GRAY)
        rows, columns = self.gray.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.gray.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.label_2.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def Thre_Image(self): #Otsu自动阈值分割
        if not hasattr(self, "gray"):
            return
        _, self.thre = cv.threshold(self.gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        rows, columns = self.thre.shape
        bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.thre.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.label_5.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_5.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def Can_Image(self): #canny边缘提取
        self.can = cv.Canny(self.gray, 100, 200)
        rows, columns = self.can.shape
        bytesPerLine = columns
        # 轮廓提取图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.can.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.label_3.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_3.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def His_Image(self): #直方图均衡绘制
        self.his = cv.equalizeHist(self.gray)
        rows, columns = self.his.shape
        bytesPerLine = columns
        # 直方图均衡也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.his.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.label_4.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_4.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    
    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.label.setText(_translate("ChildrenForm", "原始图像"))
        self.label_2.setText(_translate("ChildrenForm", "灰度图转换"))
        self.cannybutton.setText(_translate("ChildrenForm", "Canny边缘检测"))
        self.histobutton.setText(_translate("ChildrenForm", "直方图均衡"))
        self.threbutton.setText(_translate("ChildrenForm", "阈值分割"))
        self.graybutton.setText(_translate("ChildrenForm", "灰度图转换"))
        self.closebutton.setText(_translate("ChildrenForm", "最小化窗口"))
        self.openbutton.setText(_translate("ChildrenForm", "打开图片"))
        self.label_3.setText(_translate("ChildrenForm", "canny边缘检测"))
        self.label_4.setText(_translate("ChildrenForm", "直方图均衡"))
        self.label_5.setText(_translate("ChildrenForm", "阈值分割"))

