import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5 import QtCore,QtWidgets,QtGui
from Ui_new13 import Ui_MainWindow
from Ui_childrenform import Ui_ChildrenForm
from Ui_childrenform2 import Ui_ChildrenForm2
from Ui_childrenform3 import Ui_ChildrenForm3
from Ui_childrenform4 import Ui_ChildrenForm4

class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

        self.child1 = ChildrenForm1()
        self.child2 = ChildrenForm2()
        self.child3 = ChildrenForm3()
        self.child4 = ChildrenForm4()

        self.open_file.triggered.connect(self.openMsg) #可以在没设置slot的情况下自己在主函数中自己设置槽连接
        self.close_file.triggered.connect(self.close)

        self.addWinAction.triggered.connect(self.childshow1) #设置添加子窗口的槽函数
        self.addWinAction2.triggered.connect(self.childshow2)
        self.addWinAction3.triggered.connect(self.childshow3)
        self.addWinAction4.triggered.connect(self.childshow4)

    def childshow1(self): #添加子窗口1
        self.MaingridLayout.addWidget(self.child1)
        self.child1.show()

    def childshow2(self): #添加子窗口2
        self.MaingridLayout.addWidget(self.child2)
        self.child2.show()

    def childshow3(self): #添加子窗口3
        self.MaingridLayout.addWidget(self.child3)
        self.child3.show()
    
    def childshow4(self): #添加子窗口4
        self.MaingridLayout.addWidget(self.child4)
        self.child4.show()

    def openMsg(self): #定义槽函数
        file,ok = QFileDialog.getOpenFileName(self, '打开','D:/', 'All Files (*);;Text Files (*.txt)')
        self.statusbar.showMessage(file)

class ChildrenForm1(QWidget,Ui_ChildrenForm): #声明子窗口1
    def __init__(self):
        super(ChildrenForm1,self).__init__()
        self.setupUi(self)

class ChildrenForm2(QWidget,Ui_ChildrenForm2): #声明子窗口2
    def __init__(self):
        super(ChildrenForm2,self).__init__()
        self.setupUi(self)

class ChildrenForm3(QWidget,Ui_ChildrenForm3): #声明子窗口3
    def __init__(self):
        super(ChildrenForm3,self).__init__()
        self.setupUi(self)

class ChildrenForm4(QWidget,Ui_ChildrenForm4): #声明子窗口4
    def __init__(self):
        super(ChildrenForm4,self).__init__()
        self.setupUi(self)

if __name__ == "__main__": #运行程序
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec_())