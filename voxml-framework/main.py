# Basic imports
import sys
import xml.etree.ElementTree as ET

# PyQt5 imports
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

# Scenes imports
from Scenes.Scripts.MainVoxMLWindow import Ui_MainVoxMLWindow

# VoxML imports
from VoxML.VoxMLClasses import *

# Main Window class
class MainVoxMLWindow(QMainWindow):
    def __init__(self) -> None:
        # Create and setup window
        QMainWindow.__init__(self)
        self.ui = Ui_MainVoxMLWindow()
        self.ui.setupUi(self)

        # Vars
        self.allObj = []

        # Remove everything outside of backgroundFrame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # main button logic
        self.ui.openVoxMLDataButton.clicked.connect(lambda: self.appendNewObject(self.parseVoxMLData(self.chooseVoxMLData())))
        self.ui.exitButton.clicked.connect(lambda: sys.exit())

        # editing logic
        self.ui.entityBtn.clicked.connect(lambda: self.switchEditingFrame("entity"))
        self.ui.lexBtn.clicked.connect(lambda: self.switchEditingFrame("lex"))
        self.ui.typeBtn.clicked.connect(lambda: self.switchEditingFrame("type"))
        self.ui.habitatBtn.clicked.connect(lambda: self.switchEditingFrame("habitat"))
        self.ui.affordStrBtn.clicked.connect(lambda: self.switchEditingFrame("affordStr"))
        self.ui.embodimentBtn.clicked.connect(lambda: self.switchEditingFrame("embodiment"))
        self.ui.attributesBtn.clicked.connect(lambda: self.switchEditingFrame("attributes"))
        self.switchEditingFrame("none") # hide all frames in the beginning

        # setup position and show window
        self.oldPos = self.pos()
        self.show()

    # called when mouse is pressed on window -> save current window position
    def mousePressEvent(self, event) -> None:
        self.oldPos = event.globalPos()
    
    # called when mouse is pressed and moved -> drag and move window
    def mouseMoveEvent(self, event) -> None:
        if not True in [x.underMouse() for x in [self.ui.editingFrame,self.ui.exitButton,self.ui.openVoxMLDataButton,self.ui.saveVoxMLData,self.ui.templateChooser,self.ui.createVoxMLButton]]:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

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


    # Appends new object to allObj -> only used in lambda expression
    def appendNewObject(self, obj: VoxMLObject) -> None:
        if obj != None:
            self.allObj.append(obj)
            self.printLastVoxMLObject() # Testing purposes

    # Choose .txt or .xml file containing VoxML data from system
    def chooseVoxMLData(self) -> str:
        return QFileDialog.getOpenFileName(self, "Choose file", "voml-framework\\VoxMLData", "VoxML Data (*.txt *.xml)")[0]

    # Parse VoxML data file into VoxMLObject -> use together with chooseVoxMLData    
    def parseVoxMLData(self, inpath) -> VoxMLObject:
        if inpath.endswith(".xml") or inpath.endswith(".txt"):
            voxData = VoxMLObject()
            voxData.filepath = inpath
            VoxML = ET.parse(inpath).getroot()
            
            Entity = VoxML.find("Entity")
            Lex = VoxML.find("Lex")
            Type = VoxML.find("Type")
            Habitat = VoxML.find("Habitat")
            AffordStr = VoxML.find("Afford_Str")
            Embodiment = VoxML.find("Embodiment")
            Attributes = VoxML.find("Attributes")

            if Entity is not None:
                voxData.Entity.Type = Entity.get("Type")

            if Lex is not None:
                voxData.Lex.Pred = VoxML.findtext("Lex/Pred")  
                voxData.Lex.Type = VoxML.findtext("Lex/Type")
            
            if Type is not None:
                voxData.Type.Head = VoxML.findtext("Type/Head")
                voxData.Type.Concavity = VoxML.findtext("Type/Concavity")
                voxData.Type.RotatSym = VoxML.findtext("Type/RotatSym")
                voxData.Type.ReflSym = VoxML.findtext("Type/ReflSym")
                voxData.Type.Class = VoxML.findtext("Type/Class")
                voxData.Type.Value = VoxML.findtext("Type/Value")
                voxData.Type.Constr = VoxML.findtext("Type/Constr")
                voxData.Type.Scale = VoxML.findtext("Type/Scale")
                voxData.Type.Arity = VoxML.findtext("Type/Arity")
                voxData.Type.Referent = VoxML.findtext("Type/Referent")
                voxData.Type.Mapping = VoxML.findtext("Type/Mapping")

                for comp in VoxML.findall("Type/Components/Component"):
                    vComp = vComponent()
                    vComp.Value = comp.get("Value")
                    voxData.Type.Components.append(vComp)
                for arg in VoxML.findall("Type/Args/Arg"):
                    vAr = vArg()
                    vAr.Value = arg.get("Value")
                    voxData.Type.Args.append(vAr)
                for subev in VoxML.findall("Type/Body/Subevent"):
                    vSubev = vSubevent()
                    vSubev.Value = subev.get("Value")
                    voxData.Type.Body.append(vSubev)
                for corr in VoxML.findall("Type/Corresps/Corresp"):
                    vCorr = vCorresp()
                    vCorr.Value = corr.get("Value")
                    voxData.Type.Corresps.append(vCorr)

            if Habitat is not None:
                for intr in VoxML.findall("Habitat/Intrinsic/Intr"):
                    vInt = vIntr()
                    vInt.Name = intr.get("Name")
                    vInt.Value = intr.get("Value")
                    voxData.Habitat.Intrinsic.append(vInt)
                for extr in VoxML.findall("Habitat/Extrinsic/Extr"):
                    vExt = vExtr()
                    vExt.Name = extr.get("Name")
                    vExt.Value = extr.get("Value")
                    voxData.Habitat.Extrinsic.append(vExt)
            
            if AffordStr is not None:
                for afford in VoxML.findall("Afford_Str/Affordances/Affordance"):
                    vAfford = vAffordance()
                    vAfford.Formula = afford.get("Formula")
                    voxData.AffordStr.Affordances.append(vAfford)
            
            if Embodiment is not None:
                voxData.Embodiment.Scale = VoxML.findtext("Embodiment/Scale")
                voxData.Embodiment.Movable = VoxML.findtext("Embodiment/Movable")
            
            if Attributes is not None:
                for attr in VoxML.findall("Attributes/Attrs/Attr"):
                    vAtt = vAttr()
                    vAtt.Value = attr.get("Value")
                    voxData.Attributes.Attrs.append(vAtt)
            
            return voxData

    # Print last added/parsed VoxMLObject to console :: only for testing purposes / will be removed later
    def printLastVoxMLObject(self):
        if len(self.allObj) == 0:
            return
        vox = self.allObj[-1]
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

            
            

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainVoxMLWindow()
    sys.exit(app.exec_())