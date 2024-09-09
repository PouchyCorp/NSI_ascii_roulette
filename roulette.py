import random
import csv


class Game:
    def __init__(self) -> None:
        self.playerTurn = True
        self.pvP = 3
        self.pvD = 3
        self.gun = [0,0,0,0,0,0]

    def reload(self):
        print('reloading')
        self.gun[0] = 1
        random.shuffle(self.gun)
        print(self.gun)

    def shootPlayer(self,choice : str):
        if 1 not in self.gun:
            self.reload()
        if self.gun[0] == 1:
            print('paw')
        else:
            print('clic')

        if choice == "self":
            self.render()
        else:
            self.playerTurn = False
            self.render()

    def render(self,anim_index):
        print('player turn')
        #render pipeline
        if not self.playerTurn:
            #bot ai
            print("bot played")
            self.playerTurn = True
            self.render()
        
game = Game()     
        
def shoot(choice):
    game.shootPlayer(choice)
        


        


game.render(1)





