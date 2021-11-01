import os
import spacy
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

    # Part 5 :: Welche Links

    for f in allFiles:
        tree = ET.parse(f)
        root = tree.getroot()
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
    plt.show()




if __name__ == "__main__":
    completeAnalysis(r"TrainingData")