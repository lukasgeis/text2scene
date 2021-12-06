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
