# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVoxMLWindowLPeCOj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainVoxMLWindow(object):
    def setupUi(self, MainVoxMLWindow):
        if not MainVoxMLWindow.objectName():
            MainVoxMLWindow.setObjectName(u"MainVoxMLWindow")
        MainVoxMLWindow.resize(1300, 820)
        self.mainWidget = QWidget(MainVoxMLWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.backgroundFrame = QFrame(self.mainWidget)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setGeometry(QRect(20, 0, 1280, 800))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundFrame.sizePolicy().hasHeightForWidth())
        self.backgroundFrame.setSizePolicy(sizePolicy)
        self.backgroundFrame.setStyleSheet(u"QFrame#backgroundFrame {\n"
"	border-radius: 20px;\n"
"	border: None;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	color: #f0f0f0;\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.exitButton = QPushButton(self.backgroundFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(1230, 10, 40, 25))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #f62451;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f0f0f0;\n"
"}")
        self.label = QLabel(self.backgroundFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 550, 60))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"	border-radius: 0px;\n"
"	background-color: None;\n"
"	color: #f0f0f0;\n"
"	border: None;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.openVoxMLDataButton = QPushButton(self.backgroundFrame)
        self.openVoxMLDataButton.setObjectName(u"openVoxMLDataButton")
        self.openVoxMLDataButton.setGeometry(QRect(225, 120, 160, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.openVoxMLDataButton.setFont(font2)
        self.openVoxMLDataButton.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}")
        self.frame = QFrame(self.backgroundFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 170, 800, 600))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: 2px solid #f0f0f0;\n"
"	background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.createVoxMLButton = QPushButton(self.backgroundFrame)
        self.createVoxMLButton.setObjectName(u"createVoxMLButton")
        self.createVoxMLButton.setGeometry(QRect(670, 120, 160, 30))
        self.createVoxMLButton.setFont(font2)
        self.createVoxMLButton.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}")
        self.templateChooser = QComboBox(self.backgroundFrame)
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.setObjectName(u"templateChooser")
        self.templateChooser.setGeometry(QRect(500, 120, 160, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.templateChooser.setFont(font3)
        self.templateChooser.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #f0f0f0;\n"
"    border-radius: 10px;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: #f0f0f0;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    borde"
                        "r-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.backgroundFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 120, 100, 28))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: None;\n"
"	color: #2b78d3;\n"
"	border: None;\n"
"}")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.saveVoxMLData = QPushButton(self.backgroundFrame)
        self.saveVoxMLData.setObjectName(u"saveVoxMLData")
        self.saveVoxMLData.setGeometry(QRect(30, 120, 160, 30))
        self.saveVoxMLData.setFont(font2)
        self.saveVoxMLData.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #1fd78d;\n"
"}")
        MainVoxMLWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainVoxMLWindow)

        self.templateChooser.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainVoxMLWindow)
    # setupUi

    def retranslateUi(self, MainVoxMLWindow):
        MainVoxMLWindow.setWindowTitle(QCoreApplication.translate("MainVoxMLWindow", u"MainWindow", None))
        self.exitButton.setText("")
        self.label.setText(QCoreApplication.translate("MainVoxMLWindow", u"VoxML Annotator", None))
        self.openVoxMLDataButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Open VoxMLData", None))
        self.createVoxMLButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Create VoxMLData", None))
        self.templateChooser.setItemText(0, QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setItemText(1, QCoreApplication.translate("MainVoxMLWindow", u"Attribute", None))
        self.templateChooser.setItemText(2, QCoreApplication.translate("MainVoxMLWindow", u"Function", None))
        self.templateChooser.setItemText(3, QCoreApplication.translate("MainVoxMLWindow", u"Object", None))
        self.templateChooser.setItemText(4, QCoreApplication.translate("MainVoxMLWindow", u"Program", None))
        self.templateChooser.setItemText(5, QCoreApplication.translate("MainVoxMLWindow", u"Relation", None))

        self.templateChooser.setCurrentText(QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainVoxMLWindow", u"Template:", None))
        self.saveVoxMLData.setText(QCoreApplication.translate("MainVoxMLWindow", u"Save VoxMLData", None))
    # retranslateUi

