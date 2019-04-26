# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\马东徽\Desktop\new\new13\childrenform4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Huff import *
import numpy as np


class Ui_ChildrenForm4(object):
    def setupUi(self, ChildrenForm4):
        ChildrenForm4.setObjectName("ChildrenForm4")
        ChildrenForm4.resize(874, 597)

        self.textEdit = QtWidgets.QTextEdit(ChildrenForm4)
        self.textEdit.setGeometry(QtCore.QRect(320, 90, 550, 121))
        self.textEdit.setObjectName("textEdit")

        self.openbutton = QtWidgets.QPushButton(ChildrenForm4)
        self.openbutton.setGeometry(QtCore.QRect(110, 80, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.openbutton.setFont(font)
        self.openbutton.setObjectName("openbutton")
        self.openbutton.clicked.connect(ChildrenForm4.loadtxt) #打开密码本的槽连接

        self.button1 = QtWidgets.QPushButton(ChildrenForm4)
        self.button1.setGeometry(QtCore.QRect(110, 180, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(ChildrenForm4.compress_1) #重复抑制的槽连接

        self.button2 = QtWidgets.QPushButton(ChildrenForm4)
        self.button2.setGeometry(QtCore.QRect(110, 290, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(ChildrenForm4.compress_2) #模式替换的槽连接

        self.button3 = QtWidgets.QPushButton(ChildrenForm4)
        self.button3.setGeometry(QtCore.QRect(110, 410, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(ChildrenForm4.compress_3) #霍夫曼编码的槽连接

        self.textEdit_2 = QtWidgets.QTextEdit(ChildrenForm4)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 350, 550, 121))
        self.textEdit_2.setObjectName("textEdit_2")

        self.closebutton = QtWidgets.QPushButton(ChildrenForm4)
        self.closebutton.setGeometry(QtCore.QRect(110, 510, 91, 31))
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(ChildrenForm4.close) #最小化窗口的槽连接

        self.retranslateUi(ChildrenForm4)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm4)


    def loadtxt(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        global data #定义全局变量data，后面的各种压缩算法需要使用
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def compress_1(self): #重复抑制压缩算法
        string = data
        compressed = ""
        count = 0
        temp = string[0]
        for i in range(0 ,len(string)):
            if temp == string[i]:
                count = count + 1			
            else:
                compressed = compressed + str(temp) +str(count)
                count = 1
                temp = string[i]
    
            if i == len(string)-1:
                compressed = compressed + str(temp) +str(count)
        self.textEdit_2.setText(compressed)


    def compress_2(self): #模式替换算法
        string = data
        message = string.replace('and','&')
        self.textEdit_2.setText(message)

    def compress_3(self): #调用霍夫曼编码算法
        string = data
        t = nodeQeuen(freChar(string))
        tree = creatHuffmanTree(t)
        HuffmanCodeDic(tree, '')
        codemode = str(codeDic1) #将字典转换为字符串（很重要，调试bug调了很久，最后发现是数据类型原因）
        self.textEdit_2.setText(codemode)
        print(codeDic1)



    def retranslateUi(self, ChildrenForm4):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm4.setWindowTitle(_translate("ChildrenForm4", "Form"))
        self.openbutton.setText(_translate("ChildrenForm4", "打开文本"))
        self.button1.setText(_translate("ChildrenForm4", "重复抑制"))
        self.button2.setText(_translate("ChildrenForm4", "模式替换"))
        self.button3.setText(_translate("ChildrenForm4", "霍夫曼编码"))
        self.closebutton.setText(_translate("ChildrenForm4", "最小化窗口"))

codeDic1 = {}
codeDic2 = {}
# 由huffman树得到Huffman编码表
def HuffmanCodeDic(head, x): #不能在类内创建函数，否则会报错HuffmanCodeDic() takes 2 positional arguments but 3 were given
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x+'0')
        head.code += x
        if head.val:
            codeDic2[head.code] = head.val
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x+'1')