import random
import csv
from time import sleep
import os


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

    def shootPlayer(self,choice : str):
        if 1 not in self.gun:
            self.reload()
        if self.gun[0] == 1:
            self.gun[0] = 0
            print('paw')
        else:
            print('clic')

        for i in range(1,6):
            if self.gun[i] == 1:
                self.gun[i-1], self.gun[i] = self.gun[i], self.gun[i-1]
        
        print(self.gun)

        if choice == "self":
            self.render()
        else:
            self.playerTurn = False
            self.render()

    def render(self,anim_index = 0):
        print('player turn \n dwqdqwdq \n dqwjbdqwjdb')
        i = 1
        while True:
            os.system('cls')
            print(i)
            i+=1
            sleep(0.1)

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





