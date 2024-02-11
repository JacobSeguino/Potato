import random
import scores
from yamlReader import yamlReader
from rollADice import rollADice

yamlFile = "grassAndMud.yaml"


def inTheGarden():
    fate = random.randrange(2,7,2)
    # print(fate)
    print(yamlReader(yamlFile, fate))
    tableChoice(fate)


def tableChoice(fate):
    if fate == 2:
        rollADice("inTheGarden.yaml")
    if fate == 4:
        rollADice("aKnockAtTheDoor.yaml")
    if fate == 6:
        scores.potatoForOrc.score += 1
        print("it now takes "+str(scores.potatoForOrc.score)+ " potatoes to remove 1 Orc")
