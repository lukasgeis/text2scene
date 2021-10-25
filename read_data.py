import spacy

nlp = spacy.load("en_core_web_sm")

path = r"trainings_data\training\Traning\RFC\Bicycles.xml"
file = open(path, "r", encoding="utf-8").read()
a = file.index("CDATA[")
b = file.index("]]>")
text = (file[a+6:b].replace("\n\n","\n").replace("â€™","'"))

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)