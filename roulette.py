import random
from time import sleep
import os
import animation_sys

class Game:
    def __init__(self) -> None:
        self.playerTurn = True
        self.pvP = 3
        self.pvD = 3
        self.item_player = ['bag of powder','monocle']
        self.item_mafioso = ['bag of powder','monocle']
        self.item1, self.item2 = True, True
        self.item1M, self.item2M = True, True
        self.gun = [0,0,0,0,0,0]
        self.gunDmg = 1
        self.txt = ""

    def reload(self, isPlayer : bool):
        self.gun[0] = 1
        random.shuffle(self.gun)
        if isPlayer:
            animation_sys.anim('reload')
            self.txt += "\033[94mYou reloaded the gun"
            self.cycle_manager()
        else:
            self.txt += "\033[31mThe mafioso reloaded the gun"
            self.cycle_manager()

    def useItem(self, choice : int):
        if choice == 1:
            if "bag of powder" in self.item_player:
                self.gunDmg = 2
                self.txt += "\033[94mThe next shot fired (live or not) deals double dmg !"
                self.item_player.remove("bag of powder")
                self.item1 = False
            else:
                self.txt += "\033[94myou dont have this item !"
        elif choice == 2:
            if "monocle" in self.item_player:
                self.txt += f"\033[94mthere is a {'live round' if self.gun[0] == 1 else 'no bullet'} in the barrel"
                self.item_player.remove("monocle")
                self.item2 = False
            else:
                self.txt += "\033[94myou dont have this item !"
        else:
            self.txt += "\033[94mthis is not an item !"
        self.cycle_manager()
        


    def shoot(self,choice : str, isPlayer : bool):
        if 1 not in self.gun:
            self.txt += "\033[94mUse reload() to reload the gun"
            self.cycle_manager()
            return

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
        
        self.cycle_manager()
    
    def render_ui(self):
        animation_sys.clear_console()
        ui = animation_sys.get_ui(pvP=self.pvP,pvD=self.pvD,logTxt=self.txt.strip(),item1=self.item1, item2=self.item2, item1M=self.item1M, item2M = self.item2M)
        print(ui)
        self.txt = ""
        

    def cycle_manager(self):
        self.render_ui()
        if not self.playerTurn:
            txt += "\033[31mMafioso is playing"
            self.render_ui()
            self.botAi()
    
    def botAi(self):
        sleep(4)
        rng = random.randint(0,2)
        rng2 = random.randint(0,3)

        if 1 not in self.gun:
            self.reload(False)
            return

        if rng2 == 0:
            if 'bag of powder' in self.item_mafioso:
                self.gunDmg = 2
                self.txt += "\033[31mMafioso used bag of powder"
                self.item_mafioso.remove('bag of powder')
                self.item1M = False

                self.render_ui()
                sleep(3)

                self.shoot('other', False)
                return
        elif rng2 == 1:
            if 'monocle' in self.item_mafioso:
                self.txt += "\033[31mMafioso used monocle"
                self.item_mafioso.remove('monocle')
                self.item2M = False
                if self.gun[0] == 1:
                    self.shoot('other', False)
                else:
                    self.shoot('self', False)
                return

        self.shoot('self' if rng == 1 else 'other', False)
        return

        
game = Game()     
        
def shoot(choice):
    game.shoot(choice, True)
    return
def item(choice):
    game.useItem(choice)
    return
def reload():
    game.reload(True) 


        

animation_sys.anim("intro")
game.cycle_manager()





