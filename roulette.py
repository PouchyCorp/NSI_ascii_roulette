import random
from time import sleep
import os
import animation_sys

class Game:
    def __init__(self) -> None:
        self.playerTurn = True
        self.pvP = 3
        self.pvD = 1
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
                self.txt += "\033[94mThe next shot fired (live or not) deals double damage"
                self.item_player.remove("bag of powder")
                self.item1 = False
            else:
                self.txt += "\033[94mYou dont have this item"
        elif choice == 2:
            if "monocle" in self.item_player:
                self.txt += f"\033[94mThere is a {'live round' if self.gun[0] == 1 else 'no bullet'} in the barrel"
                self.item_player.remove("monocle")
                self.item2 = False
            else:
                self.txt += "\033[94mYou dont have this item"
        else:
            self.txt += "\033[94mThis is not an item"
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
                    self.txt += f"\033[94mYou shoot yourself for {self.gunDmg} damage"
                    animation_sys.anim("animselfshoot")
                else:
                    self.pvD -= self.gunDmg
                    self.txt += f"\033[31mThe Mafioso shoots himself for {self.gunDmg} damage"
                    animation_sys.anim("animbotshoot")
            else:
                if isPlayer:
                    self.pvD -= self.gunDmg
                    animation_sys.anim('animselfshootbot')
                    self.txt += f"\033[94mYou shoot the Mafioso for {self.gunDmg} damage"
                else:
                    self.pvP -= self.gunDmg
                    animation_sys.anim('animbotshootself')
                    self.txt += f"\033[31mThe Mafioso shoots you for {self.gunDmg} damage"
        else:
            if choice == 'self':
                if isPlayer:
                    animation_sys.anim("animselfpassiv")
                    self.txt += f"\033[94mYou shoot yourself, but nothing happened"
                else:
                    animation_sys.anim("animbotpassiv")
                    self.txt += f"\033[31mThe Mafioso shoots himself, but nothing happened"
            else:
                if isPlayer:
                    animation_sys.anim('animselfpassivbot')
                    self.txt += f"\033[94mYou shoot theyourself, but nothing happened"
                else:
                    animation_sys.anim('animbotpassivself')
                    self.txt += f"\033[31mThe Mafioso shoots you, but nothing happened.\033[94mYour turn"
        
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
        if self.pvP == 0:
            animation_sys.clear_console()
            print(animation_sys.GAME_OVER)
            return
        if self.pvD == 0:
            animation_sys.clear_console()
            print(animation_sys.VIVTORY)
            return

        if self.playerTurn:
            if not self.txt: self.txt += "\033[94mYour turn"

        self.render_ui()

        if not self.playerTurn:
            if not self.txt: self.txt += "\033[31mMafioso is playing"
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
    """Tire sur sois-meme, ou sur un ennemi.
    Si vous tirez sur vous-meme, vous pouvez rejouer.
    >>>shoot('self')
    vous tirez sur vous-meme
    >>>shoot('other')
    vous tirez sur le mafieux
    """
    game.shoot(choice, True)
    return

def item(choice):
    """Choisissez un item entre item(1) : 'sac de poudre', qui augmente les dégâts du prochain coup à 2, 
        ou bien item(2) : 'monocle', qui permet de savoir si le prochain coup est chargé ou non.
        /!\ utilisable une seule fois par partie"""
    game.useItem(choice)
    return

def reload():
    """Pour recharger l'arme après qu'un coup soit parti ou bien au début de la partie, utilisez -> reload()."""

    game.reload(True) 


print("""
        Roulette Sicilienne, est un jeu de stratégie en 1 vs 1.
        En face de vous le "mafioso" votre énemie. Devant vous un pistolet chargé d'une seule balle : le but, ne pas mourir à tour de rôle.

        reload() : recharge le pistolet si une balle est utilisé ou bien si c'est le début de la partie
        shoot('self') : se tirer dessus au risque de mourir mais de pouvoir rejouer
        shoot('other') : tirer sur le 'mafioso'
        item(1) : utiliser 'sac de poudre' double les dégats du prochain coup
        item(2) : utiliser 'monocle' et connaitre le contenue de la prochaine chambre dans le barillet

        Si une question vous vient en jouant utilsé help('fonction de votre choix')
        
        Faites start() pour commencer.
        """)


def start():
    animation_sys.anim("intro")
    game.cycle_manager()





