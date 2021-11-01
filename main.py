import os
import spacy
import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def completeAnalysis(inpath):
    print()
    print("Analyse von IsoSpace-Daten")
    print("==========================")
    print()

    nlp = spacy.load("en_core_web_sm")
    allFiles = []
    for d in [os.path.join(inpath,x) for x in os.listdir(inpath) if os.path.isdir(os.path.join(inpath,x))]:
        for f in [x for x in os.listdir(d) if ".xml" in x]:
            allFiles.append(os.path.join(d,f))

    print("<=: " + str(len(allFiles)) + " Dateien geladen :=>")
    print()

    # Part 1 :: Wie oft kommen welche PoS-Tags vor?
    table1 = ["ADJ","ADP","AUX","CONJ","CCONJ","DET","INTJ","NOUN","NUM","PART","PRON","PROPN","PUNCT","SCONJ","SYM","VERB","X","EOL","SPACE"]
    res1 = [0 for k in table1]

    # Part 2 :: Wie viele [SpatialEntities, Places, Motions, Locations, Signals, QsLinks, OLinks] gibt es?
    table2 = ["SPATIAL_ENTITY","PLACE","MOTION","SPATIAL_SIGNAL","MOTION_SIGNAL","QSLINK","OLINK"]
    res2 = [0 for k in table2]

    # Part 3 :: Wie oft kommen welche QsLink Typen vor?
    table3 = ["IN","OUT","DC","EC","PO","TPP","ITPP","NTPP","INTPP","EQ"]
    res3 = [0 for k in table3]

    # Part 4 :: Verteilung der Satzlänge graphisch darstellen (x: Satzlänge, y: Wie häufig)?
    y = []

    # Part 5 :: Welche Links (QSLinks, OLinks) werden von welchen Präpositionen (markiert durch SPATIAL_SIGNAL) getriggert (z.B. wie oft werden QSLinks durch die Präposition „on“ getriggert)?
    qsLinks = []
    oLinks = []
    res5 = [{},{}]

    # Part 6 :: Welches sind die fünf häufigsten "MOTION" Verben (und wie oft kommen diese vor)?
    res6 = {}

    for f in allFiles:
        root = ET.parse(f).getroot()
        
        # Part 1
        for c in root.iter("TEXT"):
            # Part 1
            for token in nlp(c.text):
                if token.pos_ in table1:
                    res1[table1.index(token.pos_)] += 1
        # Part 2
        for c in root.iter():
            if c.tag in table2:
                res2[table2.index(c.tag)] += 1
        # Part 3
        for c in root.findall("TAGS/QSLINK"):
            if c.get("relType") in table3:
                res3[table3.index(c.get("relType"))] += 1
        # Part 4
        for c in root.iter("TEXT"):
            for s in nlp(c.text).sents:
                sLen = len(str(s).split())
                if len(y) - 1 < sLen:
                    y += [0 for k in range(len(y) - 1,sLen)]
                y[sLen] += 1
        # Part 5
        for c in root.findall("TAGS/SPATIAL_SIGNAL"):
            for cqs in root.findall("TAGS/QSLINK"):
                if cqs.get("trigger") == c.get("id"):
                    qsLinks.append(c.get("text"))
            for co in root.findall("TAGS/OLINK"):
                if co.get("trigger") == c.get("id"):
                    oLinks.append(c.get("text"))
        # Part 6
        for c in root.findall("TAGS/MOTION"):
            if c.get("text") not in res6:
                res6[c.get("text")] = 0
            res6[c.get("text")] += 1
        
    
    # Part 1
    print("Wie oft kommen welche PoS-Tags vor?")
    for k in range(len(table1)):
        print(table1[k] + ": " + str(res1[k]))
    print()

    # Part 2
    print("Wie viele [SpatialEntities, Places, Motions, Locations, Signals, QsLinks, OLinks] gibt es?")
    table2 = ["SPATIAL_ENTITY","PLACE","MOTION","SIGNAL","QSLINK","OLINK"] 
    res2 = res2[:3] + [res2[3] + res2[4]] + res2[5:]
    for k in range(len(table2)):
        print(table2[k] + ": " + str(res2[k]))
    print()

    # Part 3
    print("Wie oft kommen welche QsLink Typen vor?")
    for k in range(len(table3)):
        print(table3[k] + ": " + str(res3[k]))
    print()

    # Part 4
    x = [k for k in range(len(y))]
    plt.xlabel("Satzlänge")
    plt.ylabel("Häufigkeit")
    plt.bar(x[1:],y[1:])

    # Part 5
    for w in qsLinks:
        if w not in res5[0]:
            res5[0][w] = 0
        res5[0][w] += 1
    for w in oLinks:
        if w not in res5[1]:
            res5[1][w] = 0
        res5[1][w] += 1
    print("QsLinks werden getriggert durch: ")
    for k in res5[0]:
        print(str(k) + ": " + str(res5[0][k]))
    print()
    print("OLinks werden getriggert durch: ")
    for k in res5[1]:
        print(str(k) + ": " + str(res5[1][k]))
    print()

    # Part 6
    print("Die fünf häufigsten MOTION-Verben sind:")
    for k in sorted(res6, key=res6.get, reverse=True)[:5]:
        print(str(k) + ": " + str(res6[k]))

    plt.show()



def visualizeText(inpath):
    graph = nx.Graph()
    nodes = [[],[]]
    edges = []
    metas = []

    root = ET.parse(inpath).getroot()
    for c in root.findall("TAGS/"):
        if c.tag in ["QSLINK","OLINK"]:
            edges.append((c.tag, c.attrib["relType"], c.attrib["fromID"], c.attrib["toID"]))
        if c.tag in ["SPATIAL_ENTITY","PLACE","LOCATION","NONMOTIONEVENT","PATH"]:
            nodes[0].append((c.tag, [c.attrib["id"]], [c.attrib["text"]]))
        if c.tag == "METALINK" and c.attrib["relType"] == "COREFERENCE":
            metas.append((c.attrib["objectID1"], c.attrib["objectID2"]))
    
    nodes[1].append(nodes[0][0])
    for node in nodes[0][1:]:
        check = True
        for k in range(len(nodes[1])):
            if node[1][0] in nodes[1][k][1]:
                break
            else:
                for link in metas:
                    if (node[1][0] == link[0] and link[1] in nodes[1][k][1]) or (node[1][0] == link[1] and link[0] in nodes[1][k][1]):
                        nodes[1][k][1].append(node[1][0])
                        if node[2][0] not in nodes[1][k][2]:
                            nodes[1][k][2].append(node[2][0])
                        check = False
                        break
            if not check:
                break
        if check:
            nodes[1].append(node)

    colorTable = {"SPATIAL_ENTITY":"red","PLACE":"blue","LOCATION":"green","NONMOTIONEVENT":"yellow","PATH":"black"}
    allLabels = [{},{}]
    colors = []
    for node in nodes[1]:
        graph.add_node(node[1][0])
        allLabels[0][node[1][0]] = ",".join(node[2])
        colors.append(colorTable[node[0]])
    
    for edge in edges:
        if edge[2] in graph.nodes() and edge[3] in graph.nodes():
            graph.add_edge(edge[2], edge[3])
            allLabels[1][(edge[2], edge[3])] = edge[1]
    
    pos = nx.spring_layout(graph, k=0.5, iterations=20)
    plt.figure()

    nx.draw_networkx(graph, pos, node_color=colors, labels=allLabels[0], with_labels=True, font_size=10, alpha=0.5)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=allLabels[1], font_color="red")

    plt.show()


def run23():
    completeAnalysis(r"TrainingData")

def run24I():
    visualizeText(r"TrainingData\RFC\Bicycles.xml") 

def run24II():
    visualizeText(r"TrainingData\ANC\WhereToMadrid\Highlights_of_the_Prado_Museum.xml") 

if __name__ == "__main__":
    # Aufgabe 2.3 
    # completeAnalysis(r"TrainingData")

    # Aufgabe 2.4 :: run24I || run24II
    # run24I()
    # run24II()