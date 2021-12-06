import torch

import xml.etree.ElementTree as ET

from VoxML.VoxMLClasses import *

class VoxMLDataLoader:
    def __init__(self) -> None:
        self.classdict = {
                0: "airplane",
                1: "bathtub",
                2: "bed",
                3: "bench",
                4: "bookshelf",
                5: "bottle",
                6: "bowl",
                7: "car",
                8: "chair",
                9: "cone",
                10: "cup",
                11: "curtain",
                12: "desk",
                13: "door",
                14: "dresser",
                15: "flower_pot",
                16: "glass_box",
                17: "guitar",
                18: "keyboard",
                19: "lamp",
                20: "laptop",
                21: "mantel",
                22: "monitor",
                23: "night_stand",
                24: "person",
                25: "piano",
                26: "plant",
                27: "radio",
                28: "range_hood",
                29: "sink",
                30: "sofa",
                31: "stairs",
                32: "stool",
                33: "table",
                34: "tent",
                35: "toilet",
                36: "tv_stand",
                37: "vase",
                38: "wardrobe",
                39: "xbox",
                }
        self.plotter = None
    
    # copied from old project
    def initModel(self):
        model = DGCNN().to(torch.device("cpu"))
        model = torch.nn.DataParallel(model)
        model.load_state_dict(torch.load("voml-framework\\VoxMLData\\models\\custommodelorig.t7", map_location = torch.device("cpu")))
        model = model.eval()
        self.model = model

    # parse VoxML data file into VoxMLObject
    def loadFileToObject(self, inpath) -> VoxMLObject:
        if inpath.endswith(".xml") or inpath.endswith(".txt"):
            vox = VoxMLObject()
            vox.filepath = inpath
            VoxML = ET.parse(inpath).getroot()
            
            # VoxML
            Entity = VoxML.find("Entity")
            Lex = VoxML.find("Lex")
            Type = VoxML.find("Type")
            Habitat = VoxML.find("Habitat")
            AffordStr = VoxML.find("Afford_Str")
            Embodiment = VoxML.find("Embodiment")
            Attributes = VoxML.find("Attributes")

            # Entity
            if Entity is not None:
                vox.Entity.Type = Entity.get("Type")

            # Lex
            if Lex is not None:
                vox.Lex.Pred = VoxML.findtext("Lex/Pred")  
                vox.Lex.Type = VoxML.findtext("Lex/Type")
            
            # Type
            if Type is not None:
                vox.Type.Head = VoxML.findtext("Type/Head")
                vox.Type.Concavity = VoxML.findtext("Type/Concavity")
                vox.Type.RotatSym = VoxML.findtext("Type/RotatSym")
                vox.Type.ReflSym = VoxML.findtext("Type/ReflSym")
                vox.Type.Class = VoxML.findtext("Type/Class")
                vox.Type.Value = VoxML.findtext("Type/Value")
                vox.Type.Constr = VoxML.findtext("Type/Constr")
                vox.Type.Scale = VoxML.findtext("Type/Scale")
                vox.Type.Arity = VoxML.findtext("Type/Arity")
                vox.Type.Referent = VoxML.findtext("Type/Referent")
                vox.Type.Mapping = VoxML.findtext("Type/Mapping")

                for comp in VoxML.findall("Type/Components/Component"):
                    vComp = vComponent()
                    vComp.Value = comp.get("Value")
                    vox.Type.Components.append(vComp)
                for arg in VoxML.findall("Type/Args/Arg"):
                    vAr = vArg()
                    vAr.Value = arg.get("Value")
                    vox.Type.Args.append(vAr)
                for subev in VoxML.findall("Type/Body/Subevent"):
                    vSubev = vSubevent()
                    vSubev.Value = subev.get("Value")
                    vox.Type.Body.append(vSubev)
                for corr in VoxML.findall("Type/Corresps/Corresp"):
                    vCorr = vCorresp()
                    vCorr.Value = corr.get("Value")
                    vox.Type.Corresps.append(vCorr)

            # Habitat
            if Habitat is not None:
                for intr in VoxML.findall("Habitat/Intrinsic/Intr"):
                    vInt = vIntr()
                    vInt.Name = intr.get("Name")
                    vInt.Value = intr.get("Value")
                    vox.Habitat.Intrinsic.append(vInt)
                for extr in VoxML.findall("Habitat/Extrinsic/Extr"):
                    vExt = vExtr()
                    vExt.Name = extr.get("Name")
                    vExt.Value = extr.get("Value")
                    vox.Habitat.Extrinsic.append(vExt)
            
            # AffordStr
            if AffordStr is not None:
                for afford in VoxML.findall("Afford_Str/Affordances/Affordance"):
                    vAfford = vAffordance()
                    vAfford.Formula = afford.get("Formula")
                    vox.AffordStr.Affordances.append(vAfford)
            
            # Embodiment
            if Embodiment is not None:
                vox.Embodiment.Scale = VoxML.findtext("Embodiment/Scale")
                vox.Embodiment.Movable = VoxML.findtext("Embodiment/Movable")
            
            # Attributes
            if Attributes is not None:
                for attr in VoxML.findall("Attributes/Attrs/Attr"):
                    vAtt = vAttr()
                    vAtt.Value = attr.get("Value")
                    vox.Attributes.Attrs.append(vAtt)
            
            return vox

    # create XML string from VoxMLObject
    def loadObjectToXML(self, vox: VoxMLObject) -> str:
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

    # load 3D object     


# copied from 
# https://github.com/WangYueFt/dgcnn/blob/master/pytorch/model.py
class DGCNN(torch.nn.Module):
    def __init__(self, outputChannels = 40) -> None:
        super(DGCNN, self).__init__()
        self.k = 20
        
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.bn2 = torch.nn.BatchNorm2d(64)
        self.bn3 = torch.nn.BatchNorm2d(128)
        self.bn4 = torch.nn.BatchNorm2d(256)
        self.bn5 = torch.nn.BatchNorm1d(1024)

        self.conv1 = torch.nn.Sequential(torch.nn.Conv2d(6, 64, kernel_size=1, bias=False), self.bn1, torch.nn.LeakyReLU(negative_slope=0.2))
        self.conv2 = torch.nn.Sequential(torch.nn.Conv2d(64*2, 64, kernel_size=1, bias=False), self.bn2, torch.nn.LeakyReLU(negative_slope=0.2))
        self.conv3 = torch.nn.Sequential(torch.nn.Conv2d(64*2, 128, kernel_size=1, bias=False), self.bn3, torch.nn.LeakyReLU(negative_slope=0.2))
        self.conv4 = torch.nn.Sequential(torch.nn.Conv2d(128*2, 256, kernel_size=1, bias=False), self.bn4, torch.nn.LeakyReLU(negative_slope=0.2))
        self.conv5 = torch.nn.Sequential(torch.nn.Conv1d(512, 1024, kernel_size=1, bias=False), self.bn5, torch.nn.LeakyReLU(negative_slope=0.2))

        self.linear1 = torch.nn.Linear(1024*2, 512, bias=False)
        self.bn6 = torch.nn.BatchNorm1d(512)
        self.linear2 = torch.nn.Linear(512, 256)
        self.bn7 = torch.nn.BatchNorm1d(256)
        self.linear3 = torch.nn.Linear(256, outputChannels.nnels)
