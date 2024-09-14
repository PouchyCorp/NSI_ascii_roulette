import random
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

    def reload(self, isPlayer : bool):
        self.txt += "\033[0mreloaded "
        self.gun[0] = 1
        random.shuffle(self.gun)
        if isPlayer:
            animation_sys.anim('reload')
            self.txt += "\033[94mYou reloaded the gun"
            self.render()
        else:
            self.txt += "\033[31mThe mafioso reloaded the gun"
            self.render()
    
    def useItem(self, choice : int):
        if choice == 1:
            if "bag of powder" in self.item_player:
                self.gunDmg = 2
                self.txt += "\033[94mThe next shot fired (live or not) deals double dmg !"
                self.item_player.remove("bag of powder")
            else:
                self.txt += "\033[94myou dont have this item !"
        elif choice == 2:
            if "monocle" in self.item_player:
                self.txt += f"\033[94mthere is a {'live round' if self.gun[0] == 1 else 'no bullet'} in the barrel"
                self.item_player.remove("monocle")
            else:
                self.txt += "\033[94myou dont have this item !"
        else:
            self.txt += "\033[94mthis is not an item !"
        self.render()
        


    def shoot(self,choice : str, isPlayer : bool):
        if 1 not in self.gun:
            self.txt += "\033[94mUse reload() to reload the gun"

        if self.gun[0] == 1:
            self.gun[0] = 0
            if choice == 'self':
                if isPlayer:
                    self.pvP -= self.gunDmg
                    animation_sys.anim("animselfshoot")
                else:
                    self.pvD -= self.gunDmg
                    animation_sys.anim("animbotshoot")
            else:
                if isPlayer:
                    self.pvD -= self.gunDmg
                    animation_sys.anim('animselfshootbot')
                else:
                    self.pvP -= self.gunDmg
                    animation_sys.anim('animbotshootself')

            self.txt += f"paw, {isPlayer}, {choice}"
        else:
            if choice == 'self':
                if isPlayer:
                    animation_sys.anim("animselfpassiv")
                else:
                    animation_sys.anim("animbotpassiv")
            else:
                if isPlayer:
                    animation_sys.anim('animselfpassivbot')
                else:
                    animation_sys.anim('animbotpassivself')
        
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

    def render(self,anim_index = 0):
        animation_sys.clear_console()
        #animation_sys.clear_console()
        #UI -> text
        #if not self.playerTurn:
        #    self.txt += '\033[31mmafioso playing'
        #else:
        #    self.txt += "\033[94mplayer's turn"
        
        ui = animation_sys.get_ui(pvP=self.pvP,pvD=self.pvD,logTxt=self.txt.strip())
        print(ui)

        if not self.playerTurn:
            self.botAi()
        
        self.txt = ""
    
    def botAi(self):
        sleep(4)
        rng = random.randint(0,2)
        if 1 not in self.gun:
            self.reload(False)
        self.shoot('self' if rng == 1 else 'other', False)

        
game = Game()     
        
def shoot(choice):
    game.shoot(choice, True)
    return
def item(choice):
    game.useItem(choice)
    return
def reload():
    game.reload(True)

        


        


game.render(1)





