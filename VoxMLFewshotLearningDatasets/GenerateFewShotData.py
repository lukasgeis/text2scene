import os
import pickle
import random
import argparse
import numpy as np
import xml.etree.ElementTree as ET

def classifyObjects(inpath: str, attribute: str, labelList: list) -> dict:
    if not os.path.exists(inpath):
        return {}
    
    result = {}
    for file in os.listdir(inpath):
        try:
            val = ET.parse(os.path.join(inpath, file)).getroot().findtext(attribute)
            if val not in result:
                result[val] = []
            result[val].append(labelList.index(file[:-4]))
        except Exception:
            print("ERROR while parsing " + str(file))

    return result

def generateFewshotData(way: int, shot: int, ind: int, labelDict: dict, train: str, test: str, outpath: str) -> None:
    with open(train, "rb") as f:
        trainPoints, trainLabels = pickle.load(f)
    with open(test, "rb") as f:
        testPoints, testLabels = pickle.load(f)

    trainDataset = []
    testDataset = []
    trainDict = {}
    testDict = {}

    for point, label in zip(trainPoints, trainLabels):
        label = label[0]
        if label not in trainDict:
            trainDict[label] = []
        trainDict[label].append(point)
    for point, label in zip(testPoints, testLabels):
        label = label[0]
        if label not in testDict:
            testDict[label] = []
        testDict[label].append(point)
    
    for i in range(way):
        key = random.choice(list(labelDict.keys()))
        for j in range(shot):
            data = random.choice(trainDict[random.choice(labelDict[key])])
            trainDataset.append((data, i, key))
        for j in range(20):
            data = random.choice(testDict[random.choice(labelDict[key])])
            testDataset.append((data, i, key))
    
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
    parser.add_argument("--train", metavar = "", help = "train.dat file", required = True)
    parser.add_argument("--test", metavar = "", help = "test.dat file", required = True)
    parser.add_argument("-o", "--output", metavar = "", help = "Outpath for Directories", required = True)
    parser.add_argument("-w", "--way", type = int, metavar = "", help = "way", required = True)
    parser.add_argument("-s", "--shot", type = int, metavar = "", help = "shot", required = True)

    args = parser.parse_args()
    labelList = ['airplane', 'bathtub', 'bed', 'bench', 'bookshelf', 'bottle', 'bowl', 'car', 'chair', 'cone', 'cup', 'curtain', 'desk', 'door', 'dresser', 'flower_pot', 'glass_box', 'guitar', 'keyboard', 'lamp', 'laptop', 'mantel', 'monitor', 'night_stand', 'person', 'piano', 'plant', 'radio', 'range_hood', 'sink', 'sofa', 'stairs', 'stool', 'table', 'tent', 'toilet', 'tv_stand', 'vase', 'wardrobe', 'xbox']
    rawLabels = classifyObjects(args.voxml, args.attribute, labelList)
    
    for ind in range(10):
        generateFewshotData(args.way, args.shot, ind, rawLabels, args.train, args.test, args.output)
        print(f"Finished dataset {ind}!")

if __name__ == "__main__":
    main()