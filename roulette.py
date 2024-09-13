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
        self.item_player = ['sac de poudre','monocle']
        self.gun = [0,0,0,0,0,0]
        self.gunDmg = 1
        self.txt = ""

    def reload(self):
        self.txt += "\nreloaded"
        self.gun[0] = 1
        random.shuffle(self.gun)
        self.animPlayer('combine2')
    
    def useItem(self, choice : int):
        if choice == 1:
            if "bag of powder" in self.item_player:
                self.gunDmg = 2
                self.txt += "\nThe next shot fired (live or not) deals double dmg !"
                self.item_player.remove("bag of powder")
            else:
                self.txt += "\nyou dont have this item !"
        elif choice == 2:
            if "monocle" in self.item_player:
                self.txt += f"\nthere is a {'live round' if self.gun[0] == 1 else 'no bullet'} in the barrel"
                self.item_player.remove("monocle")
            else:
                self.txt += "\nyou dont have this item !"
        else:
            self.txt += "\nthis is not an item !"
        self.render()
        


    def shoot(self,choice : str, isPlayer : bool):
        if 1 not in self.gun:
            self.reload()

        if self.gun[0] == 1:
            self.gun[0] = 0
            if choice == 'self':
                if isPlayer:
                    self.pvP -= self.gunDmg
                    self.animPlayer("placeholder 1")
                else:
                    self.pvD -= self.gunDmg
                    self.animPlayer("placeholder 2")
            else:
                if isPlayer:
                    self.pvD -= self.gunDmg
                    self.animPlayer('final')
                else:
                    self.pvP -= self.gunDmg
                    self.animPlayer('placeholder 3')

            self.txt += f"\npaw, {isPlayer}, {choice}"
        else:
            self.txt += f"\nclic, {isPlayer}, {choice}"
        
        if self.gunDmg != 1:
            self.gunDmg = 1

        for i in range(1,6):
            if self.gun[i] == 1:
                self.gun[i-1], self.gun[i] = self.gun[i], self.gun[i-1]

        if choice == "self":
            self.playerTurn = True if isPlayer else False
        else:
            self.playerTurn = False if isPlayer else True
        
        self.render()
    
    def animPlayer(self , anim_name : str):
        pass
        #animation_sys.anim(anim_name)

    def render(self,anim_index = 0):
        #animation_sys.clear_console()
        #UI -> text
        if not self.playerTurn:
            self.txt += '\nbot playing'
            self.botAi()
        else:
            self.txt += "\nplayer's turn"
        
        print(self.txt.strip())
        
        self.txt = ""
    
    def botAi(self):
        rng = random.randint(0,2)
        self.shoot('self' if rng == 1 else 'other', False)
        
game = Game()     
        
def shoot(choice):
    game.shoot(choice, True)
    return
def item(choice):
    game.useItem(choice)
    return

        


        


game.render(1)





