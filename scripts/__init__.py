import scores
import os
from grassAndMud import inTheGarden
from tradePotatoForOrc import tradePotatoForOrc


def begining():
    textReader('beginingText.txt')


def textReader(text):
    f = open('./resources/'+text, 'r')
    print(f.read())


# finds out if the game is over
def isGameOver():
    if scores.orcs.score >= 10:
        return gameOverReadOut('orcGameOverMessage.txt')
    if scores.potatoes.score >= 10:
        return gameOverReadOut('potatoeGameOverMessage.txt')
    if scores.destiny.score >= 10:
        return gameOverReadOut('destinyGameOverMessage.txt')
    return False


def gameOverReadOut(endGameYamlName):
    os.system('cls')
    textReader(endGameYamlName)
    printScore("~*~ FINAL SCORE ~*~")
    return True


# Prints out the score
def printScore(tital):
    print(" ")
    print(tital)
    print("Orcs: "+str(scores.orcs.score))
    print("Potatoes: "+str(scores.potatoes.score))
    print("Destiny: "+str(scores.destiny.score))
    print(" ")
    print("--metadata--")
    if int(scores.potatoForOrc.score) > 1:
        print("It cost " + str(scores.potatoForOrc.score) +
              " Potatoes to Remove 1 Orc")
    else:
        print("It cost " + str(scores.potatoForOrc.score) +
              " Potato to Remove 1 Orc")
    print("Game time: " + str(scores.gameTime.score))
    print("~*~*~*~")
    print(" ")
    print(" ")


def game():
    gameover = False

    while not gameover:
        if not scores.gameTime.score == 0:
            print("Hit 'enter' to continue, type 'trade' to trade "
                  + str(scores.potatoForOrc.score) +
                  " potato(es) to get rid of 1 orc, or type 'exit' to quit")
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
        gameover = isGameOver()
        if not gameover:
            printScore("~*~SCORE~*~")


begining()
game()
