import random
from yamlReader import yamlReader

yamlFile = "grassAndMud.yaml"

def inTheGarden():
    fate = random.randrange(2,7,2)
    print(fate)
    print(yamlReader(yamlFile, fate))
    tableChoice(fate)

def tableChoice(fate):
    if fate == 2:
        print("option 2")
    if fate == 4:
        print("option 4")
    if fate == 6:
        print("option 6")



inTheGarden()