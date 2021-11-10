# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVoxMLWindowgVfEIA.ui'
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
        self.backgroundFrame.setGeometry(QRect(10, 10, 1280, 800))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundFrame.sizePolicy().hasHeightForWidth())
        self.backgroundFrame.setSizePolicy(sizePolicy)
        self.backgroundFrame.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border-radius: 20px;\n"
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
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.openVoxMLDataButton = QPushButton(self.backgroundFrame)
        self.openVoxMLDataButton.setObjectName(u"openVoxMLDataButton")
        self.openVoxMLDataButton.setGeometry(QRect(20, 100, 160, 30))
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
"	background-color: None;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}")
        MainVoxMLWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainVoxMLWindow)

        QMetaObject.connectSlotsByName(MainVoxMLWindow)
    # setupUi

    def retranslateUi(self, MainVoxMLWindow):
        MainVoxMLWindow.setWindowTitle(QCoreApplication.translate("MainVoxMLWindow", u"MainWindow", None))
        self.exitButton.setText("")
        self.label.setText(QCoreApplication.translate("MainVoxMLWindow", u"VoxML Annotator", None))
        self.openVoxMLDataButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Open VoxMLData", None))
    # retranslateUi

