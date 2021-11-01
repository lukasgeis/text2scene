import os
import spacy
import xml.etree.ElementTree as ET

def completeAnalysis(inpath):
    nlp = spacy.load("en_core_web_sm")
    allFiles = []
    for directory in os.listdir(inpath):
        pass
    print(len(file))






if __name__ == "__main__":
    completeAnalysis(r"TrainingData")