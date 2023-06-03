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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 492)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionContact_Us = QAction(MainWindow)
        self.actionContact_Us.setObjectName(u"actionContact_Us")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_2.addWidget(self.graphicsView)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignVCenter)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignVCenter)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_3.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 634, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionFile)
        self.menu.addAction(self.actionCamera)
        self.menu_2.addAction(self.actionContact_Us)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u5b66\u4e60\u5206\u6790\u7cfb\u7edf", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.actionContact_Us.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u75b2\u52b3\u5206\u6790", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u59ff\u52bf\u5206\u6790", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u6ce8\u5ea6\u5206\u6790", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u7eea\u5206\u6790", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u8bc6\u522b", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u70b9", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u6807\u53f7", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u8bc6\u522b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\u72b6\u6001\u5206\u6790", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5e27\u6570", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6982\u7387", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u53c2\u6570", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

