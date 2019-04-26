# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\马东徽\Desktop\new\new13\childrenform3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os #建立文件夹储存处理后的音频文件
from PyQt5.QtMultimedia import QSound #引入Qsound播放音频
from pydub import AudioSegment #在这里，我们用ffmpeg和pydub处理音频
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class Ui_ChildrenForm3(object):
    def setupUi(self, ChildrenForm3):
        ChildrenForm3.setObjectName("ChildrenForm3")
        ChildrenForm3.resize(916, 617)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        ChildrenForm3.setFont(font)

        self.closebutton = QtWidgets.QPushButton(ChildrenForm3)
        self.closebutton.setGeometry(QtCore.QRect(770, 540, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.closebutton.setFont(font)
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(ChildrenForm3.close) #最小化程序窗口

        self.textEdit = QtWidgets.QTextEdit(ChildrenForm3)
        self.textEdit.setGeometry(QtCore.QRect(250, 370, 381, 41))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(ChildrenForm3)
        self.widget.setGeometry(QtCore.QRect(250, 450, 381, 109))
        self.widget.setObjectName("widget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.process1 = QtWidgets.QPushButton(self.widget)
        self.process1.setObjectName("process1")
        self.verticalLayout_2.addWidget(self.process1)
        self.process1.clicked.connect(ChildrenForm3.reverse) #音频翻转

        self.process2 = QtWidgets.QPushButton(self.widget)
        self.process2.setObjectName("process2")
        self.verticalLayout_2.addWidget(self.process2)
        self.process2.clicked.connect(ChildrenForm3.convert) #转换成MP3格式

        self.process3 = QtWidgets.QPushButton(self.widget)
        self.process3.setObjectName("process3")
        self.verticalLayout_2.addWidget(self.process3)
        self.process3.clicked.connect(ChildrenForm3.volumeadj) #调整音频前半段，后半段音量并拼接

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.startbutton = QtWidgets.QPushButton(self.widget)
        self.startbutton.setObjectName("startbutton")
        self.horizontalLayout.addWidget(self.startbutton)
        self.startbutton.clicked.connect(ChildrenForm3.playwav)  #播放wav文件


        self.stopbutton = QtWidgets.QPushButton(self.widget)
        self.stopbutton.setObjectName("stopbutton")
        self.horizontalLayout.addWidget(self.stopbutton)
        self.stopbutton.clicked.connect(ChildrenForm3.stopwav)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.openbutton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.openbutton.setFont(font)
        self.openbutton.setObjectName("openbutton")
        self.openbutton.clicked.connect(ChildrenForm3.openfile)

        self.verticalLayout.addWidget(self.openbutton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ChildrenForm3)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm3)

    
    def openfile(self): #打开音频文件的函数
        global sound #定义全局变量sound供后面的音频处理函数使用
        global message
        Name,Type= QFileDialog.getOpenFileName(self, '打开音频')
        message = str(Name)
        sound = QSound(message)
        self.textEdit.setText(message)

    def playwav(self):  #播放wav文件的函数
        sound.play()
    
    def stopwav(self):  #停止wav文件播放
        sound.stop()

    def reverse(self):
        path = 'D:/audioprocess/'
        folder = os.path.exists(path)
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹,用于存储处理后的音频文件
            os.mkdir(r'D:/audioprocess/')

        song = AudioSegment.from_file(message, format='wav') #生成Audiosegment对象
        backward = song.reverse()
        backward.export("D:/audioprocess/reverse.wav", format="wav")
        address1 = 'D:/audioprocess/reverse.wav'
        QSound.play(address1) #这里遇到了一个神奇的bug,之前的方案是sound1=Qsound(address1),然后sound1.play(),一直出不了声音

    def convert(self):
        song1 = AudioSegment.from_file(message, format = 'wav') #再次生成Audiosegment对象
        song1.export("D:/audioprocess/convert.mp3", format='mp3') #转化为MP3格式

    def volumeadj(self): #音频前两秒增加6分贝，后两秒降低3分贝，将音频剪辑为4秒
        song2 = AudioSegment.from_file(message, format='wav')
        first_2_seconds = song2[:2000]
        last_2_second = song2[-2000:]
        beginning = first_2_seconds + 6
        end = last_2_second -3
        plus = beginning + end
        plus.export("D:/audioprocess/plus.wav", format="wav")
        address2 = 'D:/audioprocess/plus.wav'
        QSound.play(address2)

    def retranslateUi(self, ChildrenForm3):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm3.setWindowTitle(_translate("ChildrenForm3", "Form"))
        self.closebutton.setText(_translate("ChildrenForm3", "最小化程序"))
        self.process1.setText(_translate("ChildrenForm3", "音频翻转"))
        self.process2.setText(_translate("ChildrenForm3", "wav转MP3"))
        self.process3.setText(_translate("ChildrenForm3", "音量局部调整"))
        self.startbutton.setText(_translate("ChildrenForm3", "开始播放"))
        self.stopbutton.setText(_translate("ChildrenForm3", "停止播放"))
        self.openbutton.setText(_translate("ChildrenForm3", "打开音频"))