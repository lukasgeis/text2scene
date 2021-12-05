# Python Dataclasses to implement VoxML Entities
# created using files in https://github.com/VoxML/VoxSim/tree/main/VoxML/voxml as reference
# will be modified/expanded later on if new entites emerge

import xml.etree.ElementTree as ET

# ======================== #
#        MAIN CLASS        #
# ======================== #

class VoxMLObject:
    def __init__(self) -> None:
        self.filepath = None
        self.xmlns_xsi = "http://www.w3.org/2001/XMLSchema-instance" 
        self.xmlns_xsd = "http://www.w3.org/2001/XMLSchema"
        self.Entity = vEntity()
        self.Lex = vLex()
        self.Type = vType()
        self.Habitat = vHabitat()
        self.AffordStr = vAffordStr()
        self.Embodiment = vEmbodiment()
        self.Attributes = vAttributes()
    
    # Parse VoxML data file into VoxMLObject
    def loadObjectFromFile(self, inpath: str) -> None:
        if inpath.endswith(".xml") or inpath.endswith(".txt"):
            self.filepath = inpath
            VoxML = ET.parse(inpath).getroot()
            
            Entity = VoxML.find("Entity")
            Lex = VoxML.find("Lex")
            Type = VoxML.find("Type")
            Habitat = VoxML.find("Habitat")
            AffordStr = VoxML.find("Afford_Str")
            Embodiment = VoxML.find("Embodiment")
            Attributes = VoxML.find("Attributes")

            if Entity is not None:
                self.Entity.Type = Entity.get("Type")

            if Lex is not None:
                self.Lex.Pred = VoxML.findtext("Lex/Pred")  
                self.Lex.Type = VoxML.findtext("Lex/Type")
            
            if Type is not None:
                self.Type.Head = VoxML.findtext("Type/Head")
                self.Type.Concavity = VoxML.findtext("Type/Concavity")
                self.Type.RotatSym = VoxML.findtext("Type/RotatSym")
                self.Type.ReflSym = VoxML.findtext("Type/ReflSym")
                self.Type.Class = VoxML.findtext("Type/Class")
                self.Type.Value = VoxML.findtext("Type/Value")
                self.Type.Constr = VoxML.findtext("Type/Constr")
                self.Type.Scale = VoxML.findtext("Type/Scale")
                self.Type.Arity = VoxML.findtext("Type/Arity")
                self.Type.Referent = VoxML.findtext("Type/Referent")
                self.Type.Mapping = VoxML.findtext("Type/Mapping")

                for comp in VoxML.findall("Type/Components/Component"):
                    vComp = vComponent()
                    vComp.Value = comp.get("Value")
                    self.Type.Components.append(vComp)
                for arg in VoxML.findall("Type/Args/Arg"):
                    vAr = vArg()
                    vAr.Value = arg.get("Value")
                    self.Type.Args.append(vAr)
                for subev in VoxML.findall("Type/Body/Subevent"):
                    vSubev = vSubevent()
                    vSubev.Value = subev.get("Value")
                    self.Type.Body.append(vSubev)
                for corr in VoxML.findall("Type/Corresps/Corresp"):
                    vCorr = vCorresp()
                    vCorr.Value = corr.get("Value")
                    self.Type.Corresps.append(vCorr)

            if Habitat is not None:
                for intr in VoxML.findall("Habitat/Intrinsic/Intr"):
                    vInt = vIntr()
                    vInt.Name = intr.get("Name")
                    vInt.Value = intr.get("Value")
                    self.Habitat.Intrinsic.append(vInt)
                for extr in VoxML.findall("Habitat/Extrinsic/Extr"):
                    vExt = vExtr()
                    vExt.Name = extr.get("Name")
                    vExt.Value = extr.get("Value")
                    self.Habitat.Extrinsic.append(vExt)
            
            if AffordStr is not None:
                for afford in VoxML.findall("Afford_Str/Affordances/Affordance"):
                    vAfford = vAffordance()
                    vAfford.Formula = afford.get("Formula")
                    self.AffordStr.Affordances.append(vAfford)
            
            if Embodiment is not None:
                self.Embodiment.Scale = VoxML.findtext("Embodiment/Scale")
                self.Embodiment.Movable = VoxML.findtext("Embodiment/Movable")
            
            if Attributes is not None:
                for attr in VoxML.findall("Attributes/Attrs/Attr"):
                    vAtt = vAttr()
                    vAtt.Value = attr.get("Value")
                    self.Attributes.Attrs.append(vAtt)
            
    # Create XMl string from this object
    def createXMLString(self) -> str:
        # VoxML
        VoxML = ET.Element("VoxML")
        VoxML.set("xmlns:xsi", self.xmlns_xsi)
        VoxML.set("xmlns:xsd", self.xmlns_xsd)

        # Entity
        Entity = ET.SubElement(VoxML, "Entity")
        Entity.set("Type", str(self.Entity.Type))

        # Lex
        Lex = ET.SubElement(VoxML, "Lex")
        LexPred = ET.SubElement(Lex, "Pred")
        LexType = ET.SubElement(Lex, "Type")
        if self.Lex.Pred != None:
            LexPred.text = str(self.Lex.Pred)
        if self.Lex.Type != None:
            LexType.text = str(self.Lex.Type)
        
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
        if self.Type.Head != None:
            TypeHead.text = str(self.Type.Head)
        if len(self.Type.Components) > 0:
                for x in self.Type.Components:
                    TypeComponentsComponent = ET.SubElement(TypeComponents, "Component")
                    TypeComponentsComponent.set("Value", str(x.Value))
        if self.Type.Concavity != None:
                TypeConcavity.text = str(self.Type.Concavity)
        if self.Type.RotatSym != None:
                TypeRotatSym.text = str(self.Type.RotatSym)
        if self.Type.ReflSym != None:
                TypeReflSym.text = str(self.Type.ReflSym)
        if len(self.Type.Args) > 0:
                for x in self.Type.Args:
                    TypeArgsArg = ET.SubElement(TypeArgs, "Arg")
                    TypeArgsArg.set("Value", str(x.Value))
        if len(self.Type.Body) > 0:
                for x in self.Type.Body:
                    TypeBodySubevent = ET.SubElement(TypeBody, "Subevent")
                    TypeBodySubevent.set("Value", str(x.Value))
        if self.Type.Class != None:
                TypeClass.text = str(self.Type.Class)
        if self.Type.Value != None:
                TypeValue.text = str(self.Type.Value)
        if self.Type.Constr != None:
                TypeConstr.text = str(self.Type.Constr)
        if self.Type.Scale != None:
                TypeScale.text = str(self.Type.Scale)    
        if self.Type.Arity != None:
                TypeArity.text = str(self.Type.Arity)
        if self.Type.Referent != None:
                TypeReferent.text = str(self.Type.Referent)
        if self.Type.Mapping != None:
                TypeMapping.text = str(self.Type.Mapping) 
        if len(self.Type.Corresps) > 0:
                for x in self.Type.Corresps:
                    TypeCorrespsCorresp = ET.SubElement(TypeCorresps, "Corresp")
                    TypeCorrespsCorresp.set("Value", str(x.Value))

        # Habitat
        Habitat = ET.SubElement(VoxML, "Habitat")
        HabitatIntrinsic = ET.SubElement(Habitat, "Intrinsic")
        HabitatExtrinsic = ET.SubElement(Habitat, "Extrinsic")
        if len(self.Habitat.Intrinsic) > 0:
                for x in self.Habitat.Intrinsic:
                    HabitatIntrinsicIntr = ET.SubElement(HabitatIntrinsic, "Intr")
                    HabitatIntrinsicIntr.set("Name", str(x.Name))
                    HabitatIntrinsicIntr.set("Value", str(x.Value))
        if len(self.Habitat.Extrinsic) > 0:
                for x in self.Habitat.Extrinsic:
                    HabitatExtrinsicExtr = ET.SubElement(HabitatExtrinsic, "Extr")
                    HabitatExtrinsicExtr.set("Name", str(x.Name))
                    HabitatExtrinsicExtr.set("Value", str(x.Value))
        
        # AffordStr
        AffordStr = ET.SubElement(VoxML, "AffordStr")
        AffordStrAffordances = ET.SubElement(AffordStr, "Affordances")
        if len(self.AffordStr.Affordances) > 0:
            for x in self.AffordStr.Affordances:
                AffordStrAffordancesAffordance = ET.SubElement(AffordStrAffordances, "Affordance")
                AffordStrAffordancesAffordance.set("Formula", str(x.Formula))
        
        # Embodiment
        Embodiment = ET.SubElement(VoxML, "Embodiment")
        EmbodimentScale = ET.SubElement(Embodiment, "Scale")
        EmbodimentMovable = ET.SubElement(Embodiment, "Movable")
        if self.Embodiment.Scale != None:
            EmbodimentScale.text = str(self.Embodiment.Scale)
        if self.Embodiment.Movable != None:
            EmbodimentMovable.text = str(self.Embodiment.Movable)
        
        # Attributes
        Attributes = ET.SubElement(VoxML, "Attributes")
        AttributesAttrs = ET.SubElement(AffordStr, "Attrs")
        if len(self.Attributes.Attrs) > 0:
            for x in self.Attributes.Attrs:
                AttributesAttrsAttr = ET.SubElement(AttributesAttrs, "Attr")
                AttributesAttrsAttr.set("Value", str(x.Value))

        return ET.tostring(VoxML)        



# ======================== #
#        SUBCLASSES        #
# ======================== #

class vEntity:
    def __init__(self) -> None:
        self.Type = None

class vLex:
    def __init__(self) -> None:
        self.Pred = None
        self.Type = None

class vType:
    def __init__(self) -> None:
        self.Head = None
        self.Components = []        # list of vComponent objects
        self.Concavity = None
        self.RotatSym = None
        self.ReflSym = None
        self.Args = []              # list of vArg objects
        self.Body = []              # list of vSubevent objects
        self.Class = None
        self.Value = None
        self.Constr = None
        self.Scale = None
        self.Arity = None 
        self.Referent = None
        self.Mapping = None
        self.Corresps = []          # list of vCorresp objects

class vHabitat:
    def __init__(self) -> None:
        self.Intrinsic = []         # list of vIntr objects
        self.Extrinsic = []         # list of vExtr objects

class vAffordStr:
    def __init__(self) -> None:
        self.Affordances = []       # list of vAffordance objects

class vEmbodiment:
    def __init__(self) -> None:
        self.Scale = None
        self.Movable = None

class vAttributes:
    def __init__(self) -> None:
        self.Attrs = []             # list of vAttr objects


# =========================== #
#        SUBSUBCLASSES        #
# =========================== #

class vComponent:
    def __init__(self) -> None:
        self.Value = None

class vArg:
    def __init__(self) -> None:
        self.Value = None

class vSubevent:
    def __init__(self) -> None:
        self.Value = None

class vCorresp:
    def __init__(self) -> None:
        self.Value = None

class vIntr:
    def __init__(self) -> None:
        self.Name = None
        self.Value = None

class vExtr:
    def __init__(self) -> None:
        self.Name = None
        self.Value = None

class vAffordance:
    def __init__(self) -> None:
        self.Formula = None

class vAttr:
    def __init__(self) -> None:
        self.Value = None
