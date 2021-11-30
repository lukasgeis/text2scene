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
        self.ui.createVoxMLButton.clicked.connect(lambda: self.createNewVoxMLObject(str(self.ui.templateChooser.currentText())))
        self.ui.saveVoxMLData.clicked.connect(lambda: self.saveDataToFile(self.createXMLStringFromVoxMLObject()))
        self.ui.saveToObject.clicked.connect(lambda: self.saveDataToObject())

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
        self.ui.affordStrAffordancesDelete.clicked.connect(lambda: self.deleteFromBox("affordances"))
        self.ui.attributesAttrsAdd.clicked.connect(lambda: self.addToBox("attrs"))
        self.ui.attributesAttrsDelete.clicked.connect(lambda: self.deleteFromBox("attrs"))

        # setup position and show window
        self.oldPos = self.pos()
        self.show()

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
        elif attr == "affordances":
            self.ui.affordStrAffordances.addItem(str(self.ui.affordStrAffordancesNewItem.text()))
            self.ui.affordStrAffordancesNewItem.setText("")
        elif attr == "attrs":
            self.ui.attributesAttrs.addItem(str(self.ui.attributesAttrsNewItem.text()))
            self.ui.attributesAttrsNewItem.setText("")

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
        elif attr == "affordances":
            self.ui.affordStrAffordances.removeItem(self.ui.affordStrAffordances.currentIndex())
        elif attr == "attrs":
            self.ui.attributesAttrs.removeItem(self.ui.attributesAttrs.currentIndex())

    # called when mouse is pressed on window -> save current window position
    def mousePressEvent(self, event) -> None:
        self.oldPos = event.globalPos()
    
    # called when mouse is pressed and moved -> drag and move window
    def mouseMoveEvent(self, event) -> None:
        if not True in [x.underMouse() for x in [self.ui.editingFrame,self.ui.exitButton,self.ui.openVoxMLDataButton,self.ui.saveVoxMLData,self.ui.templateChooser,self.ui.createVoxMLButton]]:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

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

    # show specific editing attributes for specific template
    def createNewVoxMLObject(self, template, create = True):
        if create:
            self.allObj.append(VoxMLObject())
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

    # Appends new object to allObj -> only used in lambda expression
    def appendNewObject(self, obj: VoxMLObject) -> None:
        if obj != None:
            self.allObj.append(obj)
            self.loadDataToEditing()
            self.createNewVoxMLObject(str(obj.Entity.Type), False)

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

    def createXMLStringFromVoxMLObject(self) -> str:
        if len(self.allObj) == 0:
            return
        vox = self.allObj[-1]

        # VoxML
        VoxML = ET.Element("VoxML")
        VoxML.set("xmlns:xsi", vox.xmlns_xsi)
        VoxML.set("xmlns:xsd", vox.xmlns_xsd)

        # Entity
        Entity = ET.SubElement(VoxML, "Entity")
        Entity.set("Type", str(vox.Entity.Type))

        # Lex
        Lex = ET.SubElement(VoxML, "Lex")
        LexPred = ET.SubElement(Lex, "Pred")
        LexType = ET.SubElement(Lex, "Type")
        if vox.Lex.Pred != None:
            LexPred.text = str(vox.Lex.Pred)
        if vox.Lex.Type != None:
            LexType.text = str(vox.Lex.Type)
        
        # Type
        Type = ET.SubElement(VoxML, "Type")
        TypeHead = ET.SubElement(Type, "Head")
        TypeComponents = ET.SubElement(Type, "Components")
        TypeConcavity = ET.SubElement(Type, "Concavity")
        TypeRotatSym = ET.SubElement(Type, "RotatSym")
        TypeReflSym = ET.SubElement(Type, "ReflSym")
        TypeArgs = ET.SubElement(Type, "Args")
        TypeBody = ET.SubElement(Type, "Body")
        TypeClass = ET.SubElement(Type, "Class")
        TypeValue = ET.SubElement(Type, "Value")
        TypeConstr = ET.SubElement(Type, "Constr")
        TypeScale = ET.SubElement(Type, "Scale")
        TypeArity = ET.SubElement(Type, "Arity")
        TypeReferent = ET.SubElement(Type, "Referent")
        TypeMapping = ET.SubElement(Type, "Mapping")
        TypeCorresps = ET.SubElement(Type, "Corresps")
        if vox.Type.Head != None:
            TypeHead.text = str(vox.Type.Head)
        if len(vox.Type.Components) > 0:
                for x in vox.Type.Components:
                    TypeComponentsComponent = ET.SubElement(TypeComponents, "Component")
                    TypeComponentsComponent.set("Value", str(x.Value))
        if vox.Type.Concavity != None:
                TypeConcavity.text = str(vox.Type.Concavity)
        if vox.Type.RotatSym != None:
                TypeRotatSym.text = str(vox.Type.RotatSym)
        if vox.Type.ReflSym != None:
                TypeReflSym.text = str(vox.Type.ReflSym)
        if len(vox.Type.Args) > 0:
                for x in vox.Type.Args:
                    TypeArgsArg = ET.SubElement(TypeArgs, "Arg")
                    TypeArgsArg.set("Value", str(x.Value))
        if len(vox.Type.Body) > 0:
                for x in vox.Type.Body:
                    TypeBodySubevent = ET.SubElement(TypeBody, "Subevent")
                    TypeBodySubevent.set("Value", str(x.Value))
        if vox.Type.Class != None:
                TypeClass.text = str(vox.Type.Class)
        if vox.Type.Value != None:
                TypeValue.text = str(vox.Type.Value)
        if vox.Type.Constr != None:
                TypeConstr.text = str(vox.Type.Constr)
        if vox.Type.Scale != None:
                TypeScale.text = str(vox.Type.Scale)    
        if vox.Type.Arity != None:
                TypeArity.text = str(vox.Type.Arity)
        if vox.Type.Referent != None:
                TypeReferent.text = str(vox.Type.Referent)
        if vox.Type.Mapping != None:
                TypeMapping.text = str(vox.Type.Mapping) 
        if len(vox.Type.Corresps) > 0:
                for x in vox.Type.Corresps:
                    TypeCorrespsCorresp = ET.SubElement(TypeCorresps, "Corresp")
                    TypeCorrespsCorresp.set("Value", str(x.Value))

        # Habitat
        Habitat = ET.SubElement(VoxML, "Habitat")
        HabitatIntrinsic = ET.SubElement(Habitat, "Intrinsic")
        HabitatExtrinsic = ET.SubElement(Habitat, "Extrinsic")
        if len(vox.Habitat.Intrinsic) > 0:
                for x in vox.Habitat.Intrinsic:
                    HabitatIntrinsicIntr = ET.SubElement(HabitatIntrinsic, "Intr")
                    HabitatIntrinsicIntr.set("Name", str(x.Name))
                    HabitatIntrinsicIntr.set("Value", str(x.Value))
        if len(vox.Habitat.Extrinsic) > 0:
                for x in vox.Habitat.Extrinsic:
                    HabitatExtrinsicExtr = ET.SubElement(HabitatExtrinsic, "Extr")
                    HabitatExtrinsicExtr.set("Name", str(x.Name))
                    HabitatExtrinsicExtr.set("Value", str(x.Value))
        
        # AffordStr
        AffordStr = ET.SubElement(VoxML, "AffordStr")
        AffordStrAffordances = ET.SubElement(AffordStr, "Affordances")
        if len(vox.AffordStr.Affordances) > 0:
            for x in vox.AffordStr.Affordances:
                AffordStrAffordancesAffordance = ET.SubElement(AffordStrAffordances, "Affordance")
                AffordStrAffordancesAffordance.set("Formula", str(x.Formula))
        
        # Embodiment
        Embodiment = ET.SubElement(VoxML, "Embodiment")
        EmbodimentScale = ET.SubElement(Embodiment, "Scale")
        EmbodimentMovable = ET.SubElement(Embodiment, "Movable")
        if vox.Embodiment.Scale != None:
            EmbodimentScale.text = str(vox.Embodiment.Scale)
        if vox.Embodiment.Movable != None:
            EmbodimentMovable.text = str(vox.Embodiment.Movable)
        
        # Attributes
        Attributes = ET.SubElement(VoxML, "Attributes")
        AttributesAttrs = ET.SubElement(AffordStr, "Attrs")
        if len(vox.Attributes.Attrs) > 0:
            for x in vox.Attributes.Attrs:
                AttributesAttrsAttr = ET.SubElement(AttributesAttrs, "Attr")
                AttributesAttrsAttr.set("Value", str(x.Value))

        return ET.tostring(VoxML)

    # save xml data to file with QFileDialog -> use together with createXMLStringFromVoxMLObject
    def saveDataToFile(self, outputStr):
        fileName = QFileDialog.getSaveFileName(self, "Save File", "voml-framework\\VoxMLData", "VoxML Data (*.xml *.txt )")[0]
        if len(fileName) > 0:
            self.printLastVoxMLObject() # Testing purposes
            with open(fileName, "w") as f:
                f.write(outputStr.decode("utf-8"))
        
    # save current input data to last VoxML Object
    def saveDataToObject(self):
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
        vox.AffordStr.Affordances = []
        for x in range(self.ui.affordStrAffordances.count()):
            aff = vAffordance()
            aff.Formula = str(self.ui.affordStrAffordances.itemText(x))
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
        vox.Attributes.Attrs = []
        for x in range(self.ui.attributesAttrs.count()):
            attr = vAttr()
            attr.Value = str(self.ui.attributesAttrs.itemText(x))
            vox.Attributes.Attrs.append(attr)

        self.allObj[-1] = vox
        self.loadDataToEditing()

    # update text and checkboxes for VoxMLObject
    def loadDataToEditing(self):
        vox = self.allObj[-1]
        
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

        # AffordStr
        self.ui.affordStrAffordances.clear()
        for x in vox.AffordStr.Affordances:
            self.ui.affordStrAffordances.addItem(str(x.Formula))
        
        # Embodiment
        if vox.Embodiment.Scale != None:
            self.ui.embodimentScale.setText(str(vox.Embodiment.Scale))
        if vox.Embodiment.Movable:
            self.ui.embodimentMovable.setChecked(True)
        else:
            self.ui.embodimentMovable.setChecked(False)
        
        # Attributes
        self.ui.attributesAttrs.clear()
        for x in vox.Attributes.Attrs:
            self.ui.attributesAttrs.addItem(str(x.Value))

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