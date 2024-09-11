import random
import csv
from time import sleep
import os
import animation_sys


class Game:
    def __init__(self) -> None:
        self.playerTurn = True
        self.pvP = 3
        self.pvD = 3
        self.gun = [0,0,0,0,0,0]
        self.gunDmg = 1

    def reload(self):
        print('reloading')
        self.gun[0] = 1
        random.shuffle(self.gun)
    
    def useItem(self):
        pass

    def shoot(self,choice : str, isPlayer : bool):
        if 1 not in self.gun:
            self.reload()

        if self.gun[0] == 1:
            self.gun[0] = 0
            if choice == 'self':
                if isPlayer:
                    self.pvP -= self.gunDmg
                else:
                    self.pvD -= self.gunDmg
            else:
                if isPlayer:
                    self.pvD -= self.gunDmg
                else:
                    self.pvP -= self.gunDmg
            print('paw', isPlayer, choice)
        else:
            print('clic', isPlayer,choice)
        
        if self.gunDmg != 1:
            self.gunDmg = 1

        for i in range(1,6):
            if self.gun[i] == 1:
                self.gun[i-1], self.gun[i] = self.gun[i], self.gun[i-1]
        
        print(self.gun)

        if choice == "self":
            self.playerTurn = True if isPlayer else False
        else:
            self.playerTurn = False if isPlayer else True
        
        self.render()

    def render(self,anim_index = 0):
#        for x in range(30):
 #           os.system('cls')
  #          print(anim_index)
   #         sleep(0.1)

        if not self.playerTurn:
            self.botAi()
    
    def botAi(self):
        rng = random.randint(0,1)
        self.shoot('self' if rng == 1 else 'other', False)
        
game = Game()     
        
def shoot(choice):
    game.shoot(choice, True)
    return
def item(choice):
    game.useItem(choice)
    return

        


        


game.render(1)





