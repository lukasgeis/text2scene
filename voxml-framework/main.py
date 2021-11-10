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

        # Remove everything outside of backgroundFrame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # button logic
        self.ui.openVoxMLDataButton.clicked.connect(lambda: self.parseVoxMLData(self.chooseVoxMLData()))
        self.ui.exitButton.clicked.connect(lambda: sys.exit())

        self.show()

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
                
            
            

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainVoxMLWindow()
    sys.exit(app.exec_())