import scores
import os
from grassAndMud import inTheGarden
from tradePotatoForOrc import tradePotatoForOrc

def begining():
    textReader('beginingText.txt')

def textReader(text):
    f = open('./resources/'+text, 'r')
    print(f.read())

#finds out if the game is over
def isGameOver():
    if scores.orcs.score >= 10:
        os.system('cls')
        textReader('orcGameOverMessage.txt')
        finalScore()
        return True
    if scores.potatoes.score >= 10:
        os.system('cls')
        textReader('potatoeGameOverMessage.txt')
        finalScore()
        return True
    if scores.destiny.score >= 10:
        os.system('cls')
        textReader('destinyGameOverMessage.txt')
        finalScore()
        return True
    return False

#prints out the score
def printScore(tital):
    print(" ")
    print(tital)
    print("Orcs: "+str(scores.orcs.score))
    print("Potatoes: "+str(scores.potatoes.score))
    print("Destiny: "+str(scores.destiny.score))
    print(" ")
    print("--metadata--")
    if int(scores.potatoForOrc.score) > 1:
        print("Potatoes to Remove an Orc: "+str(scores.potatoForOrc.score))
    else:
        print("Potato to Remove an Orc: "+str(scores.potatoForOrc.score))
    print("Game time: " + str(scores.gameTime.score))
    print("~*~*~*~")
    print(" ")
    print(" ")

def finalScore():
    print(" ")
    printScore("~*~ FINAL SCORE ~*~")

def game():
    gameover = False

    while gameover == False:
        #sudo code to help test the game out will be removed in final game
        if not scores.gameTime.score == 0:
            print("Hit 'enter' to roll, type 'trade' to trade "+ str(scores.potatoForOrc.score) +" potatos to get rid of orcs, or type 'exit' to quit")
        x = input()
        os.system('cls')

        if x == '':
            inTheGarden()
        if x == 'trade':

            tradePotatoForOrc()
        if x == 'exit':
            gameover = True
            return

        scores.gameTime.score += 1
        printScore("~*~SCORE~*~")
        gameover = isGameOver()



begining()
game()
