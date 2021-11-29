# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVoxMLWindowSWyeSx.ui'
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
        self.entityTypeLabel.setGeometry(QRect(280, 250, 120, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.entityTypeLabel.setFont(font3)
        self.entityType = QLineEdit(self.entityFrame)
        self.entityType.setObjectName(u"entityType")
        self.entityType.setGeometry(QRect(400, 250, 150, 30))
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
        self.lexTypeLabel.setGeometry(QRect(280, 275, 120, 30))
        self.lexTypeLabel.setFont(font3)
        self.lexType = QLineEdit(self.lexFrame)
        self.lexType.setObjectName(u"lexType")
        self.lexType.setGeometry(QRect(400, 275, 150, 30))
        self.lexType.setFont(font3)
        self.lexType.setAlignment(Qt.AlignCenter)
        self.lexPredLabel = QLabel(self.lexFrame)
        self.lexPredLabel.setObjectName(u"lexPredLabel")
        self.lexPredLabel.setGeometry(QRect(280, 225, 120, 30))
        self.lexPredLabel.setFont(font3)
        self.lexPred = QLineEdit(self.lexFrame)
        self.lexPred.setObjectName(u"lexPred")
        self.lexPred.setGeometry(QRect(400, 225, 150, 30))
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
        self.movableLabel.setGeometry(QRect(280, 275, 120, 30))
        self.movableLabel.setFont(font3)
        self.scaleLabel = QLabel(self.embodimentFrame)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setGeometry(QRect(280, 225, 120, 30))
        self.scaleLabel.setFont(font3)
        self.embodimentMovable = QCheckBox(self.embodimentFrame)
        self.embodimentMovable.setObjectName(u"embodimentMovable")
        self.embodimentMovable.setGeometry(QRect(460, 275, 30, 30))
        self.embodimentScale = QComboBox(self.embodimentFrame)
        self.embodimentScale.addItem("")
        self.embodimentScale.addItem("")
        self.embodimentScale.addItem("")
        self.embodimentScale.setObjectName(u"embodimentScale")
        self.embodimentScale.setGeometry(QRect(400, 225, 160, 30))
        self.embodimentScale.setFont(font3)
        self.embodimentScale.setStyleSheet(u"QComboBox {\n"
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
        self.attributesLabel.setGeometry(QRect(280, 225, 120, 30))
        self.attributesLabel.setFont(font3)
        self.attributesAttrs = QComboBox(self.attributesFrame)
        self.attributesAttrs.setObjectName(u"attributesAttrs")
        self.attributesAttrs.setGeometry(QRect(400, 225, 160, 30))
        self.attributesAttrs.setFont(font3)
        self.attributesAttrs.setStyleSheet(u"QComboBox {\n"
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
        self.attributesAttrsDelete = QPushButton(self.attributesFrame)
        self.attributesAttrsDelete.setObjectName(u"attributesAttrsDelete")
        self.attributesAttrsDelete.setGeometry(QRect(570, 225, 100, 30))
        self.attributesAttrsDelete.setFont(font2)
        self.attributesAttrsDelete.setStyleSheet(u"QPushButton {\n"
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
        self.attributesAttrsAdd.setGeometry(QRect(570, 265, 100, 30))
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
        self.attributesAttrsNewItem.setGeometry(QRect(400, 265, 160, 30))
        self.attributesAttrsNewItem.setFont(font3)
        self.attributesAttrsNewItem.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
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
        self.affordancesLabel.setGeometry(QRect(280, 225, 120, 30))
        self.affordancesLabel.setFont(font3)
        self.affordStrAffordances = QComboBox(self.affordStrFrame)
        self.affordStrAffordances.setObjectName(u"affordStrAffordances")
        self.affordStrAffordances.setGeometry(QRect(400, 225, 160, 30))
        self.affordStrAffordances.setFont(font3)
        self.affordStrAffordances.setStyleSheet(u"QComboBox {\n"
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
        self.affordStrAffordancesDelete = QPushButton(self.affordStrFrame)
        self.affordStrAffordancesDelete.setObjectName(u"affordStrAffordancesDelete")
        self.affordStrAffordancesDelete.setGeometry(QRect(570, 225, 100, 30))
        self.affordStrAffordancesDelete.setFont(font2)
        self.affordStrAffordancesDelete.setStyleSheet(u"QPushButton {\n"
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
        self.affordStrAffordancesAdd.setGeometry(QRect(570, 265, 100, 30))
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
        self.affordStrAffordancesNewItem.setGeometry(QRect(400, 265, 160, 30))
        self.affordStrAffordancesNewItem.setFont(font3)
        self.affordStrAffordancesNewItem.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
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
        self.intrinsicLabel.setGeometry(QRect(250, 175, 120, 30))
        self.intrinsicLabel.setFont(font3)
        self.habitatIntrinsic = QComboBox(self.habitatFrame)
        self.habitatIntrinsic.setObjectName(u"habitatIntrinsic")
        self.habitatIntrinsic.setGeometry(QRect(370, 175, 190, 30))
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
        self.habitatIntrinsicDelete.setGeometry(QRect(570, 175, 100, 30))
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
        self.habitatIntrinsicAdder.setGeometry(QRect(570, 215, 100, 30))
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
        self.habitatIntrName.setGeometry(QRect(370, 215, 90, 30))
        self.habitatIntrName.setFont(font3)
        self.habitatIntrName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatIntrValue = QLineEdit(self.habitatFrame)
        self.habitatIntrValue.setObjectName(u"habitatIntrValue")
        self.habitatIntrValue.setGeometry(QRect(470, 215, 90, 30))
        self.habitatIntrValue.setFont(font3)
        self.habitatIntrValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.extrinsicLabel = QLabel(self.habitatFrame)
        self.extrinsicLabel.setObjectName(u"extrinsicLabel")
        self.extrinsicLabel.setGeometry(QRect(250, 280, 120, 30))
        self.extrinsicLabel.setFont(font3)
        self.habitatExtrName = QLineEdit(self.habitatFrame)
        self.habitatExtrName.setObjectName(u"habitatExtrName")
        self.habitatExtrName.setGeometry(QRect(370, 320, 90, 30))
        self.habitatExtrName.setFont(font3)
        self.habitatExtrName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrValue = QLineEdit(self.habitatFrame)
        self.habitatExtrValue.setObjectName(u"habitatExtrValue")
        self.habitatExtrValue.setGeometry(QRect(470, 320, 90, 30))
        self.habitatExtrValue.setFont(font3)
        self.habitatExtrValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrinsic = QComboBox(self.habitatFrame)
        self.habitatExtrinsic.setObjectName(u"habitatExtrinsic")
        self.habitatExtrinsic.setGeometry(QRect(370, 280, 190, 30))
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
        self.habitatExtrinsicAdd.setGeometry(QRect(570, 320, 100, 30))
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
        self.habitatExtrinsicDelete.setGeometry(QRect(570, 280, 100, 30))
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
        self.typeRefrentLabel = QLabel(self.typeFrame)
        self.typeRefrentLabel.setObjectName(u"typeRefrentLabel")
        self.typeRefrentLabel.setGeometry(QRect(30, 405, 120, 30))
        self.typeRefrentLabel.setFont(font3)
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
        self.typeRotatSymYZ = QCheckBox(self.typeFrame)
        self.typeRotatSymYZ.setObjectName(u"typeRotatSymYZ")
        self.typeRotatSymYZ.setGeometry(QRect(640, 460, 70, 30))
        self.typeRotatSymYZ.setFont(font3)
        self.typeReflSymLabel = QLabel(self.typeFrame)
        self.typeReflSymLabel.setObjectName(u"typeReflSymLabel")
        self.typeReflSymLabel.setGeometry(QRect(360, 460, 120, 30))
        self.typeReflSymLabel.setFont(font3)
        self.typeRotatSymXZ = QCheckBox(self.typeFrame)
        self.typeRotatSymXZ.setObjectName(u"typeRotatSymXZ")
        self.typeRotatSymXZ.setGeometry(QRect(560, 460, 70, 30))
        self.typeRotatSymXZ.setFont(font3)
        self.typeRotatSymXY = QCheckBox(self.typeFrame)
        self.typeRotatSymXY.setObjectName(u"typeRotatSymXY")
        self.typeRotatSymXY.setGeometry(QRect(480, 460, 70, 30))
        self.typeRotatSymXY.setFont(font3)
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
        self.templateLabel.setGeometry(QRect(390, 120, 100, 28))
        self.templateLabel.setFont(font3)
        self.templateLabel.setStyleSheet(u"QLabel {\n"
"	background-color: None;\n"
"	color: #2b78d3;\n"
"	border: None;\n"
"}")
        self.templateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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

        self.embodimentScale.setCurrentIndex(0)
        self.attributesAttrs.setCurrentIndex(-1)
        self.affordStrAffordances.setCurrentIndex(-1)
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
        self.exitButton.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"VoxML Annotator", None))
        self.openVoxMLDataButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Open VoxMLData", None))
        self.entityBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Entity", None))
        self.lexBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Lex", None))
        self.typeBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type", None))
        self.habitatBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Habitat", None))
        self.attributesBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Attributes", None))
        self.embodimentBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"Embodiment", None))
        self.affordStrBtn.setText(QCoreApplication.translate("MainVoxMLWindow", u"AffordStr", None))
        self.entityTypeLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type:", None))
        self.entityType.setText("")
        self.lexTypeLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Type:", None))
        self.lexType.setText("")
        self.lexPredLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Pred:", None))
        self.lexPred.setText("")
        self.movableLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Movable:", None))
        self.scaleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Scale:", None))
        self.embodimentMovable.setText("")
        self.embodimentScale.setItemText(0, QCoreApplication.translate("MainVoxMLWindow", u"< agent", None))
        self.embodimentScale.setItemText(1, QCoreApplication.translate("MainVoxMLWindow", u"> agent", None))
        self.embodimentScale.setItemText(2, QCoreApplication.translate("MainVoxMLWindow", u"agent", None))

        self.embodimentScale.setCurrentText(QCoreApplication.translate("MainVoxMLWindow", u"< agent", None))
        self.embodimentScale.setPlaceholderText("")
        self.attributesLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Attrs:", None))
        self.attributesAttrs.setCurrentText("")
        self.attributesAttrs.setPlaceholderText("")
        self.attributesAttrsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.attributesAttrsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.attributesAttrsNewItem.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.affordancesLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"<html><head/><body><p>Affordances:</p></body></html>", None))
        self.affordStrAffordances.setCurrentText("")
        self.affordStrAffordances.setPlaceholderText("")
        self.affordStrAffordancesDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.affordStrAffordancesAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.affordStrAffordancesNewItem.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Formula", None))
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
        self.typeHeadLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Head:", None))
        self.typeConcavityLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Concavity:", None))
        self.typeClassLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Class:", None))
        self.typeValueLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Value:", None))
        self.typeRefrentLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Referent:", None))
        self.typeArityLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Arity:", None))
        self.typeConstrLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Constr:", None))
        self.typeScaleLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Scale:", None))
        self.typeMappingLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Mapping:", None))
        self.typeComponentsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Components:", None))
        self.typeComponentsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.typeComponents.setCurrentText("")
        self.typeComponents.setPlaceholderText("")
        self.typeComponentsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.typeComponentsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.typeArgsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Args:", None))
        self.typeArgsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.typeArgs.setCurrentText("")
        self.typeArgs.setPlaceholderText("")
        self.typeArgsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.typeArgsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.typeBodyLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Body:", None))
        self.typeBodyAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.typeBody.setCurrentText("")
        self.typeBody.setPlaceholderText("")
        self.typeBodyDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.typeBodySubeventValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Subevent: Value", None))
        self.typeCorrespsLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Corresps:", None))
        self.typeCorrespsAdd.setText(QCoreApplication.translate("MainVoxMLWindow", u"Add", None))
        self.typeCorresps.setCurrentText("")
        self.typeCorresps.setPlaceholderText("")
        self.typeCorrespsDelete.setText(QCoreApplication.translate("MainVoxMLWindow", u"Delete", None))
        self.typeCorrespsValue.setPlaceholderText(QCoreApplication.translate("MainVoxMLWindow", u"Value", None))
        self.typeRotatSymLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"RotatSym:", None))
        self.typeRotatSymX.setText(QCoreApplication.translate("MainVoxMLWindow", u"X", None))
        self.typeRotatSymY.setText(QCoreApplication.translate("MainVoxMLWindow", u"Y", None))
        self.typeRotatSymZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"Z", None))
        self.typeRotatSymYZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"YZ", None))
        self.typeReflSymLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"ReflSym:", None))
        self.typeRotatSymXZ.setText(QCoreApplication.translate("MainVoxMLWindow", u"XZ", None))
        self.typeRotatSymXY.setText(QCoreApplication.translate("MainVoxMLWindow", u"XY", None))
        self.createVoxMLButton.setText(QCoreApplication.translate("MainVoxMLWindow", u"Create VoxMLData", None))
        self.templateChooser.setItemText(0, QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setItemText(1, QCoreApplication.translate("MainVoxMLWindow", u"Attribute", None))
        self.templateChooser.setItemText(2, QCoreApplication.translate("MainVoxMLWindow", u"Function", None))
        self.templateChooser.setItemText(3, QCoreApplication.translate("MainVoxMLWindow", u"Object", None))
        self.templateChooser.setItemText(4, QCoreApplication.translate("MainVoxMLWindow", u"Program", None))
        self.templateChooser.setItemText(5, QCoreApplication.translate("MainVoxMLWindow", u"Relation", None))

        self.templateChooser.setCurrentText(QCoreApplication.translate("MainVoxMLWindow", u"Empty", None))
        self.templateChooser.setPlaceholderText("")
        self.templateLabel.setText(QCoreApplication.translate("MainVoxMLWindow", u"Template:", None))
        self.saveVoxMLData.setText(QCoreApplication.translate("MainVoxMLWindow", u"Save VoxMLData", None))
    # retranslateUi

