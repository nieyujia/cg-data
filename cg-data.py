# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import  QHBoxLayout,QApplication,QToolTip,QPushButton,QWidget
import numpy as np
from numpy import *
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont
####################系统密码

#############################################################
##########表格##########
class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("商品信息表格界面")
        # 设置窗口尺寸

        self.resize(600,500)


        # 创建QStandardItemModel对象  4行3列

        file = open('goods','r')
        i=0
        for l in file.readlines():
            i=i+1
        file.close()

        self.model = QStandardItemModel(i,4)
        # 设置字段
        self.model.setHorizontalHeaderLabels(['商品名称','时间','数量','价格'])

        # 创建QTableView控件
        self.tableview = QTableView()

        # 关联模型
        self.tableview.setModel(self.model)


        # 添加数据

        i=0
        file = open('goods','r')
        for l in file.readlines():
            a=l.split()

            item1 = QStandardItem(a[0])
            itme2 = QStandardItem(a[1])
            item3 = QStandardItem(a[2])
            item4 = QStandardItem(a[3])
            #  第一行第一列
            self.model.setItem(i,0,item1)
            #  第一行第二列
            self.model.setItem(i,1,itme2)
            #  第一行第三列
            self.model.setItem(i,2,item3)
            self.model.setItem(i,3,item4)
            i=i+1






        # 创建垂直布局
        layout = QVBoxLayout()

        # 把控件添加到布局里
        layout.addWidget(self.tableview)

        # 应用于垂直布局
        self.setLayout(layout)









############################################################
##三层系统界面
#用户升级权限
class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(816, 642)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 110, 200, 80))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 380, 171, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(330, 260, 221, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 270, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 380, 181, 71))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.high)

    def high(self):
        key ='tobe'
        if(self.lineEdit.text()!=key):
            QMessageBox.information(MainWindow, "提示窗口", '系统密码错误！', QMessageBox.Ok)
            self.lineEdit.clear()
            high.close()
        else:



            f = open('admin', 'a')
            f.write(ui.lineEdit.text() + ' ')
            f.write(ui.lineEdit_3.text() + '\n')
            f.close()
            QMessageBox.information(MainWindow, "提示窗口", '升级成功！'+ui.lineEdit.text()+'用户！', QMessageBox.Ok)
            self.lineEdit.clear()
            file = open('user', 'r')
            app = []
            for l in file.readlines():
                if (l != ui.lineEdit.text()+' '+ui.lineEdit_3.text()+'\n'):
                    app.append(l)
            file.close()
            file = open('user', 'w')
            for i in app:
                file.write(i)
            high.close()
            mainus.close()










    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "升级权限"))
        self.label_4.setText(_translate("Form", "升级权限"))
        self.pushButton_5.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "系统密码："))
        self.pushButton.setText(_translate("Form", "确定"))







#####################################################################
########################################################
######注销-用户界面
class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 357)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 50, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 180, 171, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 180, 181, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.dele)
        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def dele(self):
        file = open('user', 'r')
        app = []
        for l in file.readlines():
            if (l != ui.lineEdit.text() + ' ' + ui.lineEdit_3.text() + '\n'):
                app.append(l)
        file.close()
        file = open('user', 'w')
        for i in app:
            file.write(i)
        QMessageBox.information(MainWindow, "提示窗口", '注销成功！即将返回登陆界面', QMessageBox.Ok)
        ui.lineEdit.clear()
        ui.lineEdit_3.clear()
        delete.close()
        mainus.close()






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户注销"))
        self.label_4.setText(_translate("Form", "确认注销？"))
        self.pushButton_5.setText(_translate("Form", "返回"))
        self.pushButton.setText(_translate("Form", "确定"))
#######################################################
######注销-管理员界面
class Ui_Form7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 357)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 30, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 180, 171, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 180, 181, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.dele1)
        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def dele1(self):
        file = open('admin', 'r')
        app = []
        for l in file.readlines():
            if (l != ui.lineEdit.text() + ' ' + ui.lineEdit_3.text() + '\n'):
                app.append(l)
        file.close()
        print(ui.lineEdit.text())
        print(ui.lineEdit_3.text())
        print(app)
        file = open('admin', 'w')
        for i in app:
            file.write(i)
        QMessageBox.information(MainWindow, "提示窗口", '注销成功！即将返回登陆界面', QMessageBox.Ok)
        ui.lineEdit.clear()
        ui.lineEdit_3.clear()
        delete1.close()
        mainad.close()






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员注销"))
        self.label_4.setText(_translate("Form", "确认注销？"))
        self.pushButton_5.setText(_translate("Form", "返回"))
        self.pushButton.setText(_translate("Form", "确定"))
#######################################################
#登陆界面-管理员
class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 15, 400, 300))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 510, 191, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(130, 160, 541, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

# 按钮
        self.pushButton.clicked.connect(self.future)
        self.pushButton_4.clicked.connect(self.view)
        self.pushButton_5.clicked.connect(self.quit)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.change)
##功能函数
    def quit(self):
        mainad.close()
        ui.lineEdit_3.clear()
    def delete(self):
        delete1.show()
    def view(self):
        self.table = TableView()
        self.table.show()
    def future(self):
        future.show()
    def change(self):
        change.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员界面"))
        self.label_4.setText(_translate("Form", "管理员界面"))
        self.pushButton_5.setText(_translate("Form", "退出"))
        self.pushButton.setText(_translate("Form", "查看商品和预测信息"))
        self.pushButton_4.setText(_translate("Form", "查看总商品信息"))
        self.pushButton_3.setText(_translate("Form", "增删商品信息"))
        self.pushButton_2.setText(_translate("Form", "注销账户"))
#####################################################
#登录界面-用户
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 50, 300, 150))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 510, 191, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(130, 160, 541, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
# 按钮
        self.pushButton_3.clicked.connect(future.show)
        self.pushButton_4.clicked.connect(self.view)
        self.pushButton_5.clicked.connect(self.quit)
        self.pushButton.clicked.connect(self.high)
        self.pushButton_2.clicked.connect(self.delete)
##功能函数

    def quit(self):
        mainus.close()
        ui.lineEdit_3.clear()
    def high(self):
        high.show()
    def delete(self):
        delete.show()
    def view(self):
        self.table = TableView()
        self.table.show()





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户界面"))
        self.label_4.setText(_translate("Form", "用户界面"))
        self.pushButton_5.setText(_translate("Form", "退出"))
        self.pushButton.setText(_translate("Form", "升级权限"))
        self.pushButton_4.setText(_translate("Form", "查看总表格信息"))
        self.pushButton_3.setText(_translate("Form", "查看商品和预测信息"))
        self.pushButton_2.setText(_translate("Form", "注销账户"))

#####################################################
#注册页面
class Ui_Form3(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 80, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 510, 151, 61))
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 510, 161, 61))
        self.pushButton_2.setObjectName("pushButton_2")


        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(140, 190, 491, 291))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
#退出键

        self.pushButton_2.clicked.connect(self.quit)

#注册键
        self.pushButton.clicked.connect(self.create)





############################
#功能函数
    def quit(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        create.close()
    def create(self):


        if(self.lineEdit_2.text()!=self.lineEdit_3.text()):
            QMessageBox.information(MainWindow, "提示窗口", '两次密码输入不一致！', QMessageBox.Ok)
        elif(self.lineEdit.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入用户名！', QMessageBox.Ok)
        elif (self.lineEdit_2.text() == ''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入密码！', QMessageBox.Ok)
        else:
            i=1
            sign=0
            file = open('user', 'r')

            for line in file.readlines():
                    b=line.split()
                    if(b==[]):
                        break
                    if(self.lineEdit.text()==b[0]):
                        QMessageBox.information(MainWindow, "提示窗口", '已存在此账户！', QMessageBox.Ok)
                        sign=1
            if(sign==0):
                f = open('user','a')
                f.write(self.lineEdit.text() + ' ')
                f.write(self.lineEdit_2.text() + '\n')
                f.close()
                QMessageBox.information(MainWindow, "提示窗口", '注册成功！', QMessageBox.Ok)
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                create.close()
    #####################################



    #通用部分
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册页面"))
        self.label_4.setText(_translate("Form", "注册用户"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.pushButton_2.setText(_translate("Form", "退出注册"))
        self.label.setText(_translate("Form", "用户名"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "确认密码"))

#####################################################


#主窗口
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1012, 661)
        Form.setMinimumSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setWindowTitle('库存管理系统')


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 20, 441, 181))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 160, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(370, 430, 115, 19))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(500, 430, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(True)

        self.radioButton.toggled.connect(self.select)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radioButton_2.clicked.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(270, 280, 421, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)


        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(13, 13))
        self.lineEdit.setMaximumSize(QtCore.QSize(100000, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(13, 13))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100000, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(320, 460, 321, 102))
        self.widget1.setObjectName("widget1")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setMinimumSize(QtCore.QSize(140, 70))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setStyleSheet("font: 9pt \"造字工房悦黑体验版细体\";\n"
"image: url(:/ico/login.ico);\n"
"background-color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(140, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3.setBuddy(self.lineEdit)
        self.pushButton_2.setStyleSheet("font: 9pt \"造字工房悦黑体验版细体\";\n"
                                      "image: url(:/ico/login.ico);\n"
                                      "background-color: rgb(0, 255, 0);\n"
                                      "color: rgb(0, 0, 0);")


        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 560, 150, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("font: 9pt \"造字工房悦黑体验版细体\";\n"
                                      "image: url(:/ico/login.ico);\n"
                                      "background-color: rgb(255, 255, 0);\n"
                                      "color: rgb(255, 0, 0);")

        self.pushButton_3.clicked.connect(self.create)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)





#功能函数
    def select(self):
        if self.radioButton.isChecked():
            QMessageBox.information(MainWindow, "提示", "您选择的是 管理员 登录", QMessageBox.Ok)
        else:
            QMessageBox.information(MainWindow, "提示", "您选择的是 普通用户 登录", QMessageBox.Ok)


    def login(self):
        file = open('admin', 'r')
        files = open('user', 'r')
        if(self.lineEdit.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入用户名！', QMessageBox.Ok)
            return 0
        elif(self.lineEdit_3.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入密码！', QMessageBox.Ok)
            return 0

        if self.radioButton.isChecked():
            sign=0
            for line in file.readlines():
                b=line.split()
                if(self.lineEdit.text()==b[0]):
                        if(self.lineEdit_3.text()==b[1]):
                            QMessageBox.information(MainWindow, "结果窗口", "成功登陆管理员！ ", QMessageBox.Ok)
                            sign=1
                            mainad.show()
                        else:
                            QMessageBox.information(MainWindow, "结果窗口", "密码错误！ ", QMessageBox.Ok)
                            return 0
            if(sign==0):
                QMessageBox.information(MainWindow, "结果窗口", "不存在此用户名！ ", QMessageBox.Ok)



        elif self.radioButton_2.isChecked():

            sign=0
            for line in files.readlines():
                b=line.split()
                if(self.lineEdit.text()==b[0]):
                        if(self.lineEdit_3.text()==b[1]):
                            QMessageBox.information(MainWindow, "结果窗口", "成功登陆用户！！ ", QMessageBox.Ok)
                            sign=1
                            mainus.show()
                        else:
                            QMessageBox.information(MainWindow, "结果窗口", "密码错误！ ", QMessageBox.Ok)
                            return 0
            if(sign==0):
                QMessageBox.information(MainWindow, "结果窗口", "不存在此用户名！ ", QMessageBox.Ok)




    def create(self):
        create.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label.setText(_translate("Form", "库存管理系统"))
        self.label_2.setText(_translate("Form", "登录界面"))
        self.radioButton.setText(_translate("Form", "管理员身份"))
        self.radioButton_2.setText(_translate("Form", "用户身份"))
        self.label_4.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "用户名"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.pushButton_3.setText(_translate("Form", "注册"))

################################
#预测界面
class Ui_Form8(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 525)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 320, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 90, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 180, 231, 91))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 420, 321, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 320, 141, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.prodict)


    def prodict(self):
        n = []
        p = []
        aven = 0
        avep = 0
        if(self.lineEdit.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", "请输入商品名称！ ", QMessageBox.Ok)
        else:
            file = open('goods','r')
            s = self.lineEdit.text()

            for l in file.readlines():
                a = l.split()
                if(s==a[0]):
                    b = int(a[2])
                    n.append(b)
                    b = int(a[3])
                    p.append(b)
            if(n==[]):
                QMessageBox.information(MainWindow, "提示窗口", "无此商品！ ", QMessageBox.Ok)
                return 0
            str1 = ''.join(str(i)+' ' for i in n)
            s1 = '此商品的历史库存：'+str1
            str2 = ''.join(str(i)+' ' for i in p)
            s2 = '此商品的历史库存：'+str2
            aven = mean(n)
            avep = mean(p)
            avn = str(aven)
            avp = str(avep)
            s3 = "预测库存和价格："+avn+'和'+avp
            QMessageBox.information(MainWindow, "提示窗口", s1+'\n'+s2+'\n'+s3, QMessageBox.Ok)
            self.lineEdit.clear()




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "商品信息界面"))
        self.pushButton.setText(_translate("Form", "预测"))
        self.label.setText(_translate("Form", "输入商品名称"))
        self.label_2.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "退出"))

######################################
#增删界面
class Ui_Form9(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 683)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 490, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 90, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 580, 141, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(620, 70, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(490, 300, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 180, 211, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 380, 231, 71))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 480, 161, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 190, 381, 261))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_3.clicked.connect(self.view)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_4.clicked.connect(self.dele)


    def view(self):
        self.table = TableView()
        self.table.show()

    def add(self):
        if(self.lineEdit.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入名称！', QMessageBox.Ok)
        elif(self.lineEdit_2.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入日期！', QMessageBox.Ok)
        elif(self.lineEdit_3.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入库存！', QMessageBox.Ok)
        elif(self.lineEdit_4.text()==''):
            QMessageBox.information(MainWindow, "提示窗口", '请输入价格！', QMessageBox.Ok)
        else:
            file = open('goods','a')
            file.write(self.lineEdit.text() + ' ')
            file.write(self.lineEdit_2.text() + ' ')
            file.write(self.lineEdit_3.text() + ' ')
            file.write(self.lineEdit_4.text() + '\n')
            QMessageBox.information(MainWindow, "提示窗口", '添加成功！', QMessageBox.Ok)
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()



    def dele(self):
        a = int(self.lineEdit_5.text())

        file = open('goods','r')
        lines = file.readlines()
        num = len(lines)
        if(a<1 or a>num):
            QMessageBox.information(MainWindow, "提示窗口", '没有指定行！', QMessageBox.Ok)
            return 0
        del lines[a-1]  # 删除最后一行
        file.close()

        file_new = open('goods', 'w')
        file_new.writelines(lines)  # 将删除行后的数据写入文件
        file_new.close()
        QMessageBox.information(MainWindow, "提示窗口", '删除成功！', QMessageBox.Ok)
        self.lineEdit_5.clear()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "增删界面"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "增加"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.label_6.setText(_translate("Form", "删除"))
        self.label_7.setText(_translate("Form", "输入删除的序号"))
        self.pushButton_3.setText(_translate("Form", "查看列表"))
        self.pushButton_4.setText(_translate("Form", "删除"))
        self.label_2.setText(_translate("Form", "名称"))
        self.label_3.setText(_translate("Form", "日期"))
        self.label_4.setText(_translate("Form", "库存"))
        self.label_5.setText(_translate("Form", "价格"))

###########################################
#主程序
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)


   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   mainad = QtWidgets.QMainWindow()
   mainus = QtWidgets.QMainWindow()
   create = QtWidgets.QMainWindow()
   high = QtWidgets.QMainWindow()
   delete = QtWidgets.QMainWindow()
   delete1 = QtWidgets.QMainWindow()
   table = TableView()
   future = QtWidgets.QMainWindow()
   change = QtWidgets.QMainWindow()

   ui = Ui_Form() # 创建PyQt设计的窗体对象 *******************
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置

   uo = Ui_Form1()
   uo.setupUi(mainad)

   up = Ui_Form2()
   up.setupUi(mainus)

   uq  = Ui_Form3()
   uq.setupUi(create)

   uw = Ui_Form5()
   uw.setupUi(high)

   ue = Ui_Form6()
   ue.setupUi(delete)

   ur = Ui_Form7()
   ur.setupUi(delete1)

   ut = Ui_Form8()
   ut.setupUi(future)

   uy =Ui_Form9()
   uy.setupUi(change)






   MainWindow.show() # 显示窗体

   sys.exit(app.exec_()) # 程序关闭时退出进程