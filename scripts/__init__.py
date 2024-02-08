import scores
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
        textReader('orcGameOverMessage.txt')
        return True
    if scores.potatoes.score >= 10:
        textReader('potatoeGameOverMessage.txt')
        return True
    if scores.destiny.score >= 10:
        textReader('destinyGameOverMessage.txt')
        return True
    if scores.gameTime.score >= 10:
        return True
    return False

#prints out the score
def printScore():
    print(" ")
    print("~*~SCORE~*~")
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

def game():
    gameover = False

    while gameover == False:
        #sudo code to help test the game out will be removed in final game
        print("hit enter to roll, '2' to trade potatos to get rid of orcs, or 3 to quit")
        x = input()

        if x == '':
            inTheGarden()
        if x == '2':
            tradePotatoForOrc()
        if x == '3':
            gameover = True
            return
    
        scores.gameTime.score += 1
        printScore()
        gameover = isGameOver()



begining()
game()
