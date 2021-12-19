# Basic imports
import sys
import xml.etree.ElementTree as ET

# PyQt5 imports
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QLineEdit, QMainWindow, QPushButton

# Scenes imports
from Scenes.Scripts.MainVoxMLWindow import Ui_MainVoxMLWindow

# VoxML imports
from VoxML.VoxMLClasses import *
from VoxML.DataLoader import VoxMLDataLoader

# Main Window class
class MainVoxMLWindow(QMainWindow):
### general
    def __init__(self) -> None:
        # Create and setup window
        QMainWindow.__init__(self)
        self.ui = Ui_MainVoxMLWindow()
        self.ui.setupUi(self)

        # Vars
        self.objIndex = -1
        self.allObj = []
        self.loader = VoxMLDataLoader()

        # Remove everything outside of backgroundFrame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # main button logic
        self.ui.openVoxMLDataButton.clicked.connect(lambda: self.addObjectFromFile(self.chooseVoxMLDataFile(), "vox"))
        self.ui.open3DObjectButton.clicked.connect(lambda: self.addObjectFromFile(self.choose3DObjectFile(), "obj"))
        self.ui.openImageButton.clicked.connect(lambda: self.addObjectFromFile(self.chooseImageFile(), "img"))
        self.ui.exitButton.clicked.connect(lambda: sys.exit())
        self.ui.createVoxMLButton.clicked.connect(lambda: self.createNewVoxMLObject(str(self.ui.templateChooser.currentText())))
        self.ui.saveVoxMLData.clicked.connect(lambda: self.saveDataToFile())

        # editing logic
        self.ui.entityBtn.clicked.connect(lambda: self.switchEditingFrame("entity"))
        self.ui.lexBtn.clicked.connect(lambda: self.switchEditingFrame("lex"))
        self.ui.typeBtn.clicked.connect(lambda: self.switchEditingFrame("type"))
        self.ui.habitatBtn.clicked.connect(lambda: self.switchEditingFrame("habitat"))
        self.ui.affordStrBtn.clicked.connect(lambda: self.switchEditingFrame("affordStr"))
        self.ui.embodimentBtn.clicked.connect(lambda: self.switchEditingFrame("embodiment"))
        self.ui.attributesBtn.clicked.connect(lambda: self.switchEditingFrame("attributes"))
        self.disableEditingMode()

        # editing :: comboboxes
        self.ui.typeComponentsAdd.clicked.connect(lambda: self.addToBox("components"))
        self.ui.typeComponentsDelete.clicked.connect(lambda: self.deleteFromBox("components"))
        self.ui.typeArgsAdd.clicked.connect(lambda: self.addToBox("args"))
        self.ui.typeArgsDelete.clicked.connect(lambda: self.deleteFromBox("args"))
        self.ui.typeBodyAdd.clicked.connect(lambda: self.addToBox("body"))
        self.ui.typeBodyDelete.clicked.connect(lambda: self.deleteFromBox("body"))
        self.ui.typeCorrespsAdd.clicked.connect(lambda: self.addToBox("corresps"))
        self.ui.typeCorrespsDelete.clicked.connect(lambda: self.deleteFromBox("corresps"))

        self.ui.habitatIntrinsicAdder.clicked.connect(lambda: self.addToBox("intrinsic"))
        self.ui.habitatIntrinsicDelete.clicked.connect(lambda: self.deleteFromBox("intrinsic"))
        self.ui.habitatExtrinsicAdd.clicked.connect(lambda: self.addToBox("extrinsic"))
        self.ui.habitatExtrinsicDelete.clicked.connect(lambda: self.deleteFromBox("extrinsic"))

        self.ui.affordStrAffordancesAdd.clicked.connect(lambda: self.addToBox("affordances"))
        self.ui.afforValues = [self.ui.afforVal0,self.ui.afforVal1,self.ui.afforVal2,self.ui.afforVal3,self.ui.afforVal4,self.ui.afforVal5,self.ui.afforVal6]
        self.ui.afforDelete = [self.ui.afforDel0,self.ui.afforDel1,self.ui.afforDel2,self.ui.afforDel3,self.ui.afforDel4,self.ui.afforDel5,self.ui.afforDel6]
        self.ui.afforDel0.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(0), self.updateListVisualisations()))
        self.ui.afforDel1.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(1), self.updateListVisualisations()))
        self.ui.afforDel2.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(2), self.updateListVisualisations()))
        self.ui.afforDel3.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(3), self.updateListVisualisations()))
        self.ui.afforDel4.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(4), self.updateListVisualisations()))
        self.ui.afforDel5.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(5), self.updateListVisualisations()))
        self.ui.afforDel6.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].AffordStr.Affordances.pop(6), self.updateListVisualisations()))

        self.ui.attributesAttrsAdd.clicked.connect(lambda: self.addToBox("attrs"))
        self.ui.attrsValues = [self.ui.attrsVal0,self.ui.attrsVal1,self.ui.attrsVal2,self.ui.attrsVal3,self.ui.attrsVal4,self.ui.attrsVal5,self.ui.attrsVal6]
        self.ui.attrsDelete = [self.ui.attrsDel0,self.ui.attrsDel1,self.ui.attrsDel2,self.ui.attrsDel3,self.ui.attrsDel4,self.ui.attrsDel5,self.ui.attrsDel6]
        self.ui.attrsDel0.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(0), self.updateListVisualisations()))
        self.ui.attrsDel1.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(1), self.updateListVisualisations()))
        self.ui.attrsDel2.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(2), self.updateListVisualisations()))
        self.ui.attrsDel3.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(3), self.updateListVisualisations()))
        self.ui.attrsDel4.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(4), self.updateListVisualisations()))
        self.ui.attrsDel5.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(5), self.updateListVisualisations()))
        self.ui.attrsDel6.clicked.connect(lambda: self.doNothing(self.allObj[self.objIndex].Attributes.Attrs.pop(6), self.updateListVisualisations()))

        # setup position and show window
        self.oldPos = self.pos()
        self.ui.popupText.hide()
        self.show()

    # show popup message for x seconds
    def showPopupMessage(self, msg: str, x: float):
        self.ui.popupText.setText(msg)
        self.ui.popupText.show()
        QtCore.QTimer.singleShot(int(x * 1000), lambda: self.ui.popupText.hide())

### window drag-and-drop 

    # called when mouse is pressed on window -> save current window position
    def mousePressEvent(self, event) -> None:
        self.oldPos = event.globalPos()
    
    # called when mouse is pressed and moved -> drag and move window
    def mouseMoveEvent(self, event) -> None:
        if not True in [x.underMouse() for x in [self.ui.editingFrame,self.ui.exitButton,self.ui.openVoxMLDataButton,self.ui.saveVoxMLData,self.ui.templateChooser,self.ui.createVoxMLButton]]:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        

### editor methods

    # add item to ComboBox
    def addToBox(self, attr):
        if attr == "components":
            self.ui.typeComponents.addItem(str(self.ui.typeComponentsValue.text()))
            self.ui.typeComponentsValue.setText("")
        elif attr == "args":
            self.ui.typeArgs.addItem(str(self.ui.typeArgsValue.text()))
            self.ui.typeArgsValue.setText("")
        elif attr == "body":
            self.ui.typeBody.addItem(str(self.ui.typeBodySubeventValue.text()))
            self.ui.typeBodySubeventValue.setText("")
        elif attr == "corresps":
            self.ui.typeCorresps.addItem(str(self.ui.typeCorrespsValue.text()))
            self.ui.typeCorrespsValue.setText("")
        elif attr == "intrinsic":
            self.ui.habitatIntrinsic.addItem("Name:" + str(self.ui.habitatIntrName.text()) + ",Value:" + str(self.ui.habitatIntrValue.text()))
            self.ui.habitatIntrName.setText("")
            self.ui.habitatIntrValue.setText("")
        elif attr == "extrinsic":
            self.ui.habitatExtrinsic.addItem("Name:" + str(self.ui.habitatExtrName.text()) + ",Value:" + str(self.ui.habitatExtrValue.text()))
            self.ui.habitatExtrName.setText("")
            self.ui.habitatExtrValue.setText("")
        elif attr == "affordances" and len(str(self.ui.affordStrAffordancesNewItem.text())) > 0:
            affor = vAffordance()
            affor.Formula = str(self.ui.affordStrAffordancesNewItem.text())
            self.allObj[self.objIndex].AffordStr.Affordances.append(affor)
            self.ui.affordStrAffordancesNewItem.setText("")
        elif attr == "attrs" and len(str(self.ui.attributesAttrsNewItem.text())) > 0:
            attr = vAttr()
            attr.Value = str(self.ui.attributesAttrsNewItem.text())
            self.allObj[self.objIndex].Attributes.Attrs.append(attr)
            self.ui.attributesAttrsNewItem.setText("")
        
        self.updateListVisualisations()

    # remove item from ComboBox
    def deleteFromBox(self,attr):
        if attr == "components":
            self.ui.typeComponents.removeItem(self.ui.typeComponents.currentIndex())
        elif attr == "args":
            self.ui.typeArgs.removeItem(self.ui.typeArgs.currentIndex())
        elif attr == "body":
            self.ui.typeBody.removeItem(self.ui.typeBody.currentIndex())
        elif attr == "corresps":
            self.ui.typeCorresps.removeItem(self.ui.typeCorresps.currentIndex())
        elif attr == "intrinsic":
            self.ui.habitatIntrinsic.removeItem(self.ui.habitatIntrinsic.currentIndex())
        elif attr == "extrinsic":
            self.ui.habitatExtrinsic.removeItem(self.ui.habitatExtrinsic.currentIndex())

    # disable all editing related features
    def disableEditingMode(self):
        # disable all buttons
        self.ui.entityBtn.setEnabled(False)
        self.ui.lexBtn.setEnabled(False)
        self.ui.typeBtn.setEnabled(False)
        self.ui.habitatBtn.setEnabled(False)
        self.ui.affordStrBtn.setEnabled(False)
        self.ui.embodimentBtn.setEnabled(False)
        self.ui.attributesBtn.setEnabled(False)

        # hide all frames
        self.ui.entityFrame.hide()
        self.ui.lexFrame.hide()
        self.ui.typeFrame.hide()
        self.ui.habitatFrame.hide()
        self.ui.affordStrFrame.hide()
        self.ui.embodimentFrame.hide()
        self.ui.attributesFrame.hide()

    # switches between frames for editing: entity,lex,type,habitat,affordstr,embodiment,attributes
    def switchEditingFrame(self, chosenPart):
        # enable all buttons
        self.ui.entityBtn.setEnabled(True)
        self.ui.lexBtn.setEnabled(True)
        self.ui.typeBtn.setEnabled(True)
        self.ui.habitatBtn.setEnabled(True)
        self.ui.affordStrBtn.setEnabled(True)
        self.ui.embodimentBtn.setEnabled(True)
        self.ui.attributesBtn.setEnabled(True)

        # hide all frames
        self.ui.entityFrame.hide()
        self.ui.lexFrame.hide()
        self.ui.typeFrame.hide()
        self.ui.habitatFrame.hide()
        self.ui.affordStrFrame.hide()
        self.ui.embodimentFrame.hide()
        self.ui.attributesFrame.hide()

        # show chosen frame and button
        if chosenPart == "entity":
            self.ui.entityBtn.setEnabled(False)
            self.ui.entityFrame.show()
        elif chosenPart == "lex":
            self.ui.lexBtn.setEnabled(False)
            self.ui.lexFrame.show()
        elif chosenPart == "type":
            self.ui.typeBtn.setEnabled(False)
            self.ui.typeFrame.show()
        elif chosenPart == "habitat":
            self.ui.habitatBtn.setEnabled(False)
            self.ui.habitatFrame.show()
        elif chosenPart == "affordStr":
            self.ui.affordStrBtn.setEnabled(False)
            self.ui.affordStrFrame.show()
        elif chosenPart == "embodiment":
            self.ui.embodimentBtn.setEnabled(False)
            self.ui.embodimentFrame.show()
        elif chosenPart == "attributes":
            self.ui.attributesBtn.setEnabled(False)
            self.ui.attributesFrame.show()
        
        self.updateListVisualisations()

    # hide all attributes -> used when loading new object
    def hideAllAttributes(self):
        for x in self.ui.entityFrame.children():
            x.hide()
        for x in self.ui.lexFrame.children():
            x.hide()
        for x in self.ui.typeFrame.children():
            x.hide()
        for x in self.ui.habitatFrame.children():
            x.hide()
        for x in self.ui.affordStrFrame.children():
            x.hide()
        for x in self.ui.embodimentFrame.children():
            x.hide()
        for x in self.ui.attributesFrame.children():
            x.hide()

    # show all attributes -> used when loading new object
    def showAllAttributes(self):
        for x in self.ui.entityFrame.children():
            x.show()
        for x in self.ui.lexFrame.children():
            x.show()
        for x in self.ui.typeFrame.children():
            x.show()
        for x in self.ui.habitatFrame.children():
            x.show()
        for x in self.ui.affordStrFrame.children():
            x.show()
        for x in self.ui.embodimentFrame.children():
            x.show()
        for x in self.ui.attributesFrame.children():
            x.show()

    # update text and checkboxes for VoxMLObject
    def loadDataToEditing(self):
        vox = self.allObj[self.objIndex]
        
        # Entity
        if vox.Entity.Type != None:
            self.ui.entityType.setText(str(vox.Entity.Type))
        
        # Lex
        if vox.Lex.Pred != None:
            self.ui.lexPred.setText(str(vox.Lex.Pred))
        if vox.Lex.Type != None:
            self.ui.lexType.setText(str(vox.Lex.Type)) 

        # Type
        if vox.Type.Head != None:
            self.ui.typeHead.setText(str(vox.Type.Head)) 
        self.ui.typeComponents.clear()
        for x in vox.Type.Components:
            self.ui.typeComponents.addItem(str(x.Value))
        if vox.Type.Concavity != None:
            self.ui.typeConcavity.setText(str(vox.Type.Concavity))
        if vox.Type.RotatSym != None:
            self.ui.typeRotatSymX.setChecked("X" in vox.Type.RotatSym)
            self.ui.typeRotatSymY.setChecked("Y" in vox.Type.RotatSym)
            self.ui.typeRotatSymZ.setChecked("Z" in vox.Type.RotatSym)
        else:
            self.ui.typeRotatSymX.setChecked(False)
            self.ui.typeRotatSymY.setChecked(False)
            self.ui.typeRotatSymZ.setChecked(False)
        if vox.Type.ReflSym != None:
            self.ui.typeReflSymXY.setChecked("XY" in vox.Type.ReflSym)
            self.ui.typeReflSymXZ.setChecked("XZ" in vox.Type.ReflSym)
            self.ui.typeReflSymYZ.setChecked("YZ" in vox.Type.ReflSym)
        else:
            self.ui.typeReflSymXY.setChecked(False)
            self.ui.typeReflSymXZ.setChecked(False)
            self.ui.typeReflSymYZ.setChecked(False)
        self.ui.typeArgs.clear()
        for x in vox.Type.Args:
            self.ui.typeArgs.addItem(str(x.Value))
        self.ui.typeBody.clear()
        for x in vox.Type.Body:
            self.ui.typeBody.addItem(str(x.Value))
        if vox.Type.Class != None:
            self.ui.typeClass.setText(str(vox.Type.Class))
        if vox.Type.Value != None:
            self.ui.typeValue.setText(str(vox.Type.Value)) 
        if vox.Type.Constr != None:
            self.ui.typeConstr.setText(str(vox.Type.Constr))
        if vox.Type.Scale != None:
            self.ui.typeScale.setText(str(vox.Type.Scale))
        if vox.Type.Arity != None:
            self.ui.typeArity.setText(str(vox.Type.Arity))
        if vox.Type.Referent != None:
            self.ui.typeReferent.setText(str(vox.Type.Referent))
        if vox.Type.Mapping != None:
            self.ui.typeMapping.setText(str(vox.Type.Mapping))
        self.ui.typeCorresps.clear()
        for x in vox.Type.Corresps:
            self.ui.typeCorresps.addItem(str(x.Value))
        
        # Habitat
        self.ui.habitatIntrinsic.clear()
        for x in vox.Habitat.Intrinsic:
            self.ui.habitatIntrinsic.addItem("Name:" + str(x.Name) + ",Value:" + str(x.Value))
        self.ui.habitatExtrinsic.clear()
        for x in vox.Habitat.Extrinsic:
            self.ui.habitatExtrinsic.addItem("Name:" + str(x.Name) + ",Value:" + str(x.Value))
        
        # Embodiment
        if vox.Embodiment.Scale != None:
            self.ui.embodimentScale.setText(str(vox.Embodiment.Scale))
        if vox.Embodiment.Movable:
            self.ui.embodimentMovable.setChecked(True)
        else:
            self.ui.embodimentMovable.setChecked(False)
        
        self.updateListVisualisations()

    # show specific editing attributes for specific template
    def createNewVoxMLObject(self, template, create = True):
        if create:
            self.allObj[self.objIndex] = VoxMLObject()
        self.hideAllAttributes()
        self.switchEditingFrame("entity")
        if template == "Empty":
            self.showAllAttributes()
        elif template == "Object":
            # Entity
            for x in self.ui.entityFrame.children():
                x.show()
            self.ui.entityType.setText("Object")
            # Lex
            for x in self.ui.lexFrame.children():
                x.show()
            # Type
            self.ui.typeHeadLabel.show()
            self.ui.typeHead.show()
            self.ui.typeConcavityLabel.show()
            self.ui.typeConcavity.show()
            self.ui.typeRotatSymLabel.show()
            self.ui.typeRotatSymX.show()
            self.ui.typeRotatSymY.show()
            self.ui.typeRotatSymZ.show()
            self.ui.typeReflSymLabel.show()
            self.ui.typeReflSymXY.show()
            self.ui.typeReflSymXZ.show()
            self.ui.typeReflSymYZ.show()
            self.ui.typeComponentsLabel.show()
            self.ui.typeComponents.show()
            self.ui.typeComponentsValue.show()
            self.ui.typeComponentsAdd.show()
            self.ui.typeComponentsDelete.show()
            # Habitat
            for x in self.ui.habitatFrame.children():
                x.show()
            # AffordStr
            for x in self.ui.affordStrFrame.children():
                x.show()
            # Embodiment
            for x in self.ui.embodimentFrame.children():
                x.show()
        elif template == "Program":
            # Entity
            for x in self.ui.entityFrame.children():
                x.show()
            self.ui.entityType.setText("Program")
            # Lex
            for x in self.ui.lexFrame.children():
                x.show()
            # Type
            self.ui.typeHeadLabel.show()
            self.ui.typeHead.show()
            self.ui.typeArgsLabel.show()
            self.ui.typeArgs.show()
            self.ui.typeArgsAdd.show()
            self.ui.typeArgsValue.show()
            self.ui.typeArgsDelete.show()
            self.ui.typeBodyLabel.show()
            self.ui.typeBody.show()
            self.ui.typeBodySubeventValue.show()
            self.ui.typeBodyAdd.show()
            self.ui.typeBodyDelete.show()
        elif template == "Attribute":
            # Entity
            for x in self.ui.entityFrame.children():
                x.show()
            self.ui.entityType.setText("Attribute")
            # Lex
            self.ui.lexPredLabel.show()
            self.ui.lexPred.show()
            # Type
            self.ui.typeScaleLabel.show()
            self.ui.typeScale.show()
            self.ui.typeArgsLabel.show()
            self.ui.typeArgs.show()
            self.ui.typeArgsAdd.show()
            self.ui.typeArgsValue.show()
            self.ui.typeArgsDelete.show()
            self.ui.typeArityLabel.show()
            self.ui.typeArity.show()
        elif template == "Relation":
            # Entity
            for x in self.ui.entityFrame.children():
                x.show()
            self.ui.entityType.setText("Relation")
            # Lex
            self.ui.lexPredLabel.show()
            self.ui.lexPred.show()
            # Type
            self.ui.typeClassLabel.show()
            self.ui.typeClass.show()
            self.ui.typeArgsLabel.show()
            self.ui.typeArgs.show()
            self.ui.typeArgsAdd.show()
            self.ui.typeArgsValue.show()
            self.ui.typeArgsDelete.show()
            self.ui.typeValueLabel.show()
            self.ui.typeValue.show()
            self.ui.typeCorrespsLabel.show()
            self.ui.typeCorresps.show()
            self.ui.typeCorrespsAdd.show()
            self.ui.typeCorrespsValue.show()
            self.ui.typeCorrespsDelete.show()
            self.ui.typeConstrLabel.show()
            self.ui.typeConstr.show()
        elif template == "Function":
            # Entity
            for x in self.ui.entityFrame.children():
                x.show()
            self.ui.entityType.setText("Function")
            # Lex
            self.ui.lexPredLabel.show()
            self.ui.lexPred.show()
            # Type
            self.ui.typeReferentLabel.show()
            self.ui.typeReferent.show()
            self.ui.typeArgsLabel.show()
            self.ui.typeArgs.show()
            self.ui.typeArgsAdd.show()
            self.ui.typeArgsValue.show()
            self.ui.typeArgsDelete.show()
            self.ui.typeMappingLabel.show()
            self.ui.typeMapping.show()

        self.saveDataToObject(showPopup = False)

    # Currently handling the display of Affordances/Attrs values (max 7)
    def updateListVisualisations(self):
        # AffordStr: Affordances
        for k in range(7):
            if k < len(self.allObj[self.objIndex].AffordStr.Affordances):
                self.ui.afforValues[k].setText(str(self.allObj[self.objIndex].AffordStr.Affordances[k].Formula))
                self.ui.afforValues[k].show()
                self.ui.afforDelete[k].show()
            else:
                self.ui.afforValues[k].setText("")
                self.ui.afforValues[k].hide()
                self.ui.afforDelete[k].hide()

        # Attributes: Attrs
        for k in range(7):
            if k < len(self.allObj[self.objIndex].Attributes.Attrs):
                self.ui.attrsValues[k].setText(str(self.allObj[self.objIndex].Attributes.Attrs[k].Value))
                self.ui.attrsValues[k].show()
                self.ui.attrsDelete[k].show()
            else:
                self.ui.attrsValues[k].setText("")
                self.ui.attrsValues[k].hide()
                self.ui.attrsDelete[k].hide()


### VoxMLData related functions

    # saves pbject parsed from file to self.allObj[self.objIndex]
    def addObjectFromFile(self, inpath: str, type: str) -> None:
        if inpath != None and len(inpath) > 0:
            if type == "vox":
                obj = self.loader.loadFileToObject(inpath)
            elif type == "obj":
                obj = self.loader.load3Dobj(inpath)
            elif type == "img":
                obj = self.loader.loadImage(inpath)
            if obj == None:
                self.showPopupMessage("Couldnt load/find file!", 1.5)
                return
            self.allObj.append(obj)
            self.objIndex += 1
            self.loadDataToEditing()
            self.createNewVoxMLObject(str(self.allObj[self.objIndex].Entity.Type), False)
            self.showPopupMessage("Data loaded from file!", 1.5)

    # Choose .txt or .xml file containing VoxML data from system
    def chooseVoxMLDataFile(self) -> str:
        return QFileDialog.getOpenFileName(self, "Choose file", "voml-framework\\VoxMLData", "VoxML Data (*.txt *.xml)")[0]

    # Choose .obj or .stl or .off file containing 3D object data from system
    def choose3DObjectFile(self) -> str:
        return QFileDialog.getOpenFileName(self, "Choose file", "voml-framework\\VoxMLData", "VoxML Data (*.obj *.stl *.off)")[0]

    # Choose .jpg or .png file containing Image from system
    def chooseImageFile(self) -> str:
        return QFileDialog.getOpenFileName(self, "Choose file", "voml-framework\\VoxMLData", "VoxML Data (*.jpg *.png)")[0]

    # save xml data to file with QFileDialog -> use together with createXMLStringFromVoxMLObject
    def saveDataToFile(self):
        fileName = QFileDialog.getSaveFileName(self, "Save File", "voml-framework\\VoxMLData", "VoxML Data (*.xml *.txt )")[0]
        if len(fileName) > 0:
            self.saveDataToObject(False)
            output = self.loader.loadObjectToXML(self.allObj[self.objIndex])
            with open(fileName, "w") as f:
                f.write(output.decode("utf-8"))
            self.showPopupMessage("Data saved to file!", 1.5)
        
    # save current input data to last VoxML Object
    def saveDataToObject(self, showPopup: bool = True):
        if self.allObj[self.objIndex] == None:
            return
        vox = VoxMLObject()

        # Entity
        if len(str(self.ui.entityType.text())) > 0:
            vox.Entity.Type = str(self.ui.entityType.text()) 
        
        # Lex
        if len(str(self.ui.lexPred.text())) > 0:
            vox.Lex.Pred = str(self.ui.lexPred.text()) 
        if len(str(self.ui.lexType.text())) > 0:
            vox.Lex.Type = str(self.ui.lexType.text()) 

        # Type
        if len(str(self.ui.typeHead.text())) > 0:
            vox.Type.Head = str(self.ui.typeHead.text()) 
        vox.Type.Components = []
        for x in range(self.ui.typeComponents.count()):
            comp = vComponent()
            comp.Value = str(self.ui.typeComponents.itemText(x))
            vox.Type.Components.append(comp)
        if len(str(self.ui.typeConcavity.text())) > 0:
            vox.Type.Concavity = str(self.ui.typeConcavity.text())
        if self.ui.typeRotatSymX.isChecked() or self.ui.typeRotatSymY.isChecked() or self.ui.typeRotatSymZ.isChecked():
            rotatSym = []
            if self.ui.typeRotatSymX.isChecked():
                rotatSym.append("X")
            if self.ui.typeRotatSymY.isChecked():
                rotatSym.append("Y")
            if self.ui.typeRotatSymZ.isChecked():
                rotatSym.append("Z")
            vox.Type.RotatSym = ",".join(rotatSym)
        else:
            vox.Type.RotatSym = None
        if self.ui.typeReflSymXY.isChecked() or self.ui.typeReflSymXZ.isChecked() or self.ui.typeReflSymYZ.isChecked():
            reflSym = []
            if self.ui.typeReflSymXY.isChecked():
                reflSym.append("XY")
            if self.ui.typeReflSymXZ.isChecked():
                reflSym.append("XZ")
            if self.ui.typeReflSymYZ.isChecked():
                reflSym.append("YZ")
            vox.Type.ReflSym = ",".join(reflSym)
        else:
            vox.Type.ReflSym = None
        vox.Type.Args = []
        for x in range(self.ui.typeArgs.count()):
            arg = vArg()
            arg.Value = str(self.ui.typeArgs.itemText(x))
            vox.Type.Args.append(arg)
        vox.Type.Body = []
        for x in range(self.ui.typeBody.count()):
            subevent = vSubevent()
            subevent.Value = str(self.ui.typeBody.itemText(x))
            vox.Type.Body.append(subevent)
        if len(str(self.ui.typeClass.text())) > 0:
            vox.Type.Class = str(self.ui.typeClass.text()) 
        if len(str(self.ui.typeValue.text())) > 0:
            vox.Type.Value = str(self.ui.typeValue.text()) 
        if len(str(self.ui.typeConstr.text())) > 0:
            vox.Type.Constr = str(self.ui.typeConstr.text()) 
        if len(str(self.ui.typeScale.text())) > 0:
            vox.Type.Scale = str(self.ui.typeScale.text()) 
        if len(str(self.ui.typeArity.text())) > 0:
            vox.Type.Arity = str(self.ui.typeArity.text()) 
        if len(str(self.ui.typeReferent.text())) > 0:
            vox.Type.Referent = str(self.ui.typeReferent.text()) 
        if len(str(self.ui.typeMapping.text())) > 0:
            vox.Type.Mapping = str(self.ui.typeMapping.text()) 
        vox.Type.Corresps = []
        for x in range(self.ui.typeCorresps.count()):
            corr = vCorresp()
            corr.Value = str(self.ui.typeCorresps.itemText(x))
            vox.Type.Corresps.append(corr)
        
        # Habitat
        vox.Habitat.Intrinsic = []
        for x in range(self.ui.habitatIntrinsic.count()):
            intr = vIntr()
            content = str(self.ui.habitatIntrinsic.itemText(x))
            intr.Name = content.split(",Value:")[0].replace("Name:","")
            intr.Value = content.split(",Value:")[1]
            vox.Habitat.Intrinsic.append(intr)
        vox.Habitat.Extrinsic = []
        for x in range(self.ui.habitatExtrinsic.count()):
            extr = vExtr()
            content = str(self.ui.habitatExtrinsic.itemText(x))
            extr.Name = content.split(",Value:")[0].replace("Name:","")
            extr.Value = content.split(",Value:")[1]
            vox.Habitat.Extrinsic.append(extr)

        # AffordStr
        for x in range(len(self.allObj[self.objIndex].AffordStr.Affordances)):
            aff = vAffordance()
            aff.Formula = str(self.ui.afforValues[x].text())
            vox.AffordStr.Affordances.append(aff)
        
        # Embodiment
        if len(str(self.ui.embodimentScale.text())) > 0:
            vox.Embodiment.Scale = str(self.ui.embodimentScale.text()) 
        if self.ui.embodimentMovable.isChecked():
            vox.Embodiment.Movable = True;
        elif self.ui.embodimentMovable.isVisible():
            vox.Embodiment.Movable = False
        else:
            vox.Embodiment.Movable = None
        
        # Attributes
        for x in range(len(self.allObj[self.objIndex].Attributes.Attrs)):
            attr = vAttr()
            attr.Value = str(self.ui.attrsValues[x].text())
            vox.Attributes.Attrs.append(aff)

        self.allObj[self.objIndex] = vox
        self.loadDataToEditing()

        if showPopup:
            self.showPopupMessage("Data saved to object!", 1.5)

    # Print last added/parsed VoxMLObject to console :: only for testing purposes / will be removed later
    def printLastVoxMLObject(self):
        if self.allObj[self.objIndex] == None:
            return
        vox = self.allObj[self.objIndex]
        print("Showing parsed data of " + str(vox.filepath) + "\n")
        if vox.Entity.Type != None:
            print("Entity:\n\tType: " + str(vox.Entity.Type))
        if vox.Lex.Pred != None or vox.Lex.Type != None:
            print("Lex:")
            if vox.Lex.Pred != None:
                print("\tPred: " + str(vox.Lex.Pred))
            if vox.Lex.Type != None:
                print("\tType: " + str(vox.Lex.Type))
        if True in [x != None for x in [vox.Type.Head,vox.Type.Concavity,vox.Type.RotatSym,vox.Type.ReflSym,vox.Type.Class,vox.Type.Value,vox.Type.Constr,vox.Type.Scale,vox.Type.Arity,vox.Type.Referent,vox.Type.Mapping]] or True in [len(x) > 0 for x in [vox.Type.Components,vox.Type.Args,vox.Type.Body,vox.Type.Corresps]]:
            print("Type:")
            if vox.Type.Head != None:
                print("\tHead: " + str(vox.Type.Head))
            if len(vox.Type.Components) > 0:
                print("\tComponents:")
                for x in vox.Type.Components:
                    print("\t\tComponent: Value: " + str(x.Value))
            if vox.Type.Concavity != None:
                print("\tConcavity: " + str(vox.Type.Concavity))
            if vox.Type.RotatSym != None:
                print("\tRotatSym: " + str(vox.Type.RotatSym))
            if vox.Type.ReflSym != None:
                print("\tReflSym: " + str(vox.Type.ReflSym))
            if len(vox.Type.Args) > 0:
                print("\tArgs:")
                for x in vox.Type.Args:
                    print("\t\tArg: Value: " + str(x.Value))
            if len(vox.Type.Body) > 0:
                print("\tBody:")
                for x in vox.Type.Body:
                    print("\t\tSubevent: Value: " + str(x.Value))
            if vox.Type.Class != None:
                print("\tClass: " + str(vox.Type.Class))
            if vox.Type.Value != None:
                print("\tValue: " + str(vox.Type.Value))
            if vox.Type.Constr != None:
                print("\tConstr: " + str(vox.Type.Constr))
            if vox.Type.Scale != None:
                print("\tScale: " + str(vox.Type.Scale))      
            if vox.Type.Arity != None:
                print("\tArity: " + str(vox.Type.Arity))
            if vox.Type.Referent != None:
                print("\tReferent: " + str(vox.Type.Referent))
            if vox.Type.Mapping != None:
                print("\tMapping: " + str(vox.Type.Mapping))  
            if len(vox.Type.Corresps) > 0:
                print("\tCorresps:")
                for x in vox.Type.Corresps:
                    print("\t\tCorresp: Value: " + str(x.Value))
        if len(vox.Habitat.Intrinsic) > 0 or len(vox.Habitat.Extrinsic) > 0:
            print("Habitat:")
            if len(vox.Habitat.Intrinsic) > 0:
                print("\tIntrinsic")
                for x in vox.Habitat.Intrinsic:
                    if x.Name != None or x.Value != None:
                        print("\t\tIntr:")
                        if x.Name != None:
                            print("\t\t\tName: " + str(x.Name))
                        if x.Value != None:
                            print("\t\t\tValue: " + str(x.Value))
            if len(vox.Habitat.Extrinsic) > 0:
                print("\tExtrinsic")
                for x in vox.Habitat.Extrinsic:
                    if x.Name != None or x.Value != None:
                        print("\t\tExtr:")
                        if x.Name != None:
                            print("\t\t\tName: " + str(x.Name))
                        if x.Value != None:
                            print("\t\t\tValue: " + str(x.Value))
        if len(vox.AffordStr.Affordances) > 0:
            print("AffordStr:\n\tAffordances")
            for x in vox.AffordStr.Affordances:
                print("\t\tAffordance: Formula: " + str(x.Formula))
        if vox.Embodiment.Scale != None or vox.Embodiment.Movable != None:
            print("Embodiment:")#
            if vox.Embodiment.Scale != None:
                print("\tScale: " + str(vox.Embodiment.Scale))
            if vox.Embodiment.Movable != None:
                print("\tMovable: " + str(vox.Embodiment.Movable))
        if len(vox.Attributes.Attrs) > 0:
            print("Attributes:\n\tAttrs:")
            for x in vox.Attributes.Attrs:
                print("\t\tAttr: Value: " + str(x.Value))

    # just a function to do nothing -> execute multiple functions in lambda expression
    def doNothing(self, *args):
        pass
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainVoxMLWindow()
    sys.exit(app.exec_())