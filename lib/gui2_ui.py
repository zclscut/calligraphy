# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.label_31.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.label_31)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_7.addWidget(self.label_32)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_7.addWidget(self.label_33)

        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_7.addWidget(self.label_34)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_3)

        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_7.addWidget(self.label_35)

        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_7.addWidget(self.label_36)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

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
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u5bb6\u957f:", None))
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751fID:", None))
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u5e27\u7387:", None))
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

