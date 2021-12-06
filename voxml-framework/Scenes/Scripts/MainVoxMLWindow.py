# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVoxMLWindowVdQSeh.ui'
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
        self.titleLabel = QLabel(self.backgroundFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 550, 60))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(50)
        self.titleLabel.setFont(font1)
        self.titleLabel.setStyleSheet(u"QLabel {\n"
"	border-radius: 0px;\n"
"	background-color: None;\n"
"	color: #f0f0f0;\n"
"	border: None;\n"
"}")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.openVoxMLDataButton = QPushButton(self.backgroundFrame)
        self.openVoxMLDataButton.setObjectName(u"openVoxMLDataButton")
        self.openVoxMLDataButton.setGeometry(QRect(100, 120, 100, 30))
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
        self.editingFrame = QFrame(self.backgroundFrame)
        self.editingFrame.setObjectName(u"editingFrame")
        self.editingFrame.setGeometry(QRect(30, 170, 800, 600))
        self.editingFrame.setStyleSheet(u"QFrame#editingFrame {\n"
"	border: 2px solid #f0f0f0;\n"
"	background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border-top-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 2px solid #f0f0f0;\n"
"	background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"}")
        self.editingFrame.setFrameShape(QFrame.StyledPanel)
        self.editingFrame.setFrameShadow(QFrame.Raised)
        self.entityBtn = QPushButton(self.editingFrame)
        self.entityBtn.setObjectName(u"entityBtn")
        self.entityBtn.setGeometry(QRect(20, 20, 100, 30))
        self.entityBtn.setFont(font2)
        self.entityBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.lexBtn = QPushButton(self.editingFrame)
        self.lexBtn.setObjectName(u"lexBtn")
        self.lexBtn.setGeometry(QRect(130, 20, 100, 30))
        self.lexBtn.setFont(font2)
        self.lexBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.typeBtn = QPushButton(self.editingFrame)
        self.typeBtn.setObjectName(u"typeBtn")
        self.typeBtn.setGeometry(QRect(240, 20, 100, 30))
        self.typeBtn.setFont(font2)
        self.typeBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.habitatBtn = QPushButton(self.editingFrame)
        self.habitatBtn.setObjectName(u"habitatBtn")
        self.habitatBtn.setGeometry(QRect(350, 20, 100, 30))
        self.habitatBtn.setFont(font2)
        self.habitatBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.attributesBtn = QPushButton(self.editingFrame)
        self.attributesBtn.setObjectName(u"attributesBtn")
        self.attributesBtn.setGeometry(QRect(680, 20, 100, 30))
        self.attributesBtn.setFont(font2)
        self.attributesBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.embodimentBtn = QPushButton(self.editingFrame)
        self.embodimentBtn.setObjectName(u"embodimentBtn")
        self.embodimentBtn.setGeometry(QRect(570, 20, 100, 30))
        self.embodimentBtn.setFont(font2)
        self.embodimentBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.affordStrBtn = QPushButton(self.editingFrame)
        self.affordStrBtn.setObjectName(u"affordStrBtn")
        self.affordStrBtn.setGeometry(QRect(460, 20, 100, 30))
        self.affordStrBtn.setFont(font2)
        self.affordStrBtn.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #f0f0f0;\n"
"}")
        self.entityFrame = QFrame(self.editingFrame)
        self.entityFrame.setObjectName(u"entityFrame")
        self.entityFrame.setEnabled(True)
        self.entityFrame.setGeometry(QRect(0, 70, 800, 530))
        self.entityFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}")
        self.entityFrame.setFrameShape(QFrame.StyledPanel)
        self.entityFrame.setFrameShadow(QFrame.Raised)
        self.entityTypeLabel = QLabel(self.entityFrame)
        self.entityTypeLabel.setObjectName(u"entityTypeLabel")
        self.entityTypeLabel.setGeometry(QRect(250, 250, 120, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.entityTypeLabel.setFont(font3)
        self.entityType = QLineEdit(self.entityFrame)
        self.entityType.setObjectName(u"entityType")
        self.entityType.setGeometry(QRect(370, 250, 150, 30))
        self.entityType.setFont(font3)
        self.entityType.setAlignment(Qt.AlignCenter)
        self.lexFrame = QFrame(self.editingFrame)
        self.lexFrame.setObjectName(u"lexFrame")
        self.lexFrame.setEnabled(True)
        self.lexFrame.setGeometry(QRect(0, 70, 800, 530))
        self.lexFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}")
        self.lexFrame.setFrameShape(QFrame.StyledPanel)
        self.lexFrame.setFrameShadow(QFrame.Raised)
        self.lexTypeLabel = QLabel(self.lexFrame)
        self.lexTypeLabel.setObjectName(u"lexTypeLabel")
        self.lexTypeLabel.setGeometry(QRect(250, 275, 120, 30))
        self.lexTypeLabel.setFont(font3)
        self.lexType = QLineEdit(self.lexFrame)
        self.lexType.setObjectName(u"lexType")
        self.lexType.setGeometry(QRect(370, 275, 150, 30))
        self.lexType.setFont(font3)
        self.lexType.setAlignment(Qt.AlignCenter)
        self.lexPredLabel = QLabel(self.lexFrame)
        self.lexPredLabel.setObjectName(u"lexPredLabel")
        self.lexPredLabel.setGeometry(QRect(250, 225, 120, 30))
        self.lexPredLabel.setFont(font3)
        self.lexPred = QLineEdit(self.lexFrame)
        self.lexPred.setObjectName(u"lexPred")
        self.lexPred.setGeometry(QRect(370, 225, 150, 30))
        self.lexPred.setFont(font3)
        self.lexPred.setAlignment(Qt.AlignCenter)
        self.embodimentFrame = QFrame(self.editingFrame)
        self.embodimentFrame.setObjectName(u"embodimentFrame")
        self.embodimentFrame.setEnabled(True)
        self.embodimentFrame.setGeometry(QRect(0, 70, 800, 530))
        self.embodimentFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #f62451;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #1fd78d;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}")
        self.embodimentFrame.setFrameShape(QFrame.StyledPanel)
        self.embodimentFrame.setFrameShadow(QFrame.Raised)
        self.movableLabel = QLabel(self.embodimentFrame)
        self.movableLabel.setObjectName(u"movableLabel")
        self.movableLabel.setGeometry(QRect(250, 275, 120, 30))
        self.movableLabel.setFont(font3)
        self.scaleLabel = QLabel(self.embodimentFrame)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setGeometry(QRect(250, 225, 120, 30))
        self.scaleLabel.setFont(font3)
        self.embodimentMovable = QCheckBox(self.embodimentFrame)
        self.embodimentMovable.setObjectName(u"embodimentMovable")
        self.embodimentMovable.setGeometry(QRect(430, 275, 30, 30))
        self.embodimentScale = QLineEdit(self.embodimentFrame)
        self.embodimentScale.setObjectName(u"embodimentScale")
        self.embodimentScale.setGeometry(QRect(370, 225, 150, 30))
        self.embodimentScale.setFont(font3)
        self.attributesFrame = QFrame(self.editingFrame)
        self.attributesFrame.setObjectName(u"attributesFrame")
        self.attributesFrame.setEnabled(True)
        self.attributesFrame.setGeometry(QRect(0, 70, 800, 530))
        self.attributesFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #f62451;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #1fd78d;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}")
        self.attributesFrame.setFrameShape(QFrame.StyledPanel)
        self.attributesFrame.setFrameShadow(QFrame.Raised)
        self.attributesLabel = QLabel(self.attributesFrame)
        self.attributesLabel.setObjectName(u"attributesLabel")
        self.attributesLabel.setGeometry(QRect(200, 100, 120, 30))
        self.attributesLabel.setFont(font3)
        self.attrsDel0 = QPushButton(self.attributesFrame)
        self.attrsDel0.setObjectName(u"attrsDel0")
        self.attrsDel0.setGeometry(QRect(470, 150, 100, 30))
        self.attrsDel0.setFont(font2)
        self.attrsDel0.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attributesAttrsAdd = QPushButton(self.attributesFrame)
        self.attributesAttrsAdd.setObjectName(u"attributesAttrsAdd")
        self.attributesAttrsAdd.setGeometry(QRect(470, 100, 100, 30))
        self.attributesAttrsAdd.setFont(font2)
        self.attributesAttrsAdd.setStyleSheet(u"QPushButton {\n"
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
        self.attributesAttrsNewItem = QLineEdit(self.attributesFrame)
        self.attributesAttrsNewItem.setObjectName(u"attributesAttrsNewItem")
        self.attributesAttrsNewItem.setGeometry(QRect(300, 100, 160, 30))
        self.attributesAttrsNewItem.setFont(font3)
        self.attributesAttrsNewItem.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.attrsVal0 = QLineEdit(self.attributesFrame)
        self.attrsVal0.setObjectName(u"attrsVal0")
        self.attrsVal0.setGeometry(QRect(300, 150, 160, 30))
        self.attrsVal0.setFont(font3)
        self.attrsVal0.setStyleSheet(u"")
        self.attrsDel1 = QPushButton(self.attributesFrame)
        self.attrsDel1.setObjectName(u"attrsDel1")
        self.attrsDel1.setGeometry(QRect(470, 190, 100, 30))
        self.attrsDel1.setFont(font2)
        self.attrsDel1.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsVal1 = QLineEdit(self.attributesFrame)
        self.attrsVal1.setObjectName(u"attrsVal1")
        self.attrsVal1.setGeometry(QRect(300, 190, 160, 30))
        self.attrsVal1.setFont(font3)
        self.attrsVal1.setStyleSheet(u"")
        self.attrsDel2 = QPushButton(self.attributesFrame)
        self.attrsDel2.setObjectName(u"attrsDel2")
        self.attrsDel2.setGeometry(QRect(470, 230, 100, 30))
        self.attrsDel2.setFont(font2)
        self.attrsDel2.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsVal2 = QLineEdit(self.attributesFrame)
        self.attrsVal2.setObjectName(u"attrsVal2")
        self.attrsVal2.setGeometry(QRect(300, 230, 160, 30))
        self.attrsVal2.setFont(font3)
        self.attrsVal2.setStyleSheet(u"")
        self.attrsDel3 = QPushButton(self.attributesFrame)
        self.attrsDel3.setObjectName(u"attrsDel3")
        self.attrsDel3.setGeometry(QRect(470, 270, 100, 30))
        self.attrsDel3.setFont(font2)
        self.attrsDel3.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsVal3 = QLineEdit(self.attributesFrame)
        self.attrsVal3.setObjectName(u"attrsVal3")
        self.attrsVal3.setGeometry(QRect(300, 270, 160, 30))
        self.attrsVal3.setFont(font3)
        self.attrsVal3.setStyleSheet(u"")
        self.attrsDel4 = QPushButton(self.attributesFrame)
        self.attrsDel4.setObjectName(u"attrsDel4")
        self.attrsDel4.setGeometry(QRect(470, 310, 100, 30))
        self.attrsDel4.setFont(font2)
        self.attrsDel4.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsVal4 = QLineEdit(self.attributesFrame)
        self.attrsVal4.setObjectName(u"attrsVal4")
        self.attrsVal4.setGeometry(QRect(300, 310, 160, 30))
        self.attrsVal4.setFont(font3)
        self.attrsVal4.setStyleSheet(u"")
        self.attrsDel6 = QPushButton(self.attributesFrame)
        self.attrsDel6.setObjectName(u"attrsDel6")
        self.attrsDel6.setGeometry(QRect(470, 390, 100, 30))
        self.attrsDel6.setFont(font2)
        self.attrsDel6.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsDel5 = QPushButton(self.attributesFrame)
        self.attrsDel5.setObjectName(u"attrsDel5")
        self.attrsDel5.setGeometry(QRect(470, 350, 100, 30))
        self.attrsDel5.setFont(font2)
        self.attrsDel5.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.attrsVal6 = QLineEdit(self.attributesFrame)
        self.attrsVal6.setObjectName(u"attrsVal6")
        self.attrsVal6.setGeometry(QRect(300, 390, 160, 30))
        self.attrsVal6.setFont(font3)
        self.attrsVal6.setStyleSheet(u"")
        self.attrsVal5 = QLineEdit(self.attributesFrame)
        self.attrsVal5.setObjectName(u"attrsVal5")
        self.attrsVal5.setGeometry(QRect(300, 350, 160, 30))
        self.attrsVal5.setFont(font3)
        self.attrsVal5.setStyleSheet(u"")
        self.affordStrFrame = QFrame(self.editingFrame)
        self.affordStrFrame.setObjectName(u"affordStrFrame")
        self.affordStrFrame.setEnabled(True)
        self.affordStrFrame.setGeometry(QRect(0, 70, 800, 530))
        self.affordStrFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #f62451;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #1fd78d;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}")
        self.affordStrFrame.setFrameShape(QFrame.StyledPanel)
        self.affordStrFrame.setFrameShadow(QFrame.Raised)
        self.affordancesLabel = QLabel(self.affordStrFrame)
        self.affordancesLabel.setObjectName(u"affordancesLabel")
        self.affordancesLabel.setGeometry(QRect(200, 100, 120, 30))
        self.affordancesLabel.setFont(font3)
        self.afforDel0 = QPushButton(self.affordStrFrame)
        self.afforDel0.setObjectName(u"afforDel0")
        self.afforDel0.setGeometry(QRect(470, 150, 100, 30))
        self.afforDel0.setFont(font2)
        self.afforDel0.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.affordStrAffordancesAdd = QPushButton(self.affordStrFrame)
        self.affordStrAffordancesAdd.setObjectName(u"affordStrAffordancesAdd")
        self.affordStrAffordancesAdd.setGeometry(QRect(470, 100, 100, 30))
        self.affordStrAffordancesAdd.setFont(font2)
        self.affordStrAffordancesAdd.setStyleSheet(u"QPushButton {\n"
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
        self.affordStrAffordancesNewItem = QLineEdit(self.affordStrFrame)
        self.affordStrAffordancesNewItem.setObjectName(u"affordStrAffordancesNewItem")
        self.affordStrAffordancesNewItem.setGeometry(QRect(300, 100, 160, 30))
        self.affordStrAffordancesNewItem.setFont(font3)
        self.affordStrAffordancesNewItem.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.afforVal0 = QLineEdit(self.affordStrFrame)
        self.afforVal0.setObjectName(u"afforVal0")
        self.afforVal0.setGeometry(QRect(300, 150, 160, 30))
        self.afforVal0.setFont(font3)
        self.afforVal0.setStyleSheet(u"")
        self.afforVal1 = QLineEdit(self.affordStrFrame)
        self.afforVal1.setObjectName(u"afforVal1")
        self.afforVal1.setGeometry(QRect(300, 190, 160, 30))
        self.afforVal1.setFont(font3)
        self.afforVal1.setStyleSheet(u"")
        self.afforDel1 = QPushButton(self.affordStrFrame)
        self.afforDel1.setObjectName(u"afforDel1")
        self.afforDel1.setGeometry(QRect(470, 190, 100, 30))
        self.afforDel1.setFont(font2)
        self.afforDel1.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.afforVal2 = QLineEdit(self.affordStrFrame)
        self.afforVal2.setObjectName(u"afforVal2")
        self.afforVal2.setGeometry(QRect(300, 230, 160, 30))
        self.afforVal2.setFont(font3)
        self.afforVal2.setStyleSheet(u"")
        self.afforDel3 = QPushButton(self.affordStrFrame)
        self.afforDel3.setObjectName(u"afforDel3")
        self.afforDel3.setGeometry(QRect(470, 270, 100, 30))
        self.afforDel3.setFont(font2)
        self.afforDel3.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.afforDel2 = QPushButton(self.affordStrFrame)
        self.afforDel2.setObjectName(u"afforDel2")
        self.afforDel2.setGeometry(QRect(470, 230, 100, 30))
        self.afforDel2.setFont(font2)
        self.afforDel2.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.afforVal3 = QLineEdit(self.affordStrFrame)
        self.afforVal3.setObjectName(u"afforVal3")
        self.afforVal3.setGeometry(QRect(300, 270, 160, 30))
        self.afforVal3.setFont(font3)
        self.afforVal3.setStyleSheet(u"")
        self.afforVal4 = QLineEdit(self.affordStrFrame)
        self.afforVal4.setObjectName(u"afforVal4")
        self.afforVal4.setGeometry(QRect(300, 310, 160, 30))
        self.afforVal4.setFont(font3)
        self.afforVal4.setStyleSheet(u"")
        self.afforDel5 = QPushButton(self.affordStrFrame)
        self.afforDel5.setObjectName(u"afforDel5")
        self.afforDel5.setGeometry(QRect(470, 350, 100, 30))
        self.afforDel5.setFont(font2)
        self.afforDel5.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.afforDel4 = QPushButton(self.affordStrFrame)
        self.afforDel4.setObjectName(u"afforDel4")
        self.afforDel4.setGeometry(QRect(470, 310, 100, 30))
        self.afforDel4.setFont(font2)
        self.afforDel4.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.afforVal5 = QLineEdit(self.affordStrFrame)
        self.afforVal5.setObjectName(u"afforVal5")
        self.afforVal5.setGeometry(QRect(300, 350, 160, 30))
        self.afforVal5.setFont(font3)
        self.afforVal5.setStyleSheet(u"")
        self.afforVal6 = QLineEdit(self.affordStrFrame)
        self.afforVal6.setObjectName(u"afforVal6")
        self.afforVal6.setGeometry(QRect(300, 390, 160, 30))
        self.afforVal6.setFont(font3)
        self.afforVal6.setStyleSheet(u"")
        self.afforDel6 = QPushButton(self.affordStrFrame)
        self.afforDel6.setObjectName(u"afforDel6")
        self.afforDel6.setGeometry(QRect(470, 390, 100, 30))
        self.afforDel6.setFont(font2)
        self.afforDel6.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.habitatFrame = QFrame(self.editingFrame)
        self.habitatFrame.setObjectName(u"habitatFrame")
        self.habitatFrame.setEnabled(True)
        self.habitatFrame.setGeometry(QRect(0, 70, 800, 530))
        self.habitatFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #f62451;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #1fd78d;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}")
        self.habitatFrame.setFrameShape(QFrame.StyledPanel)
        self.habitatFrame.setFrameShadow(QFrame.Raised)
        self.intrinsicLabel = QLabel(self.habitatFrame)
        self.intrinsicLabel.setObjectName(u"intrinsicLabel")
        self.intrinsicLabel.setGeometry(QRect(200, 175, 120, 30))
        self.intrinsicLabel.setFont(font3)
        self.habitatIntrinsic = QComboBox(self.habitatFrame)
        self.habitatIntrinsic.setObjectName(u"habitatIntrinsic")
        self.habitatIntrinsic.setGeometry(QRect(300, 175, 190, 30))
        self.habitatIntrinsic.setFont(font3)
        self.habitatIntrinsic.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.habitatIntrinsicDelete = QPushButton(self.habitatFrame)
        self.habitatIntrinsicDelete.setObjectName(u"habitatIntrinsicDelete")
        self.habitatIntrinsicDelete.setGeometry(QRect(500, 175, 100, 30))
        self.habitatIntrinsicDelete.setFont(font2)
        self.habitatIntrinsicDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.habitatIntrinsicAdder = QPushButton(self.habitatFrame)
        self.habitatIntrinsicAdder.setObjectName(u"habitatIntrinsicAdder")
        self.habitatIntrinsicAdder.setGeometry(QRect(500, 215, 100, 30))
        self.habitatIntrinsicAdder.setFont(font2)
        self.habitatIntrinsicAdder.setStyleSheet(u"QPushButton {\n"
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
        self.habitatIntrName = QLineEdit(self.habitatFrame)
        self.habitatIntrName.setObjectName(u"habitatIntrName")
        self.habitatIntrName.setGeometry(QRect(300, 215, 90, 30))
        self.habitatIntrName.setFont(font3)
        self.habitatIntrName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatIntrValue = QLineEdit(self.habitatFrame)
        self.habitatIntrValue.setObjectName(u"habitatIntrValue")
        self.habitatIntrValue.setGeometry(QRect(400, 215, 90, 30))
        self.habitatIntrValue.setFont(font3)
        self.habitatIntrValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.extrinsicLabel = QLabel(self.habitatFrame)
        self.extrinsicLabel.setObjectName(u"extrinsicLabel")
        self.extrinsicLabel.setGeometry(QRect(200, 280, 120, 30))
        self.extrinsicLabel.setFont(font3)
        self.habitatExtrName = QLineEdit(self.habitatFrame)
        self.habitatExtrName.setObjectName(u"habitatExtrName")
        self.habitatExtrName.setGeometry(QRect(300, 320, 90, 30))
        self.habitatExtrName.setFont(font3)
        self.habitatExtrName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrValue = QLineEdit(self.habitatFrame)
        self.habitatExtrValue.setObjectName(u"habitatExtrValue")
        self.habitatExtrValue.setGeometry(QRect(400, 320, 90, 30))
        self.habitatExtrValue.setFont(font3)
        self.habitatExtrValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrinsic = QComboBox(self.habitatFrame)
        self.habitatExtrinsic.setObjectName(u"habitatExtrinsic")
        self.habitatExtrinsic.setGeometry(QRect(300, 280, 190, 30))
        self.habitatExtrinsic.setFont(font3)
        self.habitatExtrinsic.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.habitatExtrinsicAdd = QPushButton(self.habitatFrame)
        self.habitatExtrinsicAdd.setObjectName(u"habitatExtrinsicAdd")
        self.habitatExtrinsicAdd.setGeometry(QRect(500, 320, 100, 30))
        self.habitatExtrinsicAdd.setFont(font2)
        self.habitatExtrinsicAdd.setStyleSheet(u"QPushButton {\n"
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
        self.habitatExtrinsicDelete = QPushButton(self.habitatFrame)
        self.habitatExtrinsicDelete.setObjectName(u"habitatExtrinsicDelete")
        self.habitatExtrinsicDelete.setGeometry(QRect(500, 280, 100, 30))
        self.habitatExtrinsicDelete.setFont(font2)
        self.habitatExtrinsicDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.typeFrame = QFrame(self.editingFrame)
        self.typeFrame.setObjectName(u"typeFrame")
        self.typeFrame.setEnabled(True)
        self.typeFrame.setGeometry(QRect(0, 70, 800, 530))
        self.typeFrame.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"	color: #2b78d3;\n"
"	background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #2b78d3;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #f62451;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"	border: 2px solid #1fd78d;\n"
"	border-radius: 3px;\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}")
        self.typeFrame.setFrameShape(QFrame.StyledPanel)
        self.typeFrame.setFrameShadow(QFrame.Raised)
        self.typeHeadLabel = QLabel(self.typeFrame)
        self.typeHeadLabel.setObjectName(u"typeHeadLabel")
        self.typeHeadLabel.setGeometry(QRect(30, 20, 120, 30))
        self.typeHeadLabel.setFont(font3)
        self.typeHead = QLineEdit(self.typeFrame)
        self.typeHead.setObjectName(u"typeHead")
        self.typeHead.setGeometry(QRect(160, 20, 160, 30))
        self.typeHead.setFont(font3)
        self.typeConcavity = QLineEdit(self.typeFrame)
        self.typeConcavity.setObjectName(u"typeConcavity")
        self.typeConcavity.setGeometry(QRect(160, 75, 160, 30))
        self.typeConcavity.setFont(font3)
        self.typeConcavityLabel = QLabel(self.typeFrame)
        self.typeConcavityLabel.setObjectName(u"typeConcavityLabel")
        self.typeConcavityLabel.setGeometry(QRect(30, 75, 120, 30))
        self.typeConcavityLabel.setFont(font3)
        self.typeClass = QLineEdit(self.typeFrame)
        self.typeClass.setObjectName(u"typeClass")
        self.typeClass.setGeometry(QRect(160, 130, 160, 30))
        self.typeClass.setFont(font3)
        self.typeClassLabel = QLabel(self.typeFrame)
        self.typeClassLabel.setObjectName(u"typeClassLabel")
        self.typeClassLabel.setGeometry(QRect(30, 130, 120, 30))
        self.typeClassLabel.setFont(font3)
        self.typeValue = QLineEdit(self.typeFrame)
        self.typeValue.setObjectName(u"typeValue")
        self.typeValue.setGeometry(QRect(160, 185, 160, 30))
        self.typeValue.setFont(font3)
        self.typeValueLabel = QLabel(self.typeFrame)
        self.typeValueLabel.setObjectName(u"typeValueLabel")
        self.typeValueLabel.setGeometry(QRect(30, 185, 120, 30))
        self.typeValueLabel.setFont(font3)
        self.typeScale = QLineEdit(self.typeFrame)
        self.typeScale.setObjectName(u"typeScale")
        self.typeScale.setGeometry(QRect(160, 295, 160, 30))
        self.typeScale.setFont(font3)
        self.typeReferentLabel = QLabel(self.typeFrame)
        self.typeReferentLabel.setObjectName(u"typeReferentLabel")
        self.typeReferentLabel.setGeometry(QRect(30, 405, 120, 30))
        self.typeReferentLabel.setFont(font3)
        self.typeConstr = QLineEdit(self.typeFrame)
        self.typeConstr.setObjectName(u"typeConstr")
        self.typeConstr.setGeometry(QRect(160, 240, 160, 30))
        self.typeConstr.setFont(font3)
        self.typeArityLabel = QLabel(self.typeFrame)
        self.typeArityLabel.setObjectName(u"typeArityLabel")
        self.typeArityLabel.setGeometry(QRect(30, 350, 120, 30))
        self.typeArityLabel.setFont(font3)
        self.typeReferent = QLineEdit(self.typeFrame)
        self.typeReferent.setObjectName(u"typeReferent")
        self.typeReferent.setGeometry(QRect(160, 405, 160, 30))
        self.typeReferent.setFont(font3)
        self.typeConstrLabel = QLabel(self.typeFrame)
        self.typeConstrLabel.setObjectName(u"typeConstrLabel")
        self.typeConstrLabel.setGeometry(QRect(30, 240, 120, 30))
        self.typeConstrLabel.setFont(font3)
        self.typeScaleLabel = QLabel(self.typeFrame)
        self.typeScaleLabel.setObjectName(u"typeScaleLabel")
        self.typeScaleLabel.setGeometry(QRect(30, 295, 120, 30))
        self.typeScaleLabel.setFont(font3)
        self.typeArity = QLineEdit(self.typeFrame)
        self.typeArity.setObjectName(u"typeArity")
        self.typeArity.setGeometry(QRect(160, 350, 160, 30))
        self.typeArity.setFont(font3)
        self.typeMappingLabel = QLabel(self.typeFrame)
        self.typeMappingLabel.setObjectName(u"typeMappingLabel")
        self.typeMappingLabel.setGeometry(QRect(30, 460, 120, 30))
        self.typeMappingLabel.setFont(font3)
        self.typeMapping = QLineEdit(self.typeFrame)
        self.typeMapping.setObjectName(u"typeMapping")
        self.typeMapping.setGeometry(QRect(160, 460, 160, 30))
        self.typeMapping.setFont(font3)
        self.typeComponentsLabel = QLabel(self.typeFrame)
        self.typeComponentsLabel.setObjectName(u"typeComponentsLabel")
        self.typeComponentsLabel.setGeometry(QRect(360, 20, 120, 30))
        self.typeComponentsLabel.setFont(font3)
        self.typeComponentsValue = QLineEdit(self.typeFrame)
        self.typeComponentsValue.setObjectName(u"typeComponentsValue")
        self.typeComponentsValue.setGeometry(QRect(480, 60, 190, 30))
        self.typeComponentsValue.setFont(font3)
        self.typeComponentsValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.typeComponents = QComboBox(self.typeFrame)
        self.typeComponents.setObjectName(u"typeComponents")
        self.typeComponents.setGeometry(QRect(480, 20, 190, 30))
        self.typeComponents.setFont(font3)
        self.typeComponents.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.typeComponentsAdd = QPushButton(self.typeFrame)
        self.typeComponentsAdd.setObjectName(u"typeComponentsAdd")
        self.typeComponentsAdd.setGeometry(QRect(680, 60, 100, 30))
        self.typeComponentsAdd.setFont(font2)
        self.typeComponentsAdd.setStyleSheet(u"QPushButton {\n"
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
        self.typeComponentsDelete = QPushButton(self.typeFrame)
        self.typeComponentsDelete.setObjectName(u"typeComponentsDelete")
        self.typeComponentsDelete.setGeometry(QRect(680, 20, 100, 30))
        self.typeComponentsDelete.setFont(font2)
        self.typeComponentsDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.typeArgsLabel = QLabel(self.typeFrame)
        self.typeArgsLabel.setObjectName(u"typeArgsLabel")
        self.typeArgsLabel.setGeometry(QRect(360, 110, 120, 30))
        self.typeArgsLabel.setFont(font3)
        self.typeArgsAdd = QPushButton(self.typeFrame)
        self.typeArgsAdd.setObjectName(u"typeArgsAdd")
        self.typeArgsAdd.setGeometry(QRect(680, 150, 100, 30))
        self.typeArgsAdd.setFont(font2)
        self.typeArgsAdd.setStyleSheet(u"QPushButton {\n"
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
        self.typeArgs = QComboBox(self.typeFrame)
        self.typeArgs.setObjectName(u"typeArgs")
        self.typeArgs.setGeometry(QRect(480, 110, 190, 30))
        self.typeArgs.setFont(font3)
        self.typeArgs.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.typeArgsDelete = QPushButton(self.typeFrame)
        self.typeArgsDelete.setObjectName(u"typeArgsDelete")
        self.typeArgsDelete.setGeometry(QRect(680, 110, 100, 30))
        self.typeArgsDelete.setFont(font2)
        self.typeArgsDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.typeArgsValue = QLineEdit(self.typeFrame)
        self.typeArgsValue.setObjectName(u"typeArgsValue")
        self.typeArgsValue.setGeometry(QRect(480, 150, 190, 30))
        self.typeArgsValue.setFont(font3)
        self.typeArgsValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.typeBodyLabel = QLabel(self.typeFrame)
        self.typeBodyLabel.setObjectName(u"typeBodyLabel")
        self.typeBodyLabel.setGeometry(QRect(360, 200, 120, 30))
        self.typeBodyLabel.setFont(font3)
        self.typeBodyAdd = QPushButton(self.typeFrame)
        self.typeBodyAdd.setObjectName(u"typeBodyAdd")
        self.typeBodyAdd.setGeometry(QRect(680, 240, 100, 30))
        self.typeBodyAdd.setFont(font2)
        self.typeBodyAdd.setStyleSheet(u"QPushButton {\n"
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
        self.typeBody = QComboBox(self.typeFrame)
        self.typeBody.setObjectName(u"typeBody")
        self.typeBody.setGeometry(QRect(480, 200, 190, 30))
        self.typeBody.setFont(font3)
        self.typeBody.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.typeBodyDelete = QPushButton(self.typeFrame)
        self.typeBodyDelete.setObjectName(u"typeBodyDelete")
        self.typeBodyDelete.setGeometry(QRect(680, 200, 100, 30))
        self.typeBodyDelete.setFont(font2)
        self.typeBodyDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.typeBodySubeventValue = QLineEdit(self.typeFrame)
        self.typeBodySubeventValue.setObjectName(u"typeBodySubeventValue")
        self.typeBodySubeventValue.setGeometry(QRect(480, 240, 190, 30))
        self.typeBodySubeventValue.setFont(font3)
        self.typeBodySubeventValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.typeCorrespsLabel = QLabel(self.typeFrame)
        self.typeCorrespsLabel.setObjectName(u"typeCorrespsLabel")
        self.typeCorrespsLabel.setGeometry(QRect(360, 290, 120, 30))
        self.typeCorrespsLabel.setFont(font3)
        self.typeCorrespsAdd = QPushButton(self.typeFrame)
        self.typeCorrespsAdd.setObjectName(u"typeCorrespsAdd")
        self.typeCorrespsAdd.setGeometry(QRect(680, 330, 100, 30))
        self.typeCorrespsAdd.setFont(font2)
        self.typeCorrespsAdd.setStyleSheet(u"QPushButton {\n"
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
        self.typeCorresps = QComboBox(self.typeFrame)
        self.typeCorresps.setObjectName(u"typeCorresps")
        self.typeCorresps.setGeometry(QRect(480, 290, 190, 30))
        self.typeCorresps.setFont(font3)
        self.typeCorresps.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
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
        self.typeCorrespsDelete = QPushButton(self.typeFrame)
        self.typeCorrespsDelete.setObjectName(u"typeCorrespsDelete")
        self.typeCorrespsDelete.setGeometry(QRect(680, 290, 100, 30))
        self.typeCorrespsDelete.setFont(font2)
        self.typeCorrespsDelete.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 2px solid #f62451;\n"
"}")
        self.typeCorrespsValue = QLineEdit(self.typeFrame)
        self.typeCorrespsValue.setObjectName(u"typeCorrespsValue")
        self.typeCorrespsValue.setGeometry(QRect(480, 330, 190, 30))
        self.typeCorrespsValue.setFont(font3)
        self.typeCorrespsValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.typeRotatSymLabel = QLabel(self.typeFrame)
        self.typeRotatSymLabel.setObjectName(u"typeRotatSymLabel")
        self.typeRotatSymLabel.setGeometry(QRect(360, 405, 120, 30))
        self.typeRotatSymLabel.setFont(font3)
        self.typeRotatSymX = QCheckBox(self.typeFrame)
        self.typeRotatSymX.setObjectName(u"typeRotatSymX")
        self.typeRotatSymX.setGeometry(QRect(480, 405, 70, 30))
        self.typeRotatSymX.setFont(font3)
        self.typeRotatSymY = QCheckBox(self.typeFrame)
        self.typeRotatSymY.setObjectName(u"typeRotatSymY")
        self.typeRotatSymY.setGeometry(QRect(560, 405, 70, 30))
        self.typeRotatSymY.setFont(font3)
        self.typeRotatSymZ = QCheckBox(self.typeFrame)
        self.typeRotatSymZ.setObjectName(u"typeRotatSymZ")
        self.typeRotatSymZ.setGeometry(QRect(640, 405, 70, 30))
        self.typeRotatSymZ.setFont(font3)
        self.typeReflSymYZ = QCheckBox(self.typeFrame)
        self.typeReflSymYZ.setObjectName(u"typeReflSymYZ")
        self.typeReflSymYZ.setGeometry(QRect(640, 460, 70, 30))
        self.typeReflSymYZ.setFont(font3)
        self.typeReflSymLabel = QLabel(self.typeFrame)
        self.typeReflSymLabel.setObjectName(u"typeReflSymLabel")
        self.typeReflSymLabel.setGeometry(QRect(360, 460, 120, 30))
        self.typeReflSymLabel.setFont(font3)
        self.typeReflSymXZ = QCheckBox(self.typeFrame)
        self.typeReflSymXZ.setObjectName(u"typeReflSymXZ")
        self.typeReflSymXZ.setGeometry(QRect(560, 460, 70, 30))
        self.typeReflSymXZ.setFont(font3)
        self.typeReflSymXY = QCheckBox(self.typeFrame)
        self.typeReflSymXY.setObjectName(u"typeReflSymXY")
        self.typeReflSymXY.setGeometry(QRect(480, 460, 70, 30))
        self.typeReflSymXY.setFont(font3)
        self.entityFrame.raise_()
        self.lexFrame.raise_()
        self.embodimentFrame.raise_()
        self.attributesFrame.raise_()
        self.affordStrFrame.raise_()
        self.habitatFrame.raise_()
        self.typeFrame.raise_()
        self.entityBtn.raise_()
        self.lexBtn.raise_()
        self.typeBtn.raise_()
        self.habitatBtn.raise_()
        self.attributesBtn.raise_()
        self.embodimentBtn.raise_()
        self.affordStrBtn.raise_()
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
        self.templateChooser.setGeometry(QRect(510, 120, 150, 30))
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
        self.templateLabel = QLabel(self.backgroundFrame)
        self.templateLabel.setObjectName(u"templateLabel")
        self.templateLabel.setGeometry(QRect(400, 120, 100, 28))
        self.templateLabel.setFont(font3)
        self.templateLabel.setStyleSheet(u"QLabel {\n"
"	background-color: None;\n"
"	color: #2b78d3;\n"
"	border: None;\n"
"}")
        self.templateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.saveVoxMLData = QPushButton(self.backgroundFrame)
        self.saveVoxMLData.setObjectName(u"saveVoxMLData")
        self.saveVoxMLData.setGeometry(QRect(670, 60, 160, 30))
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
        self.saveToObject = QPushButton(self.backgroundFrame)
        self.saveToObject.setObjectName(u"saveToObject")
        self.saveToObject.setGeometry(QRect(670, 20, 160, 30))
        self.saveToObject.setFont(font2)
        self.saveToObject.setStyleSheet(u"QPushButton {\n"
"	background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #f0f0f0;\n"
"	color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 1px solid #1fd78d;\n"
"}")
        self.popupText = QLabel(self.backgroundFrame)
        self.popupText.setObjectName(u"popupText")
        self.popupText.setGeometry(QRect(850, 20, 350, 80))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(18)
        self.popupText.setFont(font4)
        self.popupText.setStyleSheet(u"QLabel {\n"
"	border-radius: 20px;\n"
"	border: 3px solid #eb7b59;\n"
"	color: #eb7b59;\n"
"}")
        self.popupText.setAlignment(Qt.AlignCenter)
        self.templateLabel_2 = QLabel(self.backgroundFrame)
        self.templateLabel_2.setObjectName(u"templateLabel_2")
        self.templateLabel_2.setGeometry(QRect(20, 120, 60, 28))
        self.templateLabel_2.setFont(font3)
        self.templateLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: None;\n"
"	color: #2b78d3;\n"
"	border: None;\n"
"}")
        self.templateLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.open3DObjectButton = QPushButton(self.backgroundFrame)
        self.open3DObjectButton.setObjectName(u"open3DObjectButton")
        self.open3DObjectButton.setGeometry(QRect(210, 120, 100, 30))
        self.open3DObjectButton.setFont(font2)
        self.open3DObjectButton.setStyleSheet(u"QPushButton {\n"
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
        self.openImageButton = QPushButton(self.backgroundFrame)
        self.openImageButton.setObjectName(u"openImageButton")
        self.openImageButton.setGeometry(QRect(320, 120, 100, 30))
        self.openImageButton.setFont(font2)
        self.openImageButton.setStyleSheet(u"QPushButton {\n"
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
        MainVoxMLWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainVoxMLWindow)

        self.habitatIntrinsic.setCurrentIndex(-1)
        self.habitatExtrinsic.setCurrentIndex(-1)
        self.typeComponents.setCurrentIndex(-1)
        self.typeArgs.setCurrentIndex(-1)
        self.typeBody.setCurrentIndex(-1)
        self.typeCorresps.setCurrentIndex(-1)
        self.templateChooser.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainVoxMLWindow)
    # setupUi

    def retranslateUi(self, MainVoxMLWindow):
        MainVoxMLWindow.setWindowTitle(QCoreApplication.translate("MainVoxMLWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.exitButton.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Exit the program.", None))
#endif // QT_CONFIG(tooltip)
        self.exitButton.setText("")
#if QT_CONFIG(tooltip)
        self.titleLabel.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"That's just the title!", None))
#endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"VoxML Annotator", None))
#if QT_CONFIG(tooltip)
        self.openVoxMLDataButton.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Import VoxML Object from file", None))
#endif // QT_CONFIG(tooltip)
        self.openVoxMLDataButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"VoxML Data", None))
#if QT_CONFIG(tooltip)
        self.entityBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Entity attributes", None))
#endif // QT_CONFIG(tooltip)
        self.entityBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Entity", None))
#if QT_CONFIG(tooltip)
        self.lexBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Lex Attributes", None))
#endif // QT_CONFIG(tooltip)
        self.lexBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Lex", None))
#if QT_CONFIG(tooltip)
        self.typeBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Type attributes", None))
#endif // QT_CONFIG(tooltip)
        self.typeBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type", None))
#if QT_CONFIG(tooltip)
        self.habitatBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Habitat attributes", None))
#endif // QT_CONFIG(tooltip)
        self.habitatBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Habitat", None))
#if QT_CONFIG(tooltip)
        self.attributesBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Attributes attributes", None))
#endif // QT_CONFIG(tooltip)
        self.attributesBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Attributes", None))
#if QT_CONFIG(tooltip)
        self.embodimentBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit Embodiment attributes", None))
#endif // QT_CONFIG(tooltip)
        self.embodimentBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Embodiment", None))
#if QT_CONFIG(tooltip)
        self.affordStrBtn.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Edit AffordStr attributes", None))
#endif // QT_CONFIG(tooltip)
        self.affordStrBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"AffordStr", None))
        self.entityTypeLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type:", None))
#if QT_CONFIG(tooltip)
        self.entityType.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Entity: Type", None))
#endif // QT_CONFIG(tooltip)
        self.entityType.setText("")
        self.lexTypeLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type:", None))
#if QT_CONFIG(tooltip)
        self.lexType.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Lex: Type", None))
#endif // QT_CONFIG(tooltip)
        self.lexType.setText("")
        self.lexPredLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Pred:", None))
#if QT_CONFIG(tooltip)
        self.lexPred.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Lex: Pred", None))
#endif // QT_CONFIG(tooltip)
        self.lexPred.setText("")
        self.movableLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Movable:", None))
        self.scaleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Scale:", None))
#if QT_CONFIG(tooltip)
        self.embodimentMovable.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Embodiment: Movable", None))
#endif // QT_CONFIG(tooltip)
        self.embodimentMovable.setText("")
#if QT_CONFIG(tooltip)
        self.embodimentScale.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Embodiment: Scale", None))
#endif // QT_CONFIG(tooltip)
        self.attributesLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Attrs:", None))
        self.attrsDel0.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attributesAttrsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.attributesAttrsNewItem.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.attrsVal0.setPlaceholderText("")
        self.attrsDel1.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsVal1.setPlaceholderText("")
        self.attrsDel2.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsVal2.setPlaceholderText("")
        self.attrsDel3.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsVal3.setPlaceholderText("")
        self.attrsDel4.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsVal4.setPlaceholderText("")
        self.attrsDel6.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsDel5.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attrsVal6.setPlaceholderText("")
        self.attrsVal5.setPlaceholderText("")
        self.affordancesLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"<html><head/><body><p>Affordances:</p></body></html>", None))
        self.afforDel0.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.affordStrAffordancesAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.affordStrAffordancesNewItem.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Formula", None))
        self.afforVal0.setPlaceholderText("")
        self.afforVal1.setPlaceholderText("")
        self.afforDel1.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.afforVal2.setPlaceholderText("")
        self.afforDel3.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.afforDel2.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.afforVal3.setPlaceholderText("")
        self.afforVal4.setPlaceholderText("")
        self.afforDel5.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.afforDel4.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.afforVal5.setPlaceholderText("")
        self.afforVal6.setPlaceholderText("")
        self.afforDel6.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.intrinsicLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"<html><head/><body><p>Intrinsic:</p></body></html>", None))
        self.habitatIntrinsic.setCurrentText("")
        self.habitatIntrinsic.setPlaceholderText("")
        self.habitatIntrinsicDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.habitatIntrinsicAdder.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.habitatIntrName.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Name", None))
        self.habitatIntrValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.extrinsicLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Extrinsic:", None))
        self.habitatExtrName.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Name", None))
        self.habitatExtrValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.habitatExtrinsic.setCurrentText("")
        self.habitatExtrinsic.setPlaceholderText("")
        self.habitatExtrinsicAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.habitatExtrinsicDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.typeHeadLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.typeHeadLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Head:", None))
#if QT_CONFIG(tooltip)
        self.typeHead.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Head", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.typeConcavity.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type Concavity", None))
#endif // QT_CONFIG(tooltip)
        self.typeConcavityLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Concavity:", None))
#if QT_CONFIG(tooltip)
        self.typeClass.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Class", None))
#endif // QT_CONFIG(tooltip)
        self.typeClassLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Class:", None))
#if QT_CONFIG(tooltip)
        self.typeValue.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Value", None))
#endif // QT_CONFIG(tooltip)
        self.typeValueLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Value:", None))
#if QT_CONFIG(tooltip)
        self.typeScale.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Scale", None))
#endif // QT_CONFIG(tooltip)
        self.typeReferentLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Referent:", None))
#if QT_CONFIG(tooltip)
        self.typeConstr.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Constr", None))
#endif // QT_CONFIG(tooltip)
        self.typeArityLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Arity:", None))
#if QT_CONFIG(tooltip)
        self.typeReferent.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Referent", None))
#endif // QT_CONFIG(tooltip)
        self.typeConstrLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Constr:", None))
        self.typeScaleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Scale:", None))
#if QT_CONFIG(tooltip)
        self.typeArity.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Arity", None))
#endif // QT_CONFIG(tooltip)
        self.typeMappingLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Mapping:", None))
#if QT_CONFIG(tooltip)
        self.typeMapping.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Mapping", None))
#endif // QT_CONFIG(tooltip)
        self.typeComponentsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Components:", None))
#if QT_CONFIG(tooltip)
        self.typeComponentsValue.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"New Component Value", None))
#endif // QT_CONFIG(tooltip)
        self.typeComponentsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
#if QT_CONFIG(tooltip)
        self.typeComponents.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Components", None))
#endif // QT_CONFIG(tooltip)
        self.typeComponents.setCurrentText("")
        self.typeComponents.setPlaceholderText("")
        self.typeComponentsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.typeComponentsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.typeArgsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Args:", None))
        self.typeArgsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.typeArgs.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Args", None))
#endif // QT_CONFIG(tooltip)
        self.typeArgs.setCurrentText("")
        self.typeArgs.setPlaceholderText("")
        self.typeArgsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.typeArgsValue.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"New Arg Value", None))
#endif // QT_CONFIG(tooltip)
        self.typeArgsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.typeBodyLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Body:", None))
        self.typeBodyAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.typeBody.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Body", None))
#endif // QT_CONFIG(tooltip)
        self.typeBody.setCurrentText("")
        self.typeBody.setPlaceholderText("")
        self.typeBodyDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.typeBodySubeventValue.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"New Subevent Value", None))
#endif // QT_CONFIG(tooltip)
        self.typeBodySubeventValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Subevent: Value", None))
        self.typeCorrespsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Corresps:", None))
        self.typeCorrespsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.typeCorresps.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: Corresps", None))
#endif // QT_CONFIG(tooltip)
        self.typeCorresps.setCurrentText("")
        self.typeCorresps.setPlaceholderText("")
        self.typeCorrespsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.typeCorrespsValue.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"New Corresp Value", None))
#endif // QT_CONFIG(tooltip)
        self.typeCorrespsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.typeRotatSymLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"RotatSym:", None))
#if QT_CONFIG(tooltip)
        self.typeRotatSymX.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: RotatSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeRotatSymX.setText(QCoreApplication.translate("MainVoxMLWindow", u"X", None))
#if QT_CONFIG(tooltip)
        self.typeRotatSymY.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: RotatSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeRotatSymY.setText(QCoreApplication.translate("MainVoxMLWindow", u"Y", None))
#if QT_CONFIG(tooltip)
        self.typeRotatSymZ.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: RotatSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeRotatSymZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"Z", None))
#if QT_CONFIG(tooltip)
        self.typeReflSymYZ.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: ReflSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeReflSymYZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"YZ", None))
        self.typeReflSymLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"ReflSym:", None))
#if QT_CONFIG(tooltip)
        self.typeReflSymXZ.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: ReflSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeReflSymXZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"XZ", None))
#if QT_CONFIG(tooltip)
        self.typeReflSymXY.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Type: ReflSym", None))
#endif // QT_CONFIG(tooltip)
        self.typeReflSymXY.setText(QCoreApplication.translate("MainVoxMLWindow", u"XY", None))
#if QT_CONFIG(tooltip)
        self.createVoxMLButton.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Create VoxML Data based on template", None))
#endif // QT_CONFIG(tooltip)
        self.createVoxMLButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Create VoxMLData", None))
        self.templateChooser.setItemText(0, QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setItemText(1, QCoreApplication.translate("MainVoxMLWindow", u"Attribute", None))
        self.templateChooser.setItemText(2, QCoreApplication.translate("MainVoxMLWindow", u"Function", None))
        self.templateChooser.setItemText(3, QCoreApplication.translate("MainVoxMLWindow", u"Object", None))
        self.templateChooser.setItemText(4, QCoreApplication.translate("MainVoxMLWindow", u"Program", None))
        self.templateChooser.setItemText(5, QCoreApplication.translate("MainVoxMLWindow", u"Relation", None))

#if QT_CONFIG(tooltip)
        self.templateChooser.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Choose a Template for your VoxML Object.", None))
#endif // QT_CONFIG(tooltip)
        self.templateChooser.setCurrentText(QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.templateLabel.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Not here. To the right!", None))
#endif // QT_CONFIG(tooltip)
        self.templateLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Template:", None))
#if QT_CONFIG(tooltip)
        self.saveVoxMLData.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Save your VoxMLObject to a file. (Press -Save- beforehand).", None))
#endif // QT_CONFIG(tooltip)
        self.saveVoxMLData.setText(QCoreApplication.translate("MainVoxMLWindow", u"Save To File", None))
#if QT_CONFIG(tooltip)
        self.saveToObject.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Save your edits to your VoxML Object", None))
#endif // QT_CONFIG(tooltip)
        self.saveToObject.setText(QCoreApplication.translate("MainVoxMLWindow", u"Save To Object", None))
        self.popupText.setText(QCoreApplication.translate("MainVoxMLWindow", u"PopUP Window", None))
#if QT_CONFIG(tooltip)
        self.templateLabel_2.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Not here. To the right!", None))
#endif // QT_CONFIG(tooltip)
        self.templateLabel_2.setText(QCoreApplication.translate("MainVoxMLWindow", u"Open:", None))
#if QT_CONFIG(tooltip)
        self.open3DObjectButton.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Import 3D Object from file", None))
#endif // QT_CONFIG(tooltip)
        self.open3DObjectButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"3D Object", None))
#if QT_CONFIG(tooltip)
        self.openImageButton.setToolTip(QCoreApplication.translate("MainVoxMLWindow", u"Import Image from file", None))
#endif // QT_CONFIG(tooltip)
        self.openImageButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Image", None))
    # retranslateUi

