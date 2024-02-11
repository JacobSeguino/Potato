import scores
import random
from yamlReader import *

def rollADice(yamlFile):
    fate = random.randrange(1,7,1)
    # print("fate is: "+str(fate))
    yamlList = yamlReader(yamlFile, fate)
    listParser(yamlList)


def dictionaryParser(val,yamlList):
    for key in yamlList[val]:
        print(str(key) + " changes by "+str(yamlList[val][key]))

def potatoChecker(val):
    if val == -1 and not int(scores.potatoes.score) == 0:
        scores.potatoes.score = scores.potatoes.score - 1
        return
    if val == -1 and int(scores.potatoes.score) == 0:
        return
    scores.potatoes.score = scores.potatoes.score + val

def changeScore(val,yamlList):
    for key in yamlList[val]:
        if str(key) == "potato":
            potatoChecker(yamlList[val][key])
        if str(key) == "orc":
            scores.orcs.score = scores.orcs.score + yamlList[val][key]
        if str(key) == "destiny":
            scores.destiny.score = scores.destiny.score+ yamlList[val][key]

def listParser(yamlList):
    for i in range(len(yamlList)):
        if i == 0 :
            print(yamlList[i])
            print(" ")
        if i >= 1:
            dictionaryParser(i,yamlList)
            changeScore(i,yamlList)
