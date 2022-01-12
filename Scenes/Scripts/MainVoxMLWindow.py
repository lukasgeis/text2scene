# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scenes/UI/MainVoxMLWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainVoxMLWindow(object):
    def setupUi(self, MainVoxMLWindow):
        MainVoxMLWindow.setObjectName("MainVoxMLWindow")
        MainVoxMLWindow.resize(1620, 820)
        self.mainWidget = QtWidgets.QWidget(MainVoxMLWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.backgroundFrame = QtWidgets.QFrame(self.mainWidget)
        self.backgroundFrame.setGeometry(QtCore.QRect(10, 10, 1600, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundFrame.sizePolicy().hasHeightForWidth())
        self.backgroundFrame.setSizePolicy(sizePolicy)
        self.backgroundFrame.setStyleSheet("QFrame#backgroundFrame {\n"
"    border-radius: 20px;\n"
"    border: None;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    color: #f0f0f0;\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.exitButton = QtWidgets.QPushButton(self.backgroundFrame)
        self.exitButton.setGeometry(QtCore.QRect(1550, 10, 40, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton {\n"
"    background-color: #f62451;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f0f0f0;\n"
"}")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.titleLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.titleLabel.setGeometry(QtCore.QRect(20, 20, 600, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
"    border-radius: 0px;\n"
"    background-color: None;\n"
"    color: #f0f0f0;\n"
"    border: None;\n"
"}")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.openVoxMLDataButton = QtWidgets.QPushButton(self.backgroundFrame)
        self.openVoxMLDataButton.setGeometry(QtCore.QRect(1080, 120, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.openVoxMLDataButton.setFont(font)
        self.openVoxMLDataButton.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}")
        self.openVoxMLDataButton.setObjectName("openVoxMLDataButton")
        self.editingFrame = QtWidgets.QFrame(self.backgroundFrame)
        self.editingFrame.setGeometry(QtCore.QRect(30, 170, 800, 600))
        self.editingFrame.setStyleSheet("QFrame#editingFrame {\n"
"    border: 2px solid #f0f0f0;\n"
"    background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border-top-right-radius: 20px;\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: 2px solid #f0f0f0;\n"
"    background-color: qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"}")
        self.editingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editingFrame.setObjectName("editingFrame")
        self.entityBtn = QtWidgets.QPushButton(self.editingFrame)
        self.entityBtn.setGeometry(QtCore.QRect(20, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.entityBtn.setFont(font)
        self.entityBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.entityBtn.setObjectName("entityBtn")
        self.lexBtn = QtWidgets.QPushButton(self.editingFrame)
        self.lexBtn.setGeometry(QtCore.QRect(130, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lexBtn.setFont(font)
        self.lexBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.lexBtn.setObjectName("lexBtn")
        self.typeBtn = QtWidgets.QPushButton(self.editingFrame)
        self.typeBtn.setGeometry(QtCore.QRect(240, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeBtn.setFont(font)
        self.typeBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.typeBtn.setObjectName("typeBtn")
        self.habitatBtn = QtWidgets.QPushButton(self.editingFrame)
        self.habitatBtn.setGeometry(QtCore.QRect(350, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.habitatBtn.setFont(font)
        self.habitatBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.habitatBtn.setObjectName("habitatBtn")
        self.attributesBtn = QtWidgets.QPushButton(self.editingFrame)
        self.attributesBtn.setGeometry(QtCore.QRect(680, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attributesBtn.setFont(font)
        self.attributesBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.attributesBtn.setObjectName("attributesBtn")
        self.embodimentBtn = QtWidgets.QPushButton(self.editingFrame)
        self.embodimentBtn.setGeometry(QtCore.QRect(570, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.embodimentBtn.setFont(font)
        self.embodimentBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.embodimentBtn.setObjectName("embodimentBtn")
        self.affordStrBtn = QtWidgets.QPushButton(self.editingFrame)
        self.affordStrBtn.setGeometry(QtCore.QRect(460, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.affordStrBtn.setFont(font)
        self.affordStrBtn.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #f0f0f0;\n"
"}")
        self.affordStrBtn.setObjectName("affordStrBtn")
        self.entityFrame = QtWidgets.QFrame(self.editingFrame)
        self.entityFrame.setEnabled(True)
        self.entityFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.entityFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}")
        self.entityFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entityFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entityFrame.setObjectName("entityFrame")
        self.entityTypeLabel = QtWidgets.QLabel(self.entityFrame)
        self.entityTypeLabel.setGeometry(QtCore.QRect(250, 250, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.entityTypeLabel.setFont(font)
        self.entityTypeLabel.setObjectName("entityTypeLabel")
        self.entityType = QtWidgets.QLineEdit(self.entityFrame)
        self.entityType.setGeometry(QtCore.QRect(370, 250, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.entityType.setFont(font)
        self.entityType.setText("")
        self.entityType.setAlignment(QtCore.Qt.AlignCenter)
        self.entityType.setObjectName("entityType")
        self.lexFrame = QtWidgets.QFrame(self.editingFrame)
        self.lexFrame.setEnabled(True)
        self.lexFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.lexFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}")
        self.lexFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lexFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lexFrame.setObjectName("lexFrame")
        self.lexTypeLabel = QtWidgets.QLabel(self.lexFrame)
        self.lexTypeLabel.setGeometry(QtCore.QRect(250, 275, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lexTypeLabel.setFont(font)
        self.lexTypeLabel.setObjectName("lexTypeLabel")
        self.lexType = QtWidgets.QLineEdit(self.lexFrame)
        self.lexType.setGeometry(QtCore.QRect(370, 275, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lexType.setFont(font)
        self.lexType.setText("")
        self.lexType.setAlignment(QtCore.Qt.AlignCenter)
        self.lexType.setObjectName("lexType")
        self.lexPredLabel = QtWidgets.QLabel(self.lexFrame)
        self.lexPredLabel.setGeometry(QtCore.QRect(250, 225, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lexPredLabel.setFont(font)
        self.lexPredLabel.setObjectName("lexPredLabel")
        self.lexPred = QtWidgets.QLineEdit(self.lexFrame)
        self.lexPred.setGeometry(QtCore.QRect(370, 225, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lexPred.setFont(font)
        self.lexPred.setText("")
        self.lexPred.setAlignment(QtCore.Qt.AlignCenter)
        self.lexPred.setObjectName("lexPred")
        self.embodimentFrame = QtWidgets.QFrame(self.editingFrame)
        self.embodimentFrame.setEnabled(True)
        self.embodimentFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.embodimentFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #f62451;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #1fd78d;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.embodimentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.embodimentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.embodimentFrame.setObjectName("embodimentFrame")
        self.movableLabel = QtWidgets.QLabel(self.embodimentFrame)
        self.movableLabel.setGeometry(QtCore.QRect(250, 275, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.movableLabel.setFont(font)
        self.movableLabel.setObjectName("movableLabel")
        self.scaleLabel = QtWidgets.QLabel(self.embodimentFrame)
        self.scaleLabel.setGeometry(QtCore.QRect(250, 225, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.scaleLabel.setFont(font)
        self.scaleLabel.setObjectName("scaleLabel")
        self.embodimentMovable = QtWidgets.QCheckBox(self.embodimentFrame)
        self.embodimentMovable.setGeometry(QtCore.QRect(430, 275, 30, 30))
        self.embodimentMovable.setText("")
        self.embodimentMovable.setObjectName("embodimentMovable")
        self.embodimentScale = QtWidgets.QLineEdit(self.embodimentFrame)
        self.embodimentScale.setGeometry(QtCore.QRect(370, 225, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.embodimentScale.setFont(font)
        self.embodimentScale.setObjectName("embodimentScale")
        self.attributesFrame = QtWidgets.QFrame(self.editingFrame)
        self.attributesFrame.setEnabled(True)
        self.attributesFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.attributesFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #f62451;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #1fd78d;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.attributesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.attributesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attributesFrame.setObjectName("attributesFrame")
        self.attributesLabel = QtWidgets.QLabel(self.attributesFrame)
        self.attributesLabel.setGeometry(QtCore.QRect(200, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attributesLabel.setFont(font)
        self.attributesLabel.setObjectName("attributesLabel")
        self.attrsDel0 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel0.setGeometry(QtCore.QRect(470, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel0.setFont(font)
        self.attrsDel0.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel0.setObjectName("attrsDel0")
        self.attributesAttrsAdd = QtWidgets.QPushButton(self.attributesFrame)
        self.attributesAttrsAdd.setGeometry(QtCore.QRect(470, 100, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attributesAttrsAdd.setFont(font)
        self.attributesAttrsAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.attributesAttrsAdd.setObjectName("attributesAttrsAdd")
        self.attributesAttrsNewItem = QtWidgets.QLineEdit(self.attributesFrame)
        self.attributesAttrsNewItem.setGeometry(QtCore.QRect(300, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attributesAttrsNewItem.setFont(font)
        self.attributesAttrsNewItem.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.attributesAttrsNewItem.setObjectName("attributesAttrsNewItem")
        self.attrsVal0 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal0.setGeometry(QtCore.QRect(300, 150, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal0.setFont(font)
        self.attrsVal0.setStyleSheet("")
        self.attrsVal0.setPlaceholderText("")
        self.attrsVal0.setObjectName("attrsVal0")
        self.attrsDel1 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel1.setGeometry(QtCore.QRect(470, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel1.setFont(font)
        self.attrsDel1.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel1.setObjectName("attrsDel1")
        self.attrsVal1 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal1.setGeometry(QtCore.QRect(300, 190, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal1.setFont(font)
        self.attrsVal1.setStyleSheet("")
        self.attrsVal1.setPlaceholderText("")
        self.attrsVal1.setObjectName("attrsVal1")
        self.attrsDel2 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel2.setGeometry(QtCore.QRect(470, 230, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel2.setFont(font)
        self.attrsDel2.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel2.setObjectName("attrsDel2")
        self.attrsVal2 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal2.setGeometry(QtCore.QRect(300, 230, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal2.setFont(font)
        self.attrsVal2.setStyleSheet("")
        self.attrsVal2.setPlaceholderText("")
        self.attrsVal2.setObjectName("attrsVal2")
        self.attrsDel3 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel3.setGeometry(QtCore.QRect(470, 270, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel3.setFont(font)
        self.attrsDel3.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel3.setObjectName("attrsDel3")
        self.attrsVal3 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal3.setGeometry(QtCore.QRect(300, 270, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal3.setFont(font)
        self.attrsVal3.setStyleSheet("")
        self.attrsVal3.setPlaceholderText("")
        self.attrsVal3.setObjectName("attrsVal3")
        self.attrsDel4 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel4.setGeometry(QtCore.QRect(470, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel4.setFont(font)
        self.attrsDel4.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel4.setObjectName("attrsDel4")
        self.attrsVal4 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal4.setGeometry(QtCore.QRect(300, 310, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal4.setFont(font)
        self.attrsVal4.setStyleSheet("")
        self.attrsVal4.setPlaceholderText("")
        self.attrsVal4.setObjectName("attrsVal4")
        self.attrsDel6 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel6.setGeometry(QtCore.QRect(470, 390, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel6.setFont(font)
        self.attrsDel6.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel6.setObjectName("attrsDel6")
        self.attrsDel5 = QtWidgets.QPushButton(self.attributesFrame)
        self.attrsDel5.setGeometry(QtCore.QRect(470, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.attrsDel5.setFont(font)
        self.attrsDel5.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.attrsDel5.setObjectName("attrsDel5")
        self.attrsVal6 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal6.setGeometry(QtCore.QRect(300, 390, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal6.setFont(font)
        self.attrsVal6.setStyleSheet("")
        self.attrsVal6.setPlaceholderText("")
        self.attrsVal6.setObjectName("attrsVal6")
        self.attrsVal5 = QtWidgets.QLineEdit(self.attributesFrame)
        self.attrsVal5.setGeometry(QtCore.QRect(300, 350, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.attrsVal5.setFont(font)
        self.attrsVal5.setStyleSheet("")
        self.attrsVal5.setPlaceholderText("")
        self.attrsVal5.setObjectName("attrsVal5")
        self.affordStrFrame = QtWidgets.QFrame(self.editingFrame)
        self.affordStrFrame.setEnabled(True)
        self.affordStrFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.affordStrFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #f62451;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #1fd78d;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.affordStrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.affordStrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.affordStrFrame.setObjectName("affordStrFrame")
        self.affordancesLabel = QtWidgets.QLabel(self.affordStrFrame)
        self.affordancesLabel.setGeometry(QtCore.QRect(200, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.affordancesLabel.setFont(font)
        self.affordancesLabel.setObjectName("affordancesLabel")
        self.afforDel0 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel0.setGeometry(QtCore.QRect(470, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel0.setFont(font)
        self.afforDel0.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel0.setObjectName("afforDel0")
        self.affordStrAffordancesAdd = QtWidgets.QPushButton(self.affordStrFrame)
        self.affordStrAffordancesAdd.setGeometry(QtCore.QRect(470, 100, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.affordStrAffordancesAdd.setFont(font)
        self.affordStrAffordancesAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.affordStrAffordancesAdd.setObjectName("affordStrAffordancesAdd")
        self.affordStrAffordancesNewItem = QtWidgets.QLineEdit(self.affordStrFrame)
        self.affordStrAffordancesNewItem.setGeometry(QtCore.QRect(300, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.affordStrAffordancesNewItem.setFont(font)
        self.affordStrAffordancesNewItem.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.affordStrAffordancesNewItem.setObjectName("affordStrAffordancesNewItem")
        self.afforVal0 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal0.setGeometry(QtCore.QRect(300, 150, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal0.setFont(font)
        self.afforVal0.setStyleSheet("")
        self.afforVal0.setPlaceholderText("")
        self.afforVal0.setObjectName("afforVal0")
        self.afforVal1 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal1.setGeometry(QtCore.QRect(300, 190, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal1.setFont(font)
        self.afforVal1.setStyleSheet("")
        self.afforVal1.setPlaceholderText("")
        self.afforVal1.setObjectName("afforVal1")
        self.afforDel1 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel1.setGeometry(QtCore.QRect(470, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel1.setFont(font)
        self.afforDel1.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel1.setObjectName("afforDel1")
        self.afforVal2 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal2.setGeometry(QtCore.QRect(300, 230, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal2.setFont(font)
        self.afforVal2.setStyleSheet("")
        self.afforVal2.setPlaceholderText("")
        self.afforVal2.setObjectName("afforVal2")
        self.afforDel3 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel3.setGeometry(QtCore.QRect(470, 270, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel3.setFont(font)
        self.afforDel3.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel3.setObjectName("afforDel3")
        self.afforDel2 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel2.setGeometry(QtCore.QRect(470, 230, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel2.setFont(font)
        self.afforDel2.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel2.setObjectName("afforDel2")
        self.afforVal3 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal3.setGeometry(QtCore.QRect(300, 270, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal3.setFont(font)
        self.afforVal3.setStyleSheet("")
        self.afforVal3.setPlaceholderText("")
        self.afforVal3.setObjectName("afforVal3")
        self.afforVal4 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal4.setGeometry(QtCore.QRect(300, 310, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal4.setFont(font)
        self.afforVal4.setStyleSheet("")
        self.afforVal4.setPlaceholderText("")
        self.afforVal4.setObjectName("afforVal4")
        self.afforDel5 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel5.setGeometry(QtCore.QRect(470, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel5.setFont(font)
        self.afforDel5.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel5.setObjectName("afforDel5")
        self.afforDel4 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel4.setGeometry(QtCore.QRect(470, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel4.setFont(font)
        self.afforDel4.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel4.setObjectName("afforDel4")
        self.afforVal5 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal5.setGeometry(QtCore.QRect(300, 350, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal5.setFont(font)
        self.afforVal5.setStyleSheet("")
        self.afforVal5.setPlaceholderText("")
        self.afforVal5.setObjectName("afforVal5")
        self.afforVal6 = QtWidgets.QLineEdit(self.affordStrFrame)
        self.afforVal6.setGeometry(QtCore.QRect(300, 390, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.afforVal6.setFont(font)
        self.afforVal6.setStyleSheet("")
        self.afforVal6.setPlaceholderText("")
        self.afforVal6.setObjectName("afforVal6")
        self.afforDel6 = QtWidgets.QPushButton(self.affordStrFrame)
        self.afforDel6.setGeometry(QtCore.QRect(470, 390, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.afforDel6.setFont(font)
        self.afforDel6.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.afforDel6.setObjectName("afforDel6")
        self.habitatFrame = QtWidgets.QFrame(self.editingFrame)
        self.habitatFrame.setEnabled(True)
        self.habitatFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.habitatFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #f62451;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #1fd78d;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.habitatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.habitatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.habitatFrame.setObjectName("habitatFrame")
        self.intrinsicLabel = QtWidgets.QLabel(self.habitatFrame)
        self.intrinsicLabel.setGeometry(QtCore.QRect(200, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrinsicLabel.setFont(font)
        self.intrinsicLabel.setObjectName("intrinsicLabel")
        self.intrDel0 = QtWidgets.QPushButton(self.habitatFrame)
        self.intrDel0.setGeometry(QtCore.QRect(500, 65, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.intrDel0.setFont(font)
        self.intrDel0.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.intrDel0.setObjectName("intrDel0")
        self.habitatIntrinsicAdder = QtWidgets.QPushButton(self.habitatFrame)
        self.habitatIntrinsicAdder.setGeometry(QtCore.QRect(500, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.habitatIntrinsicAdder.setFont(font)
        self.habitatIntrinsicAdder.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.habitatIntrinsicAdder.setObjectName("habitatIntrinsicAdder")
        self.habitatIntrName = QtWidgets.QLineEdit(self.habitatFrame)
        self.habitatIntrName.setGeometry(QtCore.QRect(300, 20, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.habitatIntrName.setFont(font)
        self.habitatIntrName.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.habitatIntrName.setObjectName("habitatIntrName")
        self.habitatIntrValue = QtWidgets.QLineEdit(self.habitatFrame)
        self.habitatIntrValue.setGeometry(QtCore.QRect(400, 20, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.habitatIntrValue.setFont(font)
        self.habitatIntrValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.habitatIntrValue.setObjectName("habitatIntrValue")
        self.extrinsicLabel = QtWidgets.QLabel(self.habitatFrame)
        self.extrinsicLabel.setGeometry(QtCore.QRect(200, 280, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrinsicLabel.setFont(font)
        self.extrinsicLabel.setObjectName("extrinsicLabel")
        self.habitatExtrName = QtWidgets.QLineEdit(self.habitatFrame)
        self.habitatExtrName.setGeometry(QtCore.QRect(300, 280, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.habitatExtrName.setFont(font)
        self.habitatExtrName.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrName.setObjectName("habitatExtrName")
        self.habitatExtrValue = QtWidgets.QLineEdit(self.habitatFrame)
        self.habitatExtrValue.setGeometry(QtCore.QRect(400, 280, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.habitatExtrValue.setFont(font)
        self.habitatExtrValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.habitatExtrValue.setObjectName("habitatExtrValue")
        self.habitatExtrinsicAdd = QtWidgets.QPushButton(self.habitatFrame)
        self.habitatExtrinsicAdd.setGeometry(QtCore.QRect(500, 280, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.habitatExtrinsicAdd.setFont(font)
        self.habitatExtrinsicAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.habitatExtrinsicAdd.setObjectName("habitatExtrinsicAdd")
        self.intrVal0 = QtWidgets.QLineEdit(self.habitatFrame)
        self.intrVal0.setGeometry(QtCore.QRect(300, 65, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrVal0.setFont(font)
        self.intrVal0.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.intrVal0.setPlaceholderText("")
        self.intrVal0.setObjectName("intrVal0")
        self.intrVal1 = QtWidgets.QLineEdit(self.habitatFrame)
        self.intrVal1.setGeometry(QtCore.QRect(300, 105, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrVal1.setFont(font)
        self.intrVal1.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.intrVal1.setPlaceholderText("")
        self.intrVal1.setObjectName("intrVal1")
        self.intrDel1 = QtWidgets.QPushButton(self.habitatFrame)
        self.intrDel1.setGeometry(QtCore.QRect(500, 105, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.intrDel1.setFont(font)
        self.intrDel1.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.intrDel1.setObjectName("intrDel1")
        self.intrVal2 = QtWidgets.QLineEdit(self.habitatFrame)
        self.intrVal2.setGeometry(QtCore.QRect(300, 145, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrVal2.setFont(font)
        self.intrVal2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.intrVal2.setPlaceholderText("")
        self.intrVal2.setObjectName("intrVal2")
        self.intrDel2 = QtWidgets.QPushButton(self.habitatFrame)
        self.intrDel2.setGeometry(QtCore.QRect(500, 145, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.intrDel2.setFont(font)
        self.intrDel2.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.intrDel2.setObjectName("intrDel2")
        self.intrDel3 = QtWidgets.QPushButton(self.habitatFrame)
        self.intrDel3.setGeometry(QtCore.QRect(500, 185, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.intrDel3.setFont(font)
        self.intrDel3.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.intrDel3.setObjectName("intrDel3")
        self.intrVal3 = QtWidgets.QLineEdit(self.habitatFrame)
        self.intrVal3.setGeometry(QtCore.QRect(300, 185, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrVal3.setFont(font)
        self.intrVal3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.intrVal3.setPlaceholderText("")
        self.intrVal3.setObjectName("intrVal3")
        self.intrDel4 = QtWidgets.QPushButton(self.habitatFrame)
        self.intrDel4.setGeometry(QtCore.QRect(500, 225, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.intrDel4.setFont(font)
        self.intrDel4.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.intrDel4.setObjectName("intrDel4")
        self.intrVal4 = QtWidgets.QLineEdit(self.habitatFrame)
        self.intrVal4.setGeometry(QtCore.QRect(300, 225, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.intrVal4.setFont(font)
        self.intrVal4.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.intrVal4.setPlaceholderText("")
        self.intrVal4.setObjectName("intrVal4")
        self.extrDel4 = QtWidgets.QPushButton(self.habitatFrame)
        self.extrDel4.setGeometry(QtCore.QRect(500, 485, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.extrDel4.setFont(font)
        self.extrDel4.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.extrDel4.setObjectName("extrDel4")
        self.extrVal0 = QtWidgets.QLineEdit(self.habitatFrame)
        self.extrVal0.setGeometry(QtCore.QRect(300, 325, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrVal0.setFont(font)
        self.extrVal0.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.extrVal0.setPlaceholderText("")
        self.extrVal0.setObjectName("extrVal0")
        self.extrDel3 = QtWidgets.QPushButton(self.habitatFrame)
        self.extrDel3.setGeometry(QtCore.QRect(500, 445, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.extrDel3.setFont(font)
        self.extrDel3.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.extrDel3.setObjectName("extrDel3")
        self.extrVal4 = QtWidgets.QLineEdit(self.habitatFrame)
        self.extrVal4.setGeometry(QtCore.QRect(300, 485, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrVal4.setFont(font)
        self.extrVal4.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.extrVal4.setPlaceholderText("")
        self.extrVal4.setObjectName("extrVal4")
        self.extrVal2 = QtWidgets.QLineEdit(self.habitatFrame)
        self.extrVal2.setGeometry(QtCore.QRect(300, 405, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrVal2.setFont(font)
        self.extrVal2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.extrVal2.setPlaceholderText("")
        self.extrVal2.setObjectName("extrVal2")
        self.extrDel0 = QtWidgets.QPushButton(self.habitatFrame)
        self.extrDel0.setGeometry(QtCore.QRect(500, 325, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.extrDel0.setFont(font)
        self.extrDel0.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.extrDel0.setObjectName("extrDel0")
        self.extrDel1 = QtWidgets.QPushButton(self.habitatFrame)
        self.extrDel1.setGeometry(QtCore.QRect(500, 365, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.extrDel1.setFont(font)
        self.extrDel1.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.extrDel1.setObjectName("extrDel1")
        self.extrVal3 = QtWidgets.QLineEdit(self.habitatFrame)
        self.extrVal3.setGeometry(QtCore.QRect(300, 445, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrVal3.setFont(font)
        self.extrVal3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.extrVal3.setPlaceholderText("")
        self.extrVal3.setObjectName("extrVal3")
        self.extrDel2 = QtWidgets.QPushButton(self.habitatFrame)
        self.extrDel2.setGeometry(QtCore.QRect(500, 405, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.extrDel2.setFont(font)
        self.extrDel2.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.extrDel2.setObjectName("extrDel2")
        self.extrVal1 = QtWidgets.QLineEdit(self.habitatFrame)
        self.extrVal1.setGeometry(QtCore.QRect(300, 365, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.extrVal1.setFont(font)
        self.extrVal1.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2d87d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid #2d87d3;\n"
"}")
        self.extrVal1.setPlaceholderText("")
        self.extrVal1.setObjectName("extrVal1")
        self.typeFrame = QtWidgets.QFrame(self.editingFrame)
        self.typeFrame.setEnabled(True)
        self.typeFrame.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.typeFrame.setStyleSheet("QLabel {\n"
"    border: None;\n"
"    color: #2b78d3;\n"
"    background: None;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #2b78d3;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #f62451;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0.063, y1:0.937318, x2:1, y2:0, stop:0 rgba(22,28,33,255), stop:1 rgba(45,57,67,255));\n"
"    border: 2px solid #1fd78d;\n"
"    border-radius: 3px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.typeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.typeFrame.setObjectName("typeFrame")
        self.typeHeadLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeHeadLabel.setGeometry(QtCore.QRect(30, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeHeadLabel.setFont(font)
        self.typeHeadLabel.setToolTip("")
        self.typeHeadLabel.setObjectName("typeHeadLabel")
        self.typeHead = QtWidgets.QLineEdit(self.typeFrame)
        self.typeHead.setGeometry(QtCore.QRect(160, 20, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeHead.setFont(font)
        self.typeHead.setObjectName("typeHead")
        self.typeConcavity = QtWidgets.QLineEdit(self.typeFrame)
        self.typeConcavity.setGeometry(QtCore.QRect(160, 75, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeConcavity.setFont(font)
        self.typeConcavity.setObjectName("typeConcavity")
        self.typeConcavityLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeConcavityLabel.setGeometry(QtCore.QRect(30, 75, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeConcavityLabel.setFont(font)
        self.typeConcavityLabel.setObjectName("typeConcavityLabel")
        self.typeClass = QtWidgets.QLineEdit(self.typeFrame)
        self.typeClass.setGeometry(QtCore.QRect(160, 130, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeClass.setFont(font)
        self.typeClass.setObjectName("typeClass")
        self.typeClassLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeClassLabel.setGeometry(QtCore.QRect(30, 130, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeClassLabel.setFont(font)
        self.typeClassLabel.setObjectName("typeClassLabel")
        self.typeValue = QtWidgets.QLineEdit(self.typeFrame)
        self.typeValue.setGeometry(QtCore.QRect(160, 185, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeValue.setFont(font)
        self.typeValue.setObjectName("typeValue")
        self.typeValueLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeValueLabel.setGeometry(QtCore.QRect(30, 185, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeValueLabel.setFont(font)
        self.typeValueLabel.setObjectName("typeValueLabel")
        self.typeScale = QtWidgets.QLineEdit(self.typeFrame)
        self.typeScale.setGeometry(QtCore.QRect(160, 295, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeScale.setFont(font)
        self.typeScale.setObjectName("typeScale")
        self.typeReferentLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeReferentLabel.setGeometry(QtCore.QRect(30, 405, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReferentLabel.setFont(font)
        self.typeReferentLabel.setObjectName("typeReferentLabel")
        self.typeConstr = QtWidgets.QLineEdit(self.typeFrame)
        self.typeConstr.setGeometry(QtCore.QRect(160, 240, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeConstr.setFont(font)
        self.typeConstr.setObjectName("typeConstr")
        self.typeArityLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeArityLabel.setGeometry(QtCore.QRect(30, 350, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeArityLabel.setFont(font)
        self.typeArityLabel.setObjectName("typeArityLabel")
        self.typeReferent = QtWidgets.QLineEdit(self.typeFrame)
        self.typeReferent.setGeometry(QtCore.QRect(160, 405, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReferent.setFont(font)
        self.typeReferent.setObjectName("typeReferent")
        self.typeConstrLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeConstrLabel.setGeometry(QtCore.QRect(30, 240, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeConstrLabel.setFont(font)
        self.typeConstrLabel.setObjectName("typeConstrLabel")
        self.typeScaleLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeScaleLabel.setGeometry(QtCore.QRect(30, 295, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeScaleLabel.setFont(font)
        self.typeScaleLabel.setObjectName("typeScaleLabel")
        self.typeArity = QtWidgets.QLineEdit(self.typeFrame)
        self.typeArity.setGeometry(QtCore.QRect(160, 350, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeArity.setFont(font)
        self.typeArity.setObjectName("typeArity")
        self.typeMappingLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeMappingLabel.setGeometry(QtCore.QRect(30, 460, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeMappingLabel.setFont(font)
        self.typeMappingLabel.setObjectName("typeMappingLabel")
        self.typeMapping = QtWidgets.QLineEdit(self.typeFrame)
        self.typeMapping.setGeometry(QtCore.QRect(160, 460, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeMapping.setFont(font)
        self.typeMapping.setObjectName("typeMapping")
        self.typeComponentsLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeComponentsLabel.setGeometry(QtCore.QRect(360, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeComponentsLabel.setFont(font)
        self.typeComponentsLabel.setObjectName("typeComponentsLabel")
        self.typeComponentsValue = QtWidgets.QLineEdit(self.typeFrame)
        self.typeComponentsValue.setGeometry(QtCore.QRect(480, 60, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeComponentsValue.setFont(font)
        self.typeComponentsValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.typeComponentsValue.setObjectName("typeComponentsValue")
        self.typeComponents = QtWidgets.QComboBox(self.typeFrame)
        self.typeComponents.setGeometry(QtCore.QRect(480, 20, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeComponents.setFont(font)
        self.typeComponents.setStyleSheet("QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #2b78d3;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.typeComponents.setCurrentText("")
        self.typeComponents.setProperty("placeholderText", "")
        self.typeComponents.setObjectName("typeComponents")
        self.typeComponentsAdd = QtWidgets.QPushButton(self.typeFrame)
        self.typeComponentsAdd.setGeometry(QtCore.QRect(680, 60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeComponentsAdd.setFont(font)
        self.typeComponentsAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.typeComponentsAdd.setObjectName("typeComponentsAdd")
        self.typeComponentsDelete = QtWidgets.QPushButton(self.typeFrame)
        self.typeComponentsDelete.setGeometry(QtCore.QRect(680, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeComponentsDelete.setFont(font)
        self.typeComponentsDelete.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.typeComponentsDelete.setObjectName("typeComponentsDelete")
        self.typeArgsLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeArgsLabel.setGeometry(QtCore.QRect(360, 110, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeArgsLabel.setFont(font)
        self.typeArgsLabel.setObjectName("typeArgsLabel")
        self.typeArgsAdd = QtWidgets.QPushButton(self.typeFrame)
        self.typeArgsAdd.setGeometry(QtCore.QRect(680, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeArgsAdd.setFont(font)
        self.typeArgsAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.typeArgsAdd.setObjectName("typeArgsAdd")
        self.typeArgs = QtWidgets.QComboBox(self.typeFrame)
        self.typeArgs.setGeometry(QtCore.QRect(480, 110, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeArgs.setFont(font)
        self.typeArgs.setStyleSheet("QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #2b78d3;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.typeArgs.setCurrentText("")
        self.typeArgs.setProperty("placeholderText", "")
        self.typeArgs.setObjectName("typeArgs")
        self.typeArgsDelete = QtWidgets.QPushButton(self.typeFrame)
        self.typeArgsDelete.setGeometry(QtCore.QRect(680, 110, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeArgsDelete.setFont(font)
        self.typeArgsDelete.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.typeArgsDelete.setObjectName("typeArgsDelete")
        self.typeArgsValue = QtWidgets.QLineEdit(self.typeFrame)
        self.typeArgsValue.setGeometry(QtCore.QRect(480, 150, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeArgsValue.setFont(font)
        self.typeArgsValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.typeArgsValue.setObjectName("typeArgsValue")
        self.typeBodyLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeBodyLabel.setGeometry(QtCore.QRect(360, 200, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeBodyLabel.setFont(font)
        self.typeBodyLabel.setObjectName("typeBodyLabel")
        self.typeBodyAdd = QtWidgets.QPushButton(self.typeFrame)
        self.typeBodyAdd.setGeometry(QtCore.QRect(680, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeBodyAdd.setFont(font)
        self.typeBodyAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.typeBodyAdd.setObjectName("typeBodyAdd")
        self.typeBody = QtWidgets.QComboBox(self.typeFrame)
        self.typeBody.setGeometry(QtCore.QRect(480, 200, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeBody.setFont(font)
        self.typeBody.setStyleSheet("QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #2b78d3;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.typeBody.setCurrentText("")
        self.typeBody.setProperty("placeholderText", "")
        self.typeBody.setObjectName("typeBody")
        self.typeBodyDelete = QtWidgets.QPushButton(self.typeFrame)
        self.typeBodyDelete.setGeometry(QtCore.QRect(680, 200, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeBodyDelete.setFont(font)
        self.typeBodyDelete.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.typeBodyDelete.setObjectName("typeBodyDelete")
        self.typeBodySubeventValue = QtWidgets.QLineEdit(self.typeFrame)
        self.typeBodySubeventValue.setGeometry(QtCore.QRect(480, 240, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeBodySubeventValue.setFont(font)
        self.typeBodySubeventValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.typeBodySubeventValue.setObjectName("typeBodySubeventValue")
        self.typeCorrespsLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeCorrespsLabel.setGeometry(QtCore.QRect(360, 290, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeCorrespsLabel.setFont(font)
        self.typeCorrespsLabel.setObjectName("typeCorrespsLabel")
        self.typeCorrespsAdd = QtWidgets.QPushButton(self.typeFrame)
        self.typeCorrespsAdd.setGeometry(QtCore.QRect(680, 330, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeCorrespsAdd.setFont(font)
        self.typeCorrespsAdd.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.typeCorrespsAdd.setObjectName("typeCorrespsAdd")
        self.typeCorresps = QtWidgets.QComboBox(self.typeFrame)
        self.typeCorresps.setGeometry(QtCore.QRect(480, 290, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeCorresps.setFont(font)
        self.typeCorresps.setStyleSheet("QComboBox {\n"
"    border: 1px solid #2b78d3;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #2b78d3;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.typeCorresps.setCurrentText("")
        self.typeCorresps.setProperty("placeholderText", "")
        self.typeCorresps.setObjectName("typeCorresps")
        self.typeCorrespsDelete = QtWidgets.QPushButton(self.typeFrame)
        self.typeCorrespsDelete.setGeometry(QtCore.QRect(680, 290, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.typeCorrespsDelete.setFont(font)
        self.typeCorrespsDelete.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #f62451;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #f62451;\n"
"}")
        self.typeCorrespsDelete.setObjectName("typeCorrespsDelete")
        self.typeCorrespsValue = QtWidgets.QLineEdit(self.typeFrame)
        self.typeCorrespsValue.setGeometry(QtCore.QRect(480, 330, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeCorrespsValue.setFont(font)
        self.typeCorrespsValue.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #f0f0f0;\n"
"}")
        self.typeCorrespsValue.setObjectName("typeCorrespsValue")
        self.typeRotatSymLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeRotatSymLabel.setGeometry(QtCore.QRect(360, 405, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeRotatSymLabel.setFont(font)
        self.typeRotatSymLabel.setObjectName("typeRotatSymLabel")
        self.typeRotatSymX = QtWidgets.QCheckBox(self.typeFrame)
        self.typeRotatSymX.setGeometry(QtCore.QRect(480, 405, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeRotatSymX.setFont(font)
        self.typeRotatSymX.setObjectName("typeRotatSymX")
        self.typeRotatSymY = QtWidgets.QCheckBox(self.typeFrame)
        self.typeRotatSymY.setGeometry(QtCore.QRect(560, 405, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeRotatSymY.setFont(font)
        self.typeRotatSymY.setObjectName("typeRotatSymY")
        self.typeRotatSymZ = QtWidgets.QCheckBox(self.typeFrame)
        self.typeRotatSymZ.setGeometry(QtCore.QRect(640, 405, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeRotatSymZ.setFont(font)
        self.typeRotatSymZ.setObjectName("typeRotatSymZ")
        self.typeReflSymYZ = QtWidgets.QCheckBox(self.typeFrame)
        self.typeReflSymYZ.setGeometry(QtCore.QRect(640, 460, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReflSymYZ.setFont(font)
        self.typeReflSymYZ.setObjectName("typeReflSymYZ")
        self.typeReflSymLabel = QtWidgets.QLabel(self.typeFrame)
        self.typeReflSymLabel.setGeometry(QtCore.QRect(360, 460, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReflSymLabel.setFont(font)
        self.typeReflSymLabel.setObjectName("typeReflSymLabel")
        self.typeReflSymXZ = QtWidgets.QCheckBox(self.typeFrame)
        self.typeReflSymXZ.setGeometry(QtCore.QRect(560, 460, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReflSymXZ.setFont(font)
        self.typeReflSymXZ.setObjectName("typeReflSymXZ")
        self.typeReflSymXY = QtWidgets.QCheckBox(self.typeFrame)
        self.typeReflSymXY.setGeometry(QtCore.QRect(480, 460, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.typeReflSymXY.setFont(font)
        self.typeReflSymXY.setObjectName("typeReflSymXY")
        self.typeFrame.raise_()
        self.entityFrame.raise_()
        self.lexFrame.raise_()
        self.embodimentFrame.raise_()
        self.attributesFrame.raise_()
        self.affordStrFrame.raise_()
        self.habitatFrame.raise_()
        self.entityBtn.raise_()
        self.lexBtn.raise_()
        self.typeBtn.raise_()
        self.habitatBtn.raise_()
        self.attributesBtn.raise_()
        self.embodimentBtn.raise_()
        self.affordStrBtn.raise_()
        self.createVoxMLButton = QtWidgets.QPushButton(self.backgroundFrame)
        self.createVoxMLButton.setGeometry(QtCore.QRect(290, 120, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.createVoxMLButton.setFont(font)
        self.createVoxMLButton.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}")
        self.createVoxMLButton.setObjectName("createVoxMLButton")
        self.templateChooser = QtWidgets.QComboBox(self.backgroundFrame)
        self.templateChooser.setGeometry(QtCore.QRect(130, 120, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.templateChooser.setFont(font)
        self.templateChooser.setStyleSheet("QComboBox {\n"
"    border: 1px solid #f0f0f0;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #2b78d3;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.templateChooser.setProperty("placeholderText", "")
        self.templateChooser.setObjectName("templateChooser")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateChooser.addItem("")
        self.templateLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.templateLabel.setGeometry(QtCore.QRect(20, 120, 100, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.templateLabel.setFont(font)
        self.templateLabel.setStyleSheet("QLabel {\n"
"    background-color: None;\n"
"    color: #2b78d3;\n"
"    border: None;\n"
"}")
        self.templateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.templateLabel.setObjectName("templateLabel")
        self.saveVoxMLData = QtWidgets.QPushButton(self.backgroundFrame)
        self.saveVoxMLData.setGeometry(QtCore.QRect(670, 120, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.saveVoxMLData.setFont(font)
        self.saveVoxMLData.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #1fd78d;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #1fd78d;\n"
"}")
        self.saveVoxMLData.setObjectName("saveVoxMLData")
        self.popupText = QtWidgets.QLabel(self.backgroundFrame)
        self.popupText.setGeometry(QtCore.QRect(670, 20, 850, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.popupText.setFont(font)
        self.popupText.setStyleSheet("QLabel {\n"
"    border-radius: 20px;\n"
"    border: 3px solid #eb7b59;\n"
"    color: #eb7b59;\n"
"}")
        self.popupText.setAlignment(QtCore.Qt.AlignCenter)
        self.popupText.setObjectName("popupText")
        self.templateLabel_2 = QtWidgets.QLabel(self.backgroundFrame)
        self.templateLabel_2.setGeometry(QtCore.QRect(850, 120, 220, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.templateLabel_2.setFont(font)
        self.templateLabel_2.setStyleSheet("QLabel {\n"
"    background-color: None;\n"
"    color: #2b78d3;\n"
"    border: None;\n"
"}")
        self.templateLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.templateLabel_2.setObjectName("templateLabel_2")
        self.open3DObjectButton = QtWidgets.QPushButton(self.backgroundFrame)
        self.open3DObjectButton.setGeometry(QtCore.QRect(1250, 120, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.open3DObjectButton.setFont(font)
        self.open3DObjectButton.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}")
        self.open3DObjectButton.setObjectName("open3DObjectButton")
        self.openImageButton = QtWidgets.QPushButton(self.backgroundFrame)
        self.openImageButton.setGeometry(QtCore.QRect(1420, 120, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.openImageButton.setFont(font)
        self.openImageButton.setStyleSheet("QPushButton {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #161c21, stop: 1.0 #2d3943);\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f0f0;\n"
"    color: #2b78d3;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border: 2px solid #2b78d3;\n"
"}")
        self.openImageButton.setObjectName("openImageButton")
        self.chooseVoxMLObject = QtWidgets.QComboBox(self.backgroundFrame)
        self.chooseVoxMLObject.setGeometry(QtCore.QRect(500, 120, 160, 30))
        self.chooseVoxMLObject.setStyleSheet("QComboBox {\n"
"    border: 1px solid #f0f0f0;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid #1fd78d;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.chooseVoxMLObject.setObjectName("chooseVoxMLObject")
        self.imgObjFrame = QtWidgets.QFrame(self.backgroundFrame)
        self.imgObjFrame.setGeometry(QtCore.QRect(850, 170, 730, 600))
        self.imgObjFrame.setStyleSheet("QFrame {\n"
"    border-radius: 0px;\n"
"    border: 2px solid #f0f0f0;\n"
"}")
        self.imgObjFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imgObjFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgObjFrame.setObjectName("imgObjFrame")
        self.displayImageLabel = QtWidgets.QLabel(self.imgObjFrame)
        self.displayImageLabel.setGeometry(QtCore.QRect(0, 0, 730, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(50)
        self.displayImageLabel.setFont(font)
        self.displayImageLabel.setToolTip("")
        self.displayImageLabel.setStyleSheet("QLabel {\n"
"    border-radius: 0px;\n"
"    background-color: None;\n"
"    color: #f0f0f0;\n"
"    border: None;\n"
"}")
        self.displayImageLabel.setText("")
        self.displayImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayImageLabel.setObjectName("displayImageLabel")
        self.objLabel = QtWidgets.QLabel(self.backgroundFrame)
        self.objLabel.setGeometry(QtCore.QRect(435, 120, 60, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.objLabel.setFont(font)
        self.objLabel.setStyleSheet("QLabel {\n"
"    background-color: None;\n"
"    color: #2b78d3;\n"
"    border: None;\n"
"}")
        self.objLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.objLabel.setObjectName("objLabel")
        self.blockFrame = QtWidgets.QFrame(self.backgroundFrame)
        self.blockFrame.setGeometry(QtCore.QRect(850, 170, 730, 600))
        self.blockFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blockFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blockFrame.setObjectName("blockFrame")
        MainVoxMLWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainVoxMLWindow)
        self.typeComponents.setCurrentIndex(-1)
        self.typeArgs.setCurrentIndex(-1)
        self.typeBody.setCurrentIndex(-1)
        self.typeCorresps.setCurrentIndex(-1)
        self.templateChooser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainVoxMLWindow)

    def retranslateUi(self, MainVoxMLWindow):
        _translate = QtCore.QCoreApplication.translate
        MainVoxMLWindow.setWindowTitle(_translate("MainVoxMLWindow", "MainWindow"))
        self.exitButton.setToolTip(_translate("MainVoxMLWindow", "Exit the program."))
        self.titleLabel.setToolTip(_translate("MainVoxMLWindow", "That\'s just the title!"))
        self.titleLabel.setText(_translate("MainVoxMLWindow", "VoxML Annotator"))
        self.openVoxMLDataButton.setToolTip(_translate("MainVoxMLWindow", "Import VoxML Object from file"))
        self.openVoxMLDataButton.setText(_translate("MainVoxMLWindow", "VoxML Data"))
        self.entityBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Entity attributes"))
        self.entityBtn.setText(_translate("MainVoxMLWindow", "Entity"))
        self.lexBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Lex Attributes"))
        self.lexBtn.setText(_translate("MainVoxMLWindow", "Lex"))
        self.typeBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Type attributes"))
        self.typeBtn.setText(_translate("MainVoxMLWindow", "Type"))
        self.habitatBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Habitat attributes"))
        self.habitatBtn.setText(_translate("MainVoxMLWindow", "Habitat"))
        self.attributesBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Attributes attributes"))
        self.attributesBtn.setText(_translate("MainVoxMLWindow", "Attributes"))
        self.embodimentBtn.setToolTip(_translate("MainVoxMLWindow", "Edit Embodiment attributes"))
        self.embodimentBtn.setText(_translate("MainVoxMLWindow", "Embodiment"))
        self.affordStrBtn.setToolTip(_translate("MainVoxMLWindow", "Edit AffordStr attributes"))
        self.affordStrBtn.setText(_translate("MainVoxMLWindow", "AffordStr"))
        self.entityTypeLabel.setText(_translate("MainVoxMLWindow", "Type:"))
        self.entityType.setToolTip(_translate("MainVoxMLWindow", "Entity: Type"))
        self.lexTypeLabel.setText(_translate("MainVoxMLWindow", "Type:"))
        self.lexType.setToolTip(_translate("MainVoxMLWindow", "Lex: Type"))
        self.lexPredLabel.setText(_translate("MainVoxMLWindow", "Pred:"))
        self.lexPred.setToolTip(_translate("MainVoxMLWindow", "Lex: Pred"))
        self.movableLabel.setText(_translate("MainVoxMLWindow", "Movable:"))
        self.scaleLabel.setText(_translate("MainVoxMLWindow", "Scale:"))
        self.embodimentMovable.setToolTip(_translate("MainVoxMLWindow", "Embodiment: Movable"))
        self.embodimentScale.setToolTip(_translate("MainVoxMLWindow", "Embodiment: Scale"))
        self.attributesLabel.setText(_translate("MainVoxMLWindow", "Attrs:"))
        self.attrsDel0.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attributesAttrsAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.attributesAttrsNewItem.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.attrsDel1.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attrsDel2.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attrsDel3.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attrsDel4.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attrsDel6.setText(_translate("MainVoxMLWindow", "Delete"))
        self.attrsDel5.setText(_translate("MainVoxMLWindow", "Delete"))
        self.affordancesLabel.setText(_translate("MainVoxMLWindow", "<html><head/><body><p>Affordances:</p></body></html>"))
        self.afforDel0.setText(_translate("MainVoxMLWindow", "Delete"))
        self.affordStrAffordancesAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.affordStrAffordancesNewItem.setPlaceholderText(_translate("MainVoxMLWindow", "Formula"))
        self.afforDel1.setText(_translate("MainVoxMLWindow", "Delete"))
        self.afforDel3.setText(_translate("MainVoxMLWindow", "Delete"))
        self.afforDel2.setText(_translate("MainVoxMLWindow", "Delete"))
        self.afforDel5.setText(_translate("MainVoxMLWindow", "Delete"))
        self.afforDel4.setText(_translate("MainVoxMLWindow", "Delete"))
        self.afforDel6.setText(_translate("MainVoxMLWindow", "Delete"))
        self.intrinsicLabel.setText(_translate("MainVoxMLWindow", "<html><head/><body><p>Intrinsic:</p></body></html>"))
        self.intrDel0.setText(_translate("MainVoxMLWindow", "Delete"))
        self.habitatIntrinsicAdder.setText(_translate("MainVoxMLWindow", "Add"))
        self.habitatIntrName.setPlaceholderText(_translate("MainVoxMLWindow", "Name"))
        self.habitatIntrValue.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.extrinsicLabel.setText(_translate("MainVoxMLWindow", "Extrinsic:"))
        self.habitatExtrName.setPlaceholderText(_translate("MainVoxMLWindow", "Name"))
        self.habitatExtrValue.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.habitatExtrinsicAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.intrDel1.setText(_translate("MainVoxMLWindow", "Delete"))
        self.intrDel2.setText(_translate("MainVoxMLWindow", "Delete"))
        self.intrDel3.setText(_translate("MainVoxMLWindow", "Delete"))
        self.intrDel4.setText(_translate("MainVoxMLWindow", "Delete"))
        self.extrDel4.setText(_translate("MainVoxMLWindow", "Delete"))
        self.extrDel3.setText(_translate("MainVoxMLWindow", "Delete"))
        self.extrDel0.setText(_translate("MainVoxMLWindow", "Delete"))
        self.extrDel1.setText(_translate("MainVoxMLWindow", "Delete"))
        self.extrDel2.setText(_translate("MainVoxMLWindow", "Delete"))
        self.typeHeadLabel.setText(_translate("MainVoxMLWindow", "Head:"))
        self.typeHead.setToolTip(_translate("MainVoxMLWindow", "Type: Head"))
        self.typeConcavity.setToolTip(_translate("MainVoxMLWindow", "Type Concavity"))
        self.typeConcavityLabel.setText(_translate("MainVoxMLWindow", "Concavity:"))
        self.typeClass.setToolTip(_translate("MainVoxMLWindow", "Type: Class"))
        self.typeClassLabel.setText(_translate("MainVoxMLWindow", "Class:"))
        self.typeValue.setToolTip(_translate("MainVoxMLWindow", "Type: Value"))
        self.typeValueLabel.setText(_translate("MainVoxMLWindow", "Value:"))
        self.typeScale.setToolTip(_translate("MainVoxMLWindow", "Type: Scale"))
        self.typeReferentLabel.setText(_translate("MainVoxMLWindow", "Referent:"))
        self.typeConstr.setToolTip(_translate("MainVoxMLWindow", "Type: Constr"))
        self.typeArityLabel.setText(_translate("MainVoxMLWindow", "Arity:"))
        self.typeReferent.setToolTip(_translate("MainVoxMLWindow", "Type: Referent"))
        self.typeConstrLabel.setText(_translate("MainVoxMLWindow", "Constr:"))
        self.typeScaleLabel.setText(_translate("MainVoxMLWindow", "Scale:"))
        self.typeArity.setToolTip(_translate("MainVoxMLWindow", "Type: Arity"))
        self.typeMappingLabel.setText(_translate("MainVoxMLWindow", "Mapping:"))
        self.typeMapping.setToolTip(_translate("MainVoxMLWindow", "Type: Mapping"))
        self.typeComponentsLabel.setText(_translate("MainVoxMLWindow", "Components:"))
        self.typeComponentsValue.setToolTip(_translate("MainVoxMLWindow", "New Component Value"))
        self.typeComponentsValue.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.typeComponents.setToolTip(_translate("MainVoxMLWindow", "Type: Components"))
        self.typeComponentsAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.typeComponentsDelete.setText(_translate("MainVoxMLWindow", "Delete"))
        self.typeArgsLabel.setText(_translate("MainVoxMLWindow", "Args:"))
        self.typeArgsAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.typeArgs.setToolTip(_translate("MainVoxMLWindow", "Type: Args"))
        self.typeArgsDelete.setText(_translate("MainVoxMLWindow", "Delete"))
        self.typeArgsValue.setToolTip(_translate("MainVoxMLWindow", "New Arg Value"))
        self.typeArgsValue.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.typeBodyLabel.setText(_translate("MainVoxMLWindow", "Body:"))
        self.typeBodyAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.typeBody.setToolTip(_translate("MainVoxMLWindow", "Type: Body"))
        self.typeBodyDelete.setText(_translate("MainVoxMLWindow", "Delete"))
        self.typeBodySubeventValue.setToolTip(_translate("MainVoxMLWindow", "New Subevent Value"))
        self.typeBodySubeventValue.setPlaceholderText(_translate("MainVoxMLWindow", "Subevent: Value"))
        self.typeCorrespsLabel.setText(_translate("MainVoxMLWindow", "Corresps:"))
        self.typeCorrespsAdd.setText(_translate("MainVoxMLWindow", "Add"))
        self.typeCorresps.setToolTip(_translate("MainVoxMLWindow", "Type: Corresps"))
        self.typeCorrespsDelete.setText(_translate("MainVoxMLWindow", "Delete"))
        self.typeCorrespsValue.setToolTip(_translate("MainVoxMLWindow", "New Corresp Value"))
        self.typeCorrespsValue.setPlaceholderText(_translate("MainVoxMLWindow", "Value"))
        self.typeRotatSymLabel.setText(_translate("MainVoxMLWindow", "RotatSym:"))
        self.typeRotatSymX.setToolTip(_translate("MainVoxMLWindow", "Type: RotatSym"))
        self.typeRotatSymX.setText(_translate("MainVoxMLWindow", "X"))
        self.typeRotatSymY.setToolTip(_translate("MainVoxMLWindow", "Type: RotatSym"))
        self.typeRotatSymY.setText(_translate("MainVoxMLWindow", "Y"))
        self.typeRotatSymZ.setToolTip(_translate("MainVoxMLWindow", "Type: RotatSym"))
        self.typeRotatSymZ.setText(_translate("MainVoxMLWindow", "Z"))
        self.typeReflSymYZ.setToolTip(_translate("MainVoxMLWindow", "Type: ReflSym"))
        self.typeReflSymYZ.setText(_translate("MainVoxMLWindow", "YZ"))
        self.typeReflSymLabel.setText(_translate("MainVoxMLWindow", "ReflSym:"))
        self.typeReflSymXZ.setToolTip(_translate("MainVoxMLWindow", "Type: ReflSym"))
        self.typeReflSymXZ.setText(_translate("MainVoxMLWindow", "XZ"))
        self.typeReflSymXY.setToolTip(_translate("MainVoxMLWindow", "Type: ReflSym"))
        self.typeReflSymXY.setText(_translate("MainVoxMLWindow", "XY"))
        self.createVoxMLButton.setToolTip(_translate("MainVoxMLWindow", "Create VoxML Data based on template"))
        self.createVoxMLButton.setText(_translate("MainVoxMLWindow", "Create VoxMLData"))
        self.templateChooser.setToolTip(_translate("MainVoxMLWindow", "Choose a Template for your VoxML Object."))
        self.templateChooser.setCurrentText(_translate("MainVoxMLWindow", "Empty"))
        self.templateChooser.setItemText(0, _translate("MainVoxMLWindow", "Empty"))
        self.templateChooser.setItemText(1, _translate("MainVoxMLWindow", "Attribute"))
        self.templateChooser.setItemText(2, _translate("MainVoxMLWindow", "Function"))
        self.templateChooser.setItemText(3, _translate("MainVoxMLWindow", "Object"))
        self.templateChooser.setItemText(4, _translate("MainVoxMLWindow", "Program"))
        self.templateChooser.setItemText(5, _translate("MainVoxMLWindow", "Relation"))
        self.templateLabel.setToolTip(_translate("MainVoxMLWindow", "Not here. To the right!"))
        self.templateLabel.setText(_translate("MainVoxMLWindow", "Template:"))
        self.saveVoxMLData.setToolTip(_translate("MainVoxMLWindow", "Save your VoxMLObject to a file. (Press -Save- beforehand)."))
        self.saveVoxMLData.setText(_translate("MainVoxMLWindow", "Save To File"))
        self.popupText.setText(_translate("MainVoxMLWindow", "PopUP Window"))
        self.templateLabel_2.setToolTip(_translate("MainVoxMLWindow", "Not here. To the right!"))
        self.templateLabel_2.setText(_translate("MainVoxMLWindow", "Open VoxML Data from:"))
        self.open3DObjectButton.setToolTip(_translate("MainVoxMLWindow", "Import 3D Object from file"))
        self.open3DObjectButton.setText(_translate("MainVoxMLWindow", "3D Object"))
        self.openImageButton.setToolTip(_translate("MainVoxMLWindow", "Import Image from file"))
        self.openImageButton.setText(_translate("MainVoxMLWindow", "Image"))
        self.imgObjFrame.setToolTip(_translate("MainVoxMLWindow", "Display images and 3D-objects"))
        self.objLabel.setToolTip(_translate("MainVoxMLWindow", "Not here. To the right!"))
        self.objLabel.setText(_translate("MainVoxMLWindow", "Obj:"))
