# game_rpg_simulation.py    written by Duncan Murray 30/3/2015

import sys
import os
import random
import aikif.cls_log as mod_log
import aikif.project as mod_prj


def main():
    """
    Prototype to see how an RPG simulation might be used
    in the AIKIF framework.
    The idea is to build a simple character and run a simulation
    to see how it succeeds in a random world against another players
    character
    character
        stats
    world
        locations
    
    """
    p = mod_prj.Project('RPG Simulation', 'Game', 'Testing character simulation in game', os.getcwd())
    
    character1 = Character('Albogh', str=4,int=7,sta=5)
    character2 = Character('Zoltor', str=6,int=3,sta=7)
    print(character1)
    b = Battle(character1, character2)
    print(b)
    
class Character():
    """
    Character class to manage how a character is built
    """
    def __init__(self, name, str=5, int=5, sta=5):
        self.name = name
        self.str = str
        self.int = int
        self.sta = sta
        self.status = 'Alive'
        self.exp = 0
        self.gold = 10
        self.backpack = ['torch', 'apple']

    def __str__(self):
        res = ''
        res += 'Character   : ' + self.name + '\n'
        res += 'Statistics  : STA=' + str(self.sta) + ', INT=' + str(self.int) + ', STR=' + str(self.str) + '\n'
        res += 'Status      : ' + self.status + '\n'
        res += 'Carrying    : ' 
        for i in self.backpack:
            res += i + ', '
        res += str(self.gold) + ' Gold'
        return res
        
class Battle():
    """
    manages a fight between 2 rpg characters
    """
    def __init__(self, char1, char2):
        self.c1 = char1
        self.c2 = char2
        self.status = 'Start...'
        self.fight()
    
    def __str__(self):
        res = 'Battle Status : ' + self.status + '\n'
        res += 'Character 1 =  ' + self.c1.name + '\n'
        res += 'Character 2 =  ' + self.c2.name + '\n'
        return res
        
    
    def fight(self, moves=10):
        """
        runs a series of fights
        """
        for i in range(1, moves):
            roll_1 = random.randint(2,200)
            roll_2 = random.randint(2,200)
            if roll_1 > roll_2:
                print(self.c1.name + ' hits ' + self.c2.name + ' for damage ' + str(roll_1))
            else:
                print(self.c2.name + ' hits ' + self.c1.name + ' for damage ' + str(roll_2))
            
        
        
main()