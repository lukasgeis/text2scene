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

        # button logic
        self.ui.openVoxMLDataButton.clicked.connect(lambda: self.appendNewObject(self.parseVoxMLData(self.chooseVoxMLData())))
        self.ui.exitButton.clicked.connect(lambda: sys.exit())

        self.show()

    # Appends new object to allObj -> only used in lambda expression
    def appendNewObject(self, obj: VoxMLObject) -> None:
        self.allObj.append(obj)

    # Choose .txt or .xml file containing VoxML data from system
    def chooseVoxMLData(self) -> str:
        return QFileDialog.getOpenFileName(self, "Choose file", "voml-framework\\VoxMLData", "VoxML Data (*.txt *.xml)")[0]

    # Parse VoxML data file into VoxMLObject -> use together with chooseVoxMLData    
    def parseVoxMLData(self, inpath) -> VoxMLObject:
        if inpath.endswith(".xml") or inpath.endswith(".txt"):
            voxData = VoxMLObject()
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
            
            

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainVoxMLWindow()
    sys.exit(app.exec_())