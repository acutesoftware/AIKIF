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
    
    character1 = Character('Albogh', str=4,int=7,sta=50)
    character2 = Character('Zoltor', str=6,int=6,sta=70)
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
        res  = 'Battle Status : ' + self.status + '\n'
        res += 'Character 1 =  ' + self.c1.name + '\n'
        res += 'Character 2 =  ' + self.c2.name + '\n'
        return res
        
    
    def fight(self, moves=10):
        """
        runs a series of fights
        """
        for i in range(1, moves):
            # player 1
            result, dmg = self.calc_move(self.c1, self.c2)
            print (self.c1.name + ' ' + result + ' for ' + str(dmg))
            self.c1.sta = self.c1.sta - dmg
            if self.is_character_dead(self.c1):
                print(self.c1.name + ' has died')
                exit(0)
            # player 2
            result, dmg = self.calc_move(self.c2, self.c1)
            print (self.c2.name + ' ' + result + ' for ' + str(dmg))
            self.c2.sta = self.c2.sta - dmg
            if self.is_character_dead(self.c2):
                print(self.c2.name + ' has died')
                exit(0)
            
    def calc_move(self, c1, c2):
        chance_hit = random.randint(2,c1.int)
        amount_dmg = random.randint(2,c1.str+3) * (c1.int/2)
       # print('chance_hit  =',chance_hit  , 'amount_dmg = ',amount_dmg  )
        if chance_hit > 6:
            return 'Crit', amount_dmg
        elif chance_hit < 3:
            return 'Miss', 0
        else:
            return 'Hit', amount_dmg
            
    def is_character_dead(self, c):
        """
        check to see if a character is dead
        """
        if c.sta < 1:
            return True
        else:
            return False
main()