
orcOver = '''  
  Orcs finally find your potato farm. 
  Alas, orcs are not so intersted in potatoes 
  as they are in eating you, and you end up in a cookpot
  
  Game Over
  '''

potatoeOver = '''  
  You have enough potatoes that you can go underground 
  and not return to the surface until the danger is past. 
  You nestle down into your burrow and enjoy your 
  well earned rest
  
  Game Over
  '''

def game():
    destiny = 0
    potatoes = 0
    orcs = 0
    gameover = False

    while gameover == False:
        print("enter a number!")
        x = input()
        potatoes += 1
        orcs += int(x)
        print("Orcs: "+str(orcs))
        print("Potatoes: "+str(potatoes))
        if orcs >= 10:
            gameover = True
            print(orcOver)
            return
        if potatoes >= 5:
            gameover = True
            print(potatoeOver)
            return
        

game()
