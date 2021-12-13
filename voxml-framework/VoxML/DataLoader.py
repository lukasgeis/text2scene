import math
import torch
import random
import trimesh
from pyvista import read as pvRead
from pyvistaqt import BackgroundPlotter

from PIL import Image
from transformers import DetrFeatureExtractor, DetrForObjectDetection

import os
import xml.etree.ElementTree as ET

from VoxML.VoxMLClasses import *

class VoxMLDataLoader:
    def __init__(self) -> None:
        self.objClassdict = {
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
        self.imgClassdict = {
                0: "N/A",
                1: "person",
                10: "traffic light",
                11: "fire hydrant",
                12: "street sign",
                13: "stop sign",
                14: "parking meter",
                15: "bench",
                16: "bird",
                17: "cat",
                18: "dog",
                19: "horse",
                2: "bicycle",
                20: "sheep",
                21: "cow",
                22: "elephant",
                23: "bear",
                24: "zebra",
                25: "giraffe",
                26: "hat",
                27: "backpack",
                28: "umbrella",
                29: "shoe",
                3: "car",
                30: "eye glasses",
                31: "handbag",
                32: "tie",
                33: "suitcase",
                34: "frisbee",
                35: "skis",
                36: "snowboard",
                37: "sports ball",
                38: "kite",
                39: "baseball bat",
                4: "motorcycle",
                40: "baseball glove",
                41: "skateboard",
                42: "surfboard",
                43: "tennis racket",
                44: "bottle",
                45: "plate",
                46: "wine glass",
                47: "cup",
                48: "fork",
                49: "knife",
                5: "airplane",
                50: "spoon",
                51: "bowl",
                52: "banana",
                53: "apple",
                54: "sandwich",
                55: "orange",
                56: "broccoli",
                57: "carrot",
                58: "hot dog",
                59: "pizza",
                6: "bus",
                60: "donut",
                61: "cake",
                62: "chair",
                63: "couch",
                64: "potted plant",
                65: "bed",
                66: "mirror",
                67: "dining table",
                68: "window",
                69: "desk",
                7: "train",
                70: "toilet",
                71: "door",
                72: "tv",
                73: "laptop",
                74: "mouse",
                75: "remote",
                76: "keyboard",
                77: "cell phone",
                78: "microwave",
                79: "oven",
                8: "truck",
                80: "toaster",
                81: "sink",
                82: "refrigerator",
                83: "blender",
                84: "book",
                85: "clock",
                86: "vase",
                87: "scissors",
                88: "teddy bear",
                89: "hair drier",
                9: "boat",
                90: "toothbrush"
            }
        self.plotter = None
        self.initModels()
    
    # copied from old project
    def initModels(self):
        model = DGCNN().to(torch.device("cpu"))
        model = torch.nn.DataParallel(model)
        model.load_state_dict(torch.load("voxml-framework/VoxMLData/models/custommodelorig.t7", map_location = torch.device("cpu")))
        model = model.eval()
        self.model3D = model

        self.featureExtractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
        self.modelImg = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    # parse VoxML data file into VoxMLObject
    def loadFileToObject(self, inpath: str) -> VoxMLObject:
        if inpath == None:
            return
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

    # load 3D object  :: copied from old project   
    def load3Dobj(self, inpath: str):
        pointCloud = torch.tensor([self.createPointCloudFromFile(inpath).tolist()])
        pointCloud = pointCloud.permute(0, 2, 1)
        logits = self.model3D(pointCloud)
        guess = (logits.max(dim = 1)[1]).item()

        if self.plotter != None:
            self.plotter.close()
        self.plotter = BackgroundPlotter()
        self.plotter.add_mesh(pvRead(inpath))

        path = os.path.abspath("voxml-framework/VoxMLData/classificator/" + str(self.objClassdict[guess]) + ".txt").replace("\\", "/")           
        return self.loadFileToObject(path)

    # load Image to object :: using https://huggingface.co/facebook/detr-resnet-50
    def loadImage(self, inpath: str):
        img = Image.open(inpath)
        inputs = self.featureExtractor(images = img, return_tensors = "pt")
        outputs = self.modelImg(**inputs)

        guess = None
        for logits, bboxes in zip(outputs.logits[0], outputs.pred_boxes[0]):
            cls = logits.argmax()
            if cls >= len(self.imgClassdict):
                continue
            guess = self.imgClassdict[cls.item()]

        if guess == None:
            return

        path = None
        for root, dirs, files in os.walk("voxml-framework/VoxMLData"):
            if guess + ".txt" in files:
                path = os.path.abspath(os.path.join(root, guess + ".txt")).replace("\\", "/")   
            if guess + ".xml" in files:
                path = os.path.abspath(os.path.join(root, guess + ".xml")).replace("\\", "/")   
        
        return self.loadFileToObject(path)
        


        


    # create PointCloud from file :: copied from old project
    def createPointCloudFromFile(self, inpath: str):
        initialsize = 2048
        mesh = trimesh.load_mesh(inpath)
        sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

        if len(sample) != 2048:
            fstmul = (2048 / len(sample)) * 0.92
            initialsize = int(initialsize * fstmul)
            sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

        while len(sample) < 2048:
            initialsize = int(initialsize * 1.02)
            sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

        i = 0
        indices = []
        rightlensample = []

        if len(sample) != 2048:
            while i < 2048:
                rand_pt_idx = random.randint(0, len(sample) - 1)
                if rand_pt_idx not in indices:
                    indices.append(rand_pt_idx)
                    i += 1
                elif rand_pt_idx in indices:
                    pass
            for each in indices:
                rightlensample.append(sample[each])
        elif len(sample) == 2048:
            rightlensample = sample

        cloud = trimesh.points.PointCloud(rightlensample)
        pccenter = cloud.centroid
        for each in rightlensample:
            each[0] = each[0] - pccenter[0]
            each[1] = each[1] - pccenter[1]
            each[2] = each[2] - pccenter[2]

        maxdist = 0
        for each in rightlensample:
            dist = math.sqrt((each[0] ** 2) + (each[1] ** 2) + (each[2] ** 2))
            if dist >= maxdist:
                maxdist = dist

        for each in rightlensample:
            each[0] = each[0] / maxdist
            each[1] = each[1] / maxdist
            each[2] = each[2] / maxdist

        cloud2 = trimesh.points.PointCloud(rightlensample)

        maxdist = 0
        for each in rightlensample:
            dist = math.sqrt((each[0] ** 2) + (each[1] ** 2) + (each[2] ** 2))
            if dist >= maxdist:
                maxdist = dist

        rightlensample2 = []
        for each in cloud2:
            rightlensample2.append(each)

        converted = torch.FloatTensor(rightlensample2)
        return converted        



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
        self.linear3 = torch.nn.Linear(256, outputChannels)
    
    def forward(self, x):
        batch_size = x.size(0)
        x = get_graph_feature(x, k=self.k)
        x = self.conv1(x)
        x1 = x.max(dim=-1, keepdim=False)[0]

        x = get_graph_feature(x1, k=self.k)
        x = self.conv2(x)
        x2 = x.max(dim=-1, keepdim=False)[0]

        x = get_graph_feature(x2, k=self.k)
        x = self.conv3(x)
        x3 = x.max(dim=-1, keepdim=False)[0]

        x = get_graph_feature(x3, k=self.k)
        x = self.conv4(x)
        x4 = x.max(dim=-1, keepdim=False)[0]

        x = torch.cat((x1, x2, x3, x4), dim=1)

        x = self.conv5(x)
        x1 = torch.nn.functional.adaptive_max_pool1d(x, 1).view(batch_size, -1)
        x2 = torch.nn.functional.adaptive_avg_pool1d(x, 1).view(batch_size, -1)
        x = torch.cat((x1, x2), 1)

        x = torch.nn.functional.leaky_relu(self.bn6(self.linear1(x)), negative_slope=0.2)
        x = torch.nn.functional.leaky_relu(self.bn7(self.linear2(x)), negative_slope=0.2)
        x = self.linear3(x)
        return x

# copied from 
# https://github.com/WangYueFt/dgcnn/blob/master/pytorch/model.py
def knn(x, k):
    inner = -2*torch.matmul(x.transpose(2, 1), x)
    xx = torch.sum(x**2, dim=1, keepdim=True)
    pairwise_distance = -xx - inner - xx.transpose(2, 1)
 
    idx = pairwise_distance.topk(k=k, dim=-1)[1]   
    
    return idx

# copied from 
# https://github.com/WangYueFt/dgcnn/blob/master/pytorch/model.py
def get_graph_feature(x, k=20, idx=None):
    batch_size = x.size(0)
    num_points = x.size(2)
    x = x.view(batch_size, -1, num_points)
    if idx is None:
        idx = knn(x, k=k)   
    device = torch.device('cpu')

    idx_base = torch.arange(0, batch_size, device=device).view(-1, 1, 1)*num_points

    idx = idx + idx_base

    idx = idx.view(-1)
 
    _, num_dims, _ = x.size()

    x = x.transpose(2, 1).contiguous()   
    feature = x.view(batch_size*num_points, -1)[idx, :]
    feature = feature.view(batch_size, num_points, k, num_dims) 
    x = x.view(batch_size, num_points, 1, num_dims).repeat(1, 1, k, 1)
    
    feature = torch.cat((feature-x, x), dim=3).permute(0, 3, 1, 2).contiguous()
  
    return feature
