# Imports
import os
import pickle
import random
import argparse
import numpy as np
import xml.etree.ElementTree as ET

def classifyObjects(inpath: str, attribute: str) -> dict:
    if not os.path.exists(inpath):
        return {}
    
    result = {}
    for file in os.listdir(inpath):
        try:
            val = ET.parse(os.path.join(inpath, file)).getroot().findtext(attribute)
            if val not in result:
                result[val] = []
            result[val].append(file[:-4])
        except Exception:
            print("ERROR while parsing " + str(file))

    return result

def generateFewshotData(way: int, shot: int, ind: int, labelDict: dict, inpath: str, outpath: str) -> None:
    trainDataset = []
    testDataset = []

    objects = os.listdir(inpath)

    for i in range(way):
        key = random.choice(list(labelDict.keys()))
        for j in range(shot):
            trainObj = None
            while trainObj not in objects:
                trainObj = random.choice(labelDict[key])
            trainObjPath = os.path.join(inpath, trainObj, "train")
            trainObjData = [[float(y) for y in x.replace("\n", "").split(" ") if y != ""] for x in open(os.path.join(trainObjPath, random.choice(os.listdir(trainObjPath))), "r").readlines()[1:]]
            trainData = np.ndarray(shape = (len(trainObjData), 3), dtype = float)
            for k in range(len(trainObjData)):
                for l in range(min(3,len(trainObjData[i]))):
                    trainData[k][l] = trainObjData[k][l]
            trainDataset.append((trainData, i, key))
        for j in range(20):
            testObj = None
            while testObj not in objects:
                testObj = random.choice(labelDict[key])
            testObjPath = os.path.join(inpath, testObj, "test")
            testObjData = [[float(y) for y in x.replace("\n", "").split(" ") if y != ""] for x in open(os.path.join(testObjPath, random.choice(os.listdir(testObjPath))), "r").readlines()[1:]]
            testData = np.ndarray(shape = (len(testObjData), 3), dtype = float)
            for k in range(len(testObjData)):
                for l in range(min(3,len(testObjData[i]))):
                    testData[k][l] = testObjData[k][l]
            testDataset.append((testData, i, key))

    random.shuffle(trainDataset)
    random.shuffle(testDataset)
    dataset = {
        "train": trainDataset,
        "test": testDataset
    }

    fullOutpath = os.path.join(outpath, f"{way}way_{shot}shot")
    if not os.path.exists(fullOutpath):
        os.makedirs(fullOutpath)
    with open(os.path.join(fullOutpath, f"{ind}.pkl"), "wb") as f:
        pickle.dump(dataset, f)

            

def main():
    parser = argparse.ArgumentParser(description = "Create FewshotLearning Dataset for VoxML Attributes")
    parser.add_argument("attribute", help = "VoxML Attribute")
    parser.add_argument("-v", "--voxml", metavar = "", help = "Directory of VoxML files", required = True)
    parser.add_argument("-d", "--dataset", metavar = "", help = "Directory of all 3D-Objects (see README.md for more information)", required = True)
    parser.add_argument("-o", "--output", metavar = "", help = "Outpath for Directories", required = True)

    args = parser.parse_args()
    rawLabels = classifyObjects(args.voxml, args.attribute)

    for way in [5,10]:
        for shot in [10,20]:
            for ind in range(10):
                generateFewshotData(way, shot, ind, rawLabels, args.dataset, args.output)
                print("Finished dataset => way: " + str(way) + ", shot: " + str(shot) + ", ind: " + str(ind))


if __name__ == "__main__":
    main()