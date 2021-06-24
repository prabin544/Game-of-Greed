import random
import collections
import random
import math
import sys

class GameLogic:
    def __init__ (self, dice_roll, free_dice):
        self.dice_roll = dice_roll
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

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        pairs = 0
        c = collections.Counter(dice_roll)

        # three_ones_and_a_five
        for i in c:
            if c[1] == 3 and c[5] == 1:
                score += 1050
                return score

        # six_ones
        for k, v in c.items():
            if c[1] == 6:
                score += 4000
                return score

        # three_fives
        for k, v in c.items():
            if k == 5 and v == 3:
                score += 500
                return score

        # three_ones
        for k, v in c.items():
            if k == 1 and v == 3:
                score += 1000
                return score

        # Handles straights
        if len(c) == 6:
            score += 1500
            return score

        # three_of_a_kind
        for k, v in c.items():
            if v == 3:
                score += 200
                return score

        # four_of_a_kind
        for k, v in c.items():
            if v == 4:
                score += 400
                return score

        # five_of_a_kind
        for k, v in c.items():
            if v == 5:
                score += 600
                return score

        # six_of_a_kind
        for k, v in c.items():
            if v == 6:
                score += 800
                return score

        # one_and_five
        if c[1] == 1 and c[5] == 1:
            score += 150
            return score

        # single_five
        if c[5] == 1:
            score += 50
            return score

        # single_one
        if c[1] == 1:
            score += 100
            return score

        # two_fives
        if c[5] == 2:
            score += 100
            return score

        # two_ones
        if c[1] == 2:
            score += 200
            return score

        # zilch
        if c[2] == 1:
            score += 0
            return score


class Banker:
    pass

