# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import cv2 as cv
from time import time
import numpy as np
import datetime
import logging

from configparser import ConfigParser
from database import original_event_counter,doSql,event_insert,state_insert,original_event_insert_all,study_state_insert_all

from posture import postureFrameDetectCopy as posture_detect
from fatigue import fatigueFrameDetect as fatigue_detect
from concentration import concentrationFrameDetect as concentration_detect
from emotion import emotionFrameDetect as emotion_detect
from emotion import emotion_db_dic
from emotion import faceDetectorVideo_dlib as face_detect

#该方法参考博客https://blog.csdn.net/weixin_45896213/article/details/125600170
class MyConf(ConfigParser):
    def __init__(self,  filename,encoding):
        #初始化父类对象
        super().__init__()
        #读取配置文件，自定义类的构造函数
        self.read(filename, encoding=encoding)

db = MyConf("db.ini","utf-8")  # 实例化配置文件对象，读取配置文件
menu = MyConf('menu.ini', "utf-8")



class Ui_Login:
    def __init__(self):
        super().__init__()  # 调用父类QMainWindow的初始化函数
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('lib/login.ui')
        self.ui.setWindowTitle('登录页')

        self.ui.setFixedSize(530, 405)
        self.ui.pushButton_2.clicked.connect(self.online_learning)
        self.ui.pushButton.clicked.connect(self.register_window)

    def online_learning(self):
        account=self.ui.lineEdit.text()
        passwd=self.ui.lineEdit_2.text()
        if  account == ''or passwd == '':
            QMessageBox.about(self.ui, '错误', '账号密码不能为空！')
        else:
            print('账号{}密码{}'.format(account, passwd))
            sql = f'''
                use online_learning;
                select * from student_info where student_id={account};
                '''
            #print(sql)
            stu_info=doSql(sql,option='query')
            print(stu_info)
            if stu_info==[]:
                QMessageBox.about(self.ui, '错误', '账号不存在！请注册！')
            elif passwd==stu_info[0][0][3]:
                print(stu_info[0][0][3])
                # 实例化另外一个窗口
                self.window3 = MainCode()
                # 显示新窗口
                self.window3.show()
                #self.window3 = Ui_Login()
                #self.window3.ui.show()
                sql = f'''
                        use online_learning;
                        select parent_name from parent_info where student_id={account};
                        '''
                # print(sql)
                stu_info = doSql(sql, option='query')
                if stu_info==[]:
                    QMessageBox.about(self.ui, '错误', '家长端未注册！请移步家长注册')
                else:
                    parent_name=stu_info[0][0][0]
                    print(parent_name)
                    self.window3.label_32.setText(parent_name)#家长姓名
                    self.window3.label_34.setText(account)#学生账号
                    # 关闭自己
                    self.ui.close()
            else:
                QMessageBox.about(self.ui, '错误', '密码错误')

    def register_window(self):

        # 实例化另外一个窗口
        self.window2 = Ui_Register()
        # 显示新窗口
        self.window2.ui.show()
        # 关闭自己
        self.ui.close()

class Ui_Register():
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('lib/register.ui')
        self.ui.setWindowTitle('注册页')

        self.ui.setFixedSize(530, 405)
        self.ui.pushButton.clicked.connect(self.back_login)
        self.ui.pushButton_2.clicked.connect(self.register_success)
    def back_login(self):
        # 实例化另外一个窗口
        self.window = Ui_Login()
        # 显示新窗口
        self.window.ui.show()
        # 关闭自己
        self.ui.close()
    def register_success(self):
        name = self.ui.lineEdit.text()
        account = self.ui.lineEdit_2.text()
        passwd_1 = self.ui.lineEdit_3.text()
        passwd_2 = self.ui.lineEdit_4.text()
        gender = ''
        if self.ui.radioButton.isChecked():
            gender = 'man'
        elif self.ui.radioButton_2.isChecked():
            gender = 'woman'

        print('name={}account={}passwd_1={}passwd_2={}gender={}'.format(name,account,passwd_1,passwd_2,gender))
        if name=='' or account==''or passwd_1=='' or passwd_2=='' or gender=='':
            QMessageBox.about(self.ui, '错误', '选项不能为空！')
        elif passwd_1!=passwd_2:
            QMessageBox.about(self.ui, '错误', '密码不一致！')
        elif len(passwd_1)<6:
            QMessageBox.about(self.ui, '错误', '密码不能少于6位！')
        else:
            sql = f'''
                        use online_learning;
                        select * from student_info where student_id={account};
                        '''
            # print(sql)
            stu_info = doSql(sql, option='query')
            print(stu_info)
            if stu_info != []:
                QMessageBox.about(self.ui, '错误', '账号已占用！请重新输入账号名！')
                #print(stu_info[0][0][3])
            else:
                sql = f'''
                        use online_learning;
                        INSERT INTO student_info(student_id,student_name,student_sex,student_pswd)VALUES({account},'{name}','{gender}',{passwd_1});
                        '''
                print(sql)
                is_connect=doSql(sql,option = 'others')#若插入成功函数会有返回值
                if is_connect==[]:
                    QMessageBox.about(self.ui, "错误", "操作数据库失败！请联系管理员！")
                else:
                    QMessageBox.about(self.ui, "提示", "注册成功！请返回继续登录！")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1170, 698)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.actionContact_us = QAction(MainWindow)
        self.actionContact_us.setObjectName(u"actionContact_us")


        self.actionManual.triggered.connect(self.manual)
        self.actionGithub.triggered.connect(self.github)
        self.actionContact_us.triggered.connect(self.contact_us)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setWindowTitle('主页')
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(100, 200))
        self.groupBox_4.setMaximumSize(QSize(100, 16777215))
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 60, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 70, 60, 30))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 110, 60, 30))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 160, 60, 30))
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setMinimumSize(QSize(100, 125))
        self.groupBox_5.setMaximumSize(QSize(100, 16777215))
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QRect(10, 30, 87, 18))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox_2 = QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QRect(10, 60, 87, 18))
        self.checkBox_2.setChecked(True)
        self.checkBox_3 = QCheckBox(self.groupBox_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QRect(10, 90, 87, 18))
        self.checkBox_3.setChecked(True)
        self.checkBox_4 = QCheckBox(self.groupBox_5)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QRect(10, 120, 87, 18))
        self.checkBox_4.setChecked(True)

        self.verticalLayout.addWidget(self.groupBox_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")
        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.label_31)
        self.horizontalLayout_7.addWidget(self.label_32)
        self.horizontalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_7.addWidget(self.label_33)
        self.horizontalLayout_7.addWidget(self.label_34)
        self.horizontalLayout_7.addWidget(self.line_3)
        self.horizontalLayout_7.addWidget(self.label_35)
        self.horizontalLayout_7.addWidget(self.label_36)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        #self.graphicsView = QGraphicsView(self.centralwidget)
        #self.graphicsView.setObjectName(u"graphicsView")

        #self.verticalLayout_2.addWidget(self.graphicsView)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.img_label = QLabel(self.centralwidget)
        self.img_label.resize(720,1280)
        # self.img_label.setGeometry(QRect(0, 0, 640, 480))
        self.img_label.setObjectName("img_label")

        self.verticalLayout_2.addWidget(self.img_label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(200, 0))
        self.groupBox_6.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(180, 30))
        self.groupBox_2.setMaximumSize(QSize(180, 100))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 30, 63, 14))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_11 = QLineEdit(self.groupBox_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setGeometry(QRect(80, 30, 81, 20))
        self.lineEdit_11.setAlignment(Qt.AlignCenter)
        self.lineEdit_12 = QLineEdit(self.groupBox_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QRect(80, 60, 81, 20))
        self.lineEdit_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 60, 63, 14))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(180, 30))
        self.groupBox.setMaximumSize(QSize(180, 120))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-1, 28, 63, 14))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-1, 58, 63, 14))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_21 = QLineEdit(self.groupBox)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_21.setGeometry(QRect(80, 20, 81, 20))
        self.lineEdit_21.setAlignment(Qt.AlignCenter)
        self.lineEdit_22 = QLineEdit(self.groupBox)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QRect(80, 60, 81, 20))
        self.lineEdit_22.setAlignment(Qt.AlignCenter)
        self.lineEdit_23 = QLineEdit(self.groupBox)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setEnabled(False)
        self.lineEdit_23.setGeometry(QRect(80, 90, 81, 20))
        self.lineEdit_23.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 90, 63, 14))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(180, 30))
        self.groupBox_3.setMaximumSize(QSize(16777215, 270))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 63, 14))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 63, 14))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 150, 63, 14))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 120, 63, 14))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 190, 63, 14))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 220, 63, 14))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.lineEdit_32 = QLineEdit(self.groupBox_3)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setEnabled(False)
        self.lineEdit_32.setGeometry(QRect(90, 60, 81, 20))
        self.lineEdit_32.setAlignment(Qt.AlignCenter)
        self.lineEdit_33 = QLineEdit(self.groupBox_3)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setGeometry(QRect(90, 90, 81, 20))
        self.lineEdit_33.setAlignment(Qt.AlignCenter)
        self.lineEdit_34 = QLineEdit(self.groupBox_3)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_34.setGeometry(QRect(90, 120, 81, 20))
        self.lineEdit_34.setAlignment(Qt.AlignCenter)
        self.lineEdit_35 = QLineEdit(self.groupBox_3)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setEnabled(False)
        self.lineEdit_35.setGeometry(QRect(90, 150, 81, 20))
        self.lineEdit_35.setAlignment(Qt.AlignCenter)
        self.lineEdit_36 = QLineEdit(self.groupBox_3)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setEnabled(False)
        self.lineEdit_36.setGeometry(QRect(90, 190, 81, 20))
        self.lineEdit_36.setAlignment(Qt.AlignCenter)
        self.lineEdit_37 = QLineEdit(self.groupBox_3)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setEnabled(False)
        self.lineEdit_37.setGeometry(QRect(90, 220, 81, 20))
        self.lineEdit_37.setAlignment(Qt.AlignCenter)
        self.lineEdit_31 = QLineEdit(self.groupBox_3)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setEnabled(False)
        self.lineEdit_31.setGeometry(QRect(90, 30, 81, 20))
        self.lineEdit_31.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 30, 63, 14))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(180, 30))
        self.groupBox_7.setMaximumSize(QSize(180, 100))
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 63, 14))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 60, 63, 14))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.lineEdit_41 = QLineEdit(self.groupBox_7)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(False)
        self.lineEdit_41.setGeometry(QRect(80, 30, 81, 20))
        self.lineEdit_41.setAlignment(Qt.AlignCenter)
        self.lineEdit_42 = QLineEdit(self.groupBox_7)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(False)
        self.lineEdit_42.setGeometry(QRect(80, 60, 81, 20))
        self.lineEdit_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.groupBox_7)


        self.verticalLayout_3.addWidget(self.groupBox_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1170, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionFile)
        self.menu.addAction(self.actionCamera)
        self.menu_2.addAction(self.actionManual)
        self.menu_2.addAction(self.actionGithub)
        self.menu_2.addAction(self.actionContact_us)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u5b66\u4e60\u5206\u6790\u7cfb\u7edf", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.actionManual.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u624b\u518c", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u7801\u4ed3\u5e93", None))
        self.actionContact_us.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u6211\u4eec", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790\u6a21\u5f0f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u59ff\u52bf", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u7eea", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u75b2\u52b3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u8bc6", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u59ff\u52bf\u7ebf", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u6846", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u70b9", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u8138\u671d\u5411", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"家长:", None))
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"学生ID:", None))
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"帧率:", None))
        self.label_36.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u7efc\u5408(\u4e13\u6ce8\u5ea6)\u5206\u6790", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u59ff\u52bf\u5206\u6790", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5750\u59ff", None))
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u60c5\u7eea\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7ec6\u5206", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5927\u7c7b", None))
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u75b2\u52b3\u5206\u6790", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7728\u773c\u6b21\u6570", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u5634\u5e27", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u95ed\u773c\u5e27", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u54c8\u6b20\u6b21\u6570", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u95ed\u773c\u6b21\u6570", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None))
        self.lineEdit_32.setText("")
        self.lineEdit_33.setText("")
        self.lineEdit_34.setText("")
        self.lineEdit_35.setText("")
        self.lineEdit_36.setText("")
        self.lineEdit_37.setText("")
        self.lineEdit_31.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5e27\u8ba1\u65f6", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u4e13\u6ce8\u5ea6\u8bc4\u5206", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u7ea7", None))
        self.lineEdit_41.setText("")
        self.lineEdit_42.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi


    def manual(self):
        QDesktopServices.openUrl(QUrl(menu.get('help','manual')))
    def github(self):
        QDesktopServices.openUrl(QUrl(menu.get('help','github')))
    def contact_us(self):
        QMessageBox.about(self, "信息", "请联系{}".format(menu.get('help','contact_us')))





class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()#调用父类QMainWindow的初始化函数
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

class MainCode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.video=cv.VideoCapture(0)
        self.bg = cv.imread('lib/green.jpg')
        #self.video = cv.VideoCapture('D:/Windows Folders/下载/媒体1.mp4')
        self.painter = QPainter(self)
        self.buttonFlag = 0  # 没有按钮按下
        #print('reset')
        self.videodir=''
        self.cameraopen=1
        self.fileopen=0
        self.opendb=db.getint('write','is_insert')
        self.actionFile.triggered.connect(self.openfile)
        self.actionCamera.triggered.connect(self.camera_switch)
        self.eng = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}  # 用于Ini写数据库

        self.pushButton.clicked.connect(self.xflag)
        self.pushButton_2.clicked.connect(self.xflag_2)
        self.pushButton_3.clicked.connect(self.xflag_3)
        self.pushButton_4.clicked.connect(self.xflag_4)
        self.student_id=self.lineEdit_34.text()
        self.framecounter=0
        self.framecountermax=1000#连续检测1000帧
        self.timetest=time()
        self.fatiguedatatuple =(0,0,0,0,0,0,0,0,0,0,0)
        self.scoretuple=(0,0,0,0)
        self.gradetuple=(0,0,0,0)
        self.concentrationdatatuple=({'Angry': 0, 'Hate': 0, 'Fear': 0, 'Happy': 0, 'Sad': 0, 'Surprise': 0, 'Neutral': 0, },
                                     [],[],[],[],[])
    def xflag(self):
        self.framecounter = 0
        self.fatiguedatatuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0)
        print('按下按钮{}'.format(self.buttonFlag))
        if self.buttonFlag==0:
            self.buttonFlag=1
            self.pushButton.setText('分析..')
            self.timetest = time()
            print('开始计时')
        else:
            self.buttonFlag=0
            self.pushButton.setText('姿势')
            self.pushButton_2.setText('情绪')
            self.pushButton_3.setText('疲劳')
            self.pushButton_4.setText('综合')
    def xflag_2(self):
        self.framecounter = 0
        self.fatiguedatatuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0)
        print('按下按钮{}'.format(self.buttonFlag))
        if self.buttonFlag==0:
            self.buttonFlag=2
            self.pushButton_2.setText('分析..')
            self.timetest = time()
            print('开始计时')
        else:
            self.buttonFlag=0
            self.pushButton.setText('姿势')
            self.pushButton_2.setText('情绪')
            self.pushButton_3.setText('疲劳')
            self.pushButton_4.setText('综合')
    def xflag_3(self):
        self.framecounter = 0
        self.fatiguedatatuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0)
        print('按下按钮{}'.format(self.buttonFlag))
        if self.buttonFlag==0:
            self.buttonFlag=3
            self.pushButton_3.setText('分析..')
            self.timetest = time()
            print('开始计时')
        else:
            self.buttonFlag=0
            self.pushButton.setText('姿势')
            self.pushButton_2.setText('情绪')
            self.pushButton_3.setText('疲劳')
            self.pushButton_4.setText('综合')
    #专注度分析模块要用到scoretuple，gradetuple，concentrationdatatuple
    def xflag_4(self):
        self.framecounter = 0
        self.fatiguedatatuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0)
        self.scoretuple = (0, 0, 0, 0)
        self.gradetuple = (0, 0, 0, 0)
        self.concentrationdatatuple = (
        {'Angry': 0, 'Hate': 0, 'Fear': 0, 'Happy': 0, 'Sad': 0, 'Surprise': 0, 'Neutral': 0, },
        [], [], [], [], [])
        print('按下按钮{}'.format(self.buttonFlag))
        if self.buttonFlag==0:
            self.buttonFlag=4
            self.pushButton_4.setText('分析..')
            self.timetest = time()
            print('开始计时')
        else:
            self.buttonFlag=0
            self.pushButton.setText('姿势')
            self.pushButton_2.setText('情绪')
            self.pushButton_3.setText('疲劳')
            self.pushButton_4.setText('综合')

    def openfile(self):
        filetype=menu.get('start', 'filetype')
        fileinfo = QFileDialog.getOpenFileName(self,'选择文件','',filetype)
        print('fileinfo = {}'.format(fileinfo))
        #fileinfo = ('D:/Windows Folders/下载/WeChat_20230302153542.mp4', 'Video files(*.mp4 , *.avi)')
        self.videodir=fileinfo[0]
        print('self.videodir = {}'.format(self.videodir))
        self.video = cv.VideoCapture(self.videodir)
        self.fileopen=1
        self.cameraopen=0
    def camera_switch(self):
        # 0/1切换
        if self.cameraopen==0 and self.fileopen==1:#前一状态
            self.video = cv.VideoCapture(0)
            self.cameraopen = 1
            self.fileopen=0
        elif self.cameraopen == 0 and self.fileopen == 0:#前一状态
            self.cameraopen = 1
            self.fileopen = 0
        elif self.cameraopen == 1 and self.fileopen == 0:  # 前一状态
            self.cameraopen = 0
            self.fileopen = 0

    def paintEvent(self, a0: QPaintEvent):
        #print('self.cameraopen={},self.fileopen={}'.format(self.cameraopen,self.fileopen))

        if self.cameraopen or self.fileopen:
            ret, frame = self.video.read()

            if ret:
                t_start=time()
                print(self.framecounter)
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                self.framecounter+=1
                # 疲劳分析需要连续分析1000帧,计算1000帧以内的闭眼时长、眨眼频率、打哈欠频率
                if self.framecounter==self.framecountermax:
                    self.framecounter=0
                    self.fatiguedatatuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0)
                    print('运行1000帧时间为{}秒'.format(time()-self.timetest))
                    self.timetest=time()
                    #self.scoretuple = (0, 0, 0, 0)
                    #self.gradetuple = (0, 0, 0, 0)
                    self.concentrationdatatuple=({'Angry': 0, 'Hate': 0, 'Fear': 0, 'Happy': 0, 'Sad': 0, 'Surprise': 0, 'Neutral': 0, },
                                             [],[],[],[],[])
                # 按下情绪识别按钮
                if self.buttonFlag==2:
                    t=time()
                    self.checkBox_2.setEnabled(True)
                    is_show_box = self.checkBox_2.isChecked()
                    print('is_show_box={}'.format(is_show_box))
                    rects,roi_gray, photo = face_detect(frame,is_show_box)  # 输出人脸矩形坐标，压缩人脸灰度图
                    print('圈出人脸时间为{:.3f}'.format(time()-t))
                    t=time()


                    emoFlag, photo = emotion_detect(roi_gray,photo)  # 输入灰度图，输出情绪类别标签emoFlag，并输出情绪识别后用文字标签后的图片
                    print('识别情绪时间为{:.3f}'.format(time() - t))
                    t = time()
                    self.QImage=QImage(photo.data, photo.shape[1], photo.shape[0], photo.shape[1] * 3, QImage.Format_RGB888)


                    self.lineEdit_21.setEnabled(True)
                    # print('字典第一个元素为{}'.format(dic[1]))
                    self.lineEdit_21.setText('{}'.format(db.get("emotion", self.eng[emotion_db_dic[emoFlag]])))

                    if self.opendb:#根据ini配置，是否插入数据库
                        event_insert(self.student_id, 'emotion', emoFlag, 2)
                    print('写数据库时间为{:.3f}'.format(time() - t))
                    #t = time()
                    #log.info("The user zcl write to the database sucessfully")
                    #logging.info("the original_event=emotion,original_value={}".format(emoFlag))
                # 按下姿势识别按钮
                elif self.buttonFlag==1:
                    self.checkBox.setEnabled(True)
                    is_show=(False,False,self.checkBox.isChecked(),False)
                    is_z_gap, is_y_gap_sh, is_y_head_gap, is_per, isPosture, headPosture, photo = \
                        posture_detect(frame, frame,is_show)
                    self.QImage = QImage(photo.data, photo.shape[1], photo.shape[0], photo.shape[1] * 3, QImage.Format_RGB888)

                    self.lineEdit_11.setEnabled(True)
                    #print('字典第一个元素为{}'.format(dic[1]))
                    self.lineEdit_11.setText('{}'.format(db.get("posture", self.eng[headPosture])))

                    if self.opendb:#根据ini配置，是否插入数据库
                        state_insert(self.student_id,'posture', headPosture, 2)
    
                        event_insert(self.student_id, 'is_z_gap', is_z_gap, 2)
                        event_insert(self.student_id, 'is_y_gap_sh', is_y_gap_sh, 2)
                        event_insert(self.student_id, 'is_y_head_gap', is_y_head_gap, 2)
                        event_insert(self.student_id, 'is_per', is_per, 2)

                    # log.info("The user zcl write to the database successfully")
                    #logging.info("the original_event=posture,original_value={}".format(3))

                # 按下疲劳分析按钮
                elif self.buttonFlag==3:
                    self.checkBox_2.setEnabled(True)
                    self.checkBox_3.setEnabled(True)
                    is_show=(self.checkBox_2.isChecked(),self.checkBox_3.isChecked(),False)

                    rects, roi_gray, frame = face_detect(frame)  # 输出人脸矩形坐标，压缩人脸灰度图
                    self.fatiguedatatuple,photo=fatigue_detect(self.fatiguedatatuple,self.framecounter,rects,frame,is_show)
                    self.QImage = QImage(photo.data, photo.shape[1], photo.shape[0], photo.shape[1] * 3, QImage.Format_RGB888)

                    self.lineEdit_31.setEnabled(True)
                    self.lineEdit_32.setEnabled(True)
                    self.lineEdit_33.setEnabled(True)
                    self.lineEdit_34.setEnabled(True)
                    self.lineEdit_35.setEnabled(True)
                    self.lineEdit_36.setEnabled(True)
                    self.lineEdit_37.setEnabled(True)
                    self.lineEdit_31.setText(str(self.framecounter))
                    self.lineEdit_32.setText(str(self.fatiguedatatuple[3]))
                    self.lineEdit_33.setText(str(self.fatiguedatatuple[6]))
                    self.lineEdit_34.setText(str(self.fatiguedatatuple[7]))
                    self.lineEdit_35.setText(str(self.fatiguedatatuple[2]))
                    self.lineEdit_36.setText(str(self.fatiguedatatuple[4]))
                    self.lineEdit_37.setText('{:.0f}'.format(100*self.fatiguedatatuple[1]))
                    #如果累计参数+1,则数据库插入1;若累计参数不变，则数据库插入0

                    is_blink=self.fatiguedatatuple[11]
                    is_yawn=self.fatiguedatatuple[12]
                    is_close=self.fatiguedatatuple[13]

                    if self.opendb:#根据ini配置，是否插入数据库
                        event_insert(self.student_id, 'is_blink', is_blink, 2)
                        event_insert(self.student_id, 'is_yawn', is_yawn, 2)
                        event_insert(self.student_id, 'is_close', is_close, 2)


                    #累计统计framecountermax帧后，输出的疲劳值才是准确值,否则小于真实疲劳值
                    if self.framecounter==self.framecountermax-1:
                        print('疲劳程度为{}'.format(self.fatiguedatatuple[0]))
                        if self.opendb:#根据ini配置，是否插入数据库
                            state_insert(self.student_id, 'fatigue', self.fatiguedatatuple[0], 2)

                    # log.info("The user zcl write to the database successfully")
                    # logging.info("the original_event=fatigue,original_value={}".format(3))
                # 按下专注度分析按钮
                elif self.buttonFlag==4:
                    self.checkBox.setEnabled(True)
                    self.checkBox_2.setEnabled(True)
                    self.checkBox_3.setEnabled(True)
                    self.checkBox_4.setEnabled(True)
                    is_show=(self.checkBox.isChecked(),self.checkBox_2.isChecked(),
                             self.checkBox_3.isChecked(),self.checkBox_4.isChecked())
                    self.concentrationdatatuple,self.fatiguedatatuple, \
                    (emoFlag, emotion_sort), headPosture,\
                    self.scoretuple,self.gradetuple,eventtuple,photo=\
                        concentration_detect(self.concentrationdatatuple,self.fatiguedatatuple,
                                             self.scoretuple,self.gradetuple,
                                             self.framecounter,
                                             self.framecountermax,frame,is_show)
                    self.QImage = QImage(photo.data, photo.shape[1], photo.shape[0], photo.shape[1] * 3, QImage.Format_RGB888)


                    self.lineEdit_31.setEnabled(True)
                    self.lineEdit_32.setEnabled(True)
                    self.lineEdit_33.setEnabled(True)
                    self.lineEdit_34.setEnabled(True)
                    self.lineEdit_35.setEnabled(True)
                    self.lineEdit_36.setEnabled(True)
                    self.lineEdit_37.setEnabled(True)
                    self.lineEdit_31.setText(str(self.framecounter))
                    self.lineEdit_32.setText(str(self.fatiguedatatuple[3]))
                    self.lineEdit_33.setText(str(self.fatiguedatatuple[6]))
                    self.lineEdit_34.setText(str(self.fatiguedatatuple[7]))
                    self.lineEdit_35.setText(str(self.fatiguedatatuple[2]))
                    self.lineEdit_36.setText(str(self.fatiguedatatuple[4]))
                    self.lineEdit_37.setText('{:.0f}'.format(100 * self.fatiguedatatuple[1]))

                    self.lineEdit_11.setEnabled(True)
                    self.lineEdit_21.setEnabled(True)
                    #self.lineEdit_37.setEnabled(True)
                    self.lineEdit_41.setEnabled(True)
                    self.lineEdit_11.setText('{}'.format(db.get("posture", self.eng[headPosture])))
                    self.lineEdit_21.setText('{}'.format(db.get("emotion", self.eng[emotion_db_dic[emoFlag]])))
                    #self.lineEdit_37.setText('{:.0f}'.format(100 * self.scoretuple[2]))
                    self.lineEdit_41.setText('{:.0f}'.format(100 * self.scoretuple[3]))



                    (emoFlag, is_pitch, is_yaw, is_roll,
                     is_z_gap, is_y_gap_sh,is_y_head_gap, is_per,
                     is_blink,is_yawn,is_close)=eventtuple
                    if self.opendb:#根据ini配置，是否插入数据库
                        original_event_insert_all(self.student_id, emoFlag, is_pitch, is_yaw, is_roll, is_z_gap, is_y_gap_sh,
                                          is_y_head_gap, is_per, is_blink,is_yawn,is_close)
                    # 累计统计framecountermax帧后，输出的疲劳值才是准确值,否则小于真实疲劳值
                    if self.framecounter == self.framecountermax - 1:
                        (emotion_grade,fatigue_grade,posture_grade,focus_grade)=self.gradetuple
                        (posture_score, emotion_score,fatigue_score, focus_score) = self.scoretuple
                        print('情绪消极程度为{},评分为{}'.format(emotion_grade,emotion_score))
                        print('疲劳程度为{},评分为{}'.format(fatigue_grade,fatigue_score))
                        print('姿势错误度为{},评分为{}'.format(posture_grade,posture_score))
                        print('专注程度为{},评分为{}'.format(focus_grade,focus_score))

                        self.lineEdit_12.setEnabled(True)
                        self.lineEdit_22.setEnabled(True)
                        self.lineEdit_23.setEnabled(True)
                        self.lineEdit_42.setEnabled(True)
                        # print('gradetuple最后一项为')
                        # print(self.gradetuple[3])
                        self.lineEdit_12.setText('{:.0f}'.format(100 * self.scoretuple[0]))
                        self.lineEdit_22.setText('{}'.format(db.get("emotion", emotion_sort)))
                        self.lineEdit_23.setText('{:.0f}'.format(100 * self.scoretuple[1]))
                        self.lineEdit_42.setText('{}'.format(db.get("concentration", self.eng[self.gradetuple[3]])))
                        # 每个周期插入数据
                        if self.opendb:#根据ini配置，是否插入数据库
                            study_state_insert_all(self.student_id, emotion_grade, fatigue_grade, posture_grade, focus_grade)
                    # log.info("The user zcl write to the database successfully")
                    # logging.info("the original_event=concentration,original_value={}".format(3))
                else:
                    self.lineEdit_11.setEnabled(False)
                    self.lineEdit_12.setEnabled(False)
                    self.lineEdit_21.setEnabled(False)
                    self.lineEdit_22.setEnabled(False)
                    self.lineEdit_23.setEnabled(False)
                    self.lineEdit_31.setEnabled(False)
                    self.lineEdit_32.setEnabled(False)
                    self.lineEdit_33.setEnabled(False)
                    self.lineEdit_34.setEnabled(False)
                    self.lineEdit_35.setEnabled(False)
                    self.lineEdit_36.setEnabled(False)
                    self.lineEdit_37.setEnabled(False)
                    self.lineEdit_41.setEnabled(False)
                    self.lineEdit_42.setEnabled(False)
                    self.lineEdit_11.setText('')
                    self.lineEdit_12.setText('')
                    self.lineEdit_21.setText('')
                    self.lineEdit_22.setText('')
                    self.lineEdit_23.setText('')
                    self.lineEdit_31.setText('')
                    self.lineEdit_32.setText('')
                    self.lineEdit_33.setText('')
                    self.lineEdit_34.setText('')
                    self.lineEdit_35.setText('')
                    self.lineEdit_36.setText('')
                    self.lineEdit_37.setText('')
                    self.lineEdit_41.setText('')
                    self.lineEdit_42.setText('')
                    self.checkBox.setEnabled(False)
                    self.checkBox_2.setEnabled(False)
                    self.checkBox_3.setEnabled(False)
                    self.checkBox_4.setEnabled(False)


                    self.QImage = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
                t_end=time()
                fps=30.0
                if t_end-t_start:
                    fps=1.0/(t_end-t_start)#若检测时间过短，则可能没检测到人脸，忽略不更新
                    #print('fps={:.0f}'.format(fps))
                    if fps>30.0:
                        fps=30.0#cv最高帧率为30帧
                t=time()
                self.label_36.setText('{:.0f}'.format(fps))
                self.img_label.setPixmap(QPixmap.fromImage(self.QImage))
                self.update()
                #print('重置帧时间为{:.3f}'.format(time() - t))
            '''
            else:
                reply=QMessageBox.about(self, "警告", "无视频信号！可能是以下原因:\n1.文件播放完毕\n2.文件选择出错\n3.无可用摄像头")
                print('reply={}'.format(reply))#reply=None
                if reply==None:
                    self.video=cv.VideoCapture(0)
            '''
        else:
            #cv.resize(self.bg,(1280,720))
            frame=self.bg
            self.QImage = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
            self.img_label.setPixmap(QPixmap.fromImage(self.QImage))
            self.update()








app = QApplication([])
mainw = Ui_Login()
mainw.ui.show()
#mainw=MainCode()
#mainw.show()
app.exec_()