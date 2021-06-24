import random

class GameLogic:
    def __init__ (self, free_dice):
        self.free_dice = free_dice
       
    
    @staticmethod
    def roll_dice(free_dice):
        if free_dice == None:
            free_dice = free_dice
        if free_dice == 0:
            return()
        roll = tuple(random.randint(1, 6) for i in range(free_dice))
        print('You rolled a ' + str(roll))
        return roll