import random
import collections
from collections import Counter
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
        # print('You rolled a ' + str(roll))
        return roll

    @staticmethod
    def get_scorers(dice_roll):
        print(f' Test input is {dice_roll}')
        keepers = ()
        for dice in dice_roll:
            if 1 in dice_roll and 5 in dice_roll:
                keepers = (1, 5)
            elif 1 in dice_roll:
                keepers = (1,)
            elif 5 in dice_roll:
                keepers = (5,)
            else:
                keepers = ()
        return keepers

    @staticmethod
    def validate_keepers(roll, keepers):
        # version_3

        return not Counter(keepers) - Counter(roll)

    # def validate_keepers(roll, keepers):
    #     roll_counter = collections.Counter(roll)
    #     keepers_counter = collections.Counter(keepers)
    #     return len(keepers_counter - roll_counter) == 0

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent the user's selected dice pulled out from current roll
        """
        # version_1

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = collections.Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3

                # bug if 2 threesomes? Let's test it

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score



    # @staticmethod
    # def calculate_score(dice_roll):
    #     score = 0
    #     pairs = 0
    #     c = collections.Counter(dice_roll)

    #     # # one and five
    #     # for i in c:
    #     #     if c[1] == 1 and c[5] == 1:
    #     #         score += 200000
    #     #         return score
    #     # two ones
    #     for k, v in c.items():
    #         if k == 1 and v == 2:
    #             score += 200
    #             return score

    #     for k, v in c.items():
    #         score = 0
    #         if k == 3 and v == 2:
    #             score += 500
    #             return score
    #         if k == 1 and v == 2:
    #             score += 500
    #         if k == 2 and v == 2:
    #             score += 500
            

    #     # three_ones_and_a_five
    #     for i in c:
    #         if c[1] == 3 and c[5] == 1:
    #             score += 1050
    #             return score

    #     # three_three_and_a_five
    #     for i in c:
    #         if c[3] == 3 and c[5] == 1:
    #             score += 350
    #             return score

    #     # six_ones
    #     for k, v in c.items():
    #         if c[1] == 6:
    #             score += 4000
    #             return score

    #     # three_fives
    #     for k, v in c.items():
    #         if k == 5 and v == 3:
    #             score += 500
    #             return score

    #     # three_ones
    #     for k, v in c.items():
    #         if k == 1 and v == 3:
    #             score += 1000
    #             return score

    #     # Handles straights
    #     if len(c) == 6:
    #         score += 1500
    #         return score

    #     # three_of_a_kind
    #     for k, v in c.items():
    #         if v == 3:
    #             score += k * 100
    #             return score

    #     # four_of_a_kind
    #     for k, v in c.items():
    #         if v == 4:
    #             score += 400
    #             return score

    #     # five_of_a_kind
    #     for k, v in c.items():
    #         if v == 5:
    #             score += 600
    #             return score

    #     # six_of_a_kind
    #     for k, v in c.items():
    #         if v == 6:
    #             score += 800
    #             return score

    #     # one_and_five
    #     if c[1] == 1 and c[5] == 1:
    #         score += 150
    #         return score

    #     # single_five
    #     if c[5] == 1:
    #         score += 50
    #         return score

    #     # single_one
    #     if c[1] == 1:
    #         score += 100
    #         return score

    #     # two_fives
    #     if c[5] == 2:
    #         score += 100
    #         return score

    #     # # two_ones
    #     # if c[1] == 2:
    #     #     score += 200
    #     #     return score

    #     # zilch
    #     if c[2] == 1:
    #         score += 0
    #         return score

# from collections import Counter
# from random import randint


# class GameLogic:
#     @staticmethod
#     def roll_dice(num=6):
#         # version_1

#         return tuple([randint(1, 6) for _ in range(num)])

#     @staticmethod
#     def calculate_score(dice):
#         """
#         dice is a tuple of integers that represent the user's selected dice pulled out from current roll
#         """
#         # version_1

#         if len(dice) > 6:
#             raise Exception("Cheating Cheater!")

#         counts = Counter(dice)

#         if len(counts) == 6:
#             return 1500

#         if len(counts) == 3 and all(val == 2 for val in counts.values()):
#             return 1500

#         score = 0

#         ones_used = fives_used = False

#         for num in range(1, 6 + 1):

#             pip_count = counts[num]

#             if pip_count >= 3:

#                 if num == 1:

#                     ones_used = True

#                 elif num == 5:

#                     fives_used = True

#                 score += num * 100

#                 # handle 4,5,6 of a kind
#                 pips_beyond_3 = pip_count - 3

#                 score += score * pips_beyond_3

#                 # bug if 2 threesomes? Let's test it

#                 # 1s are worth 10x
#                 if num == 1:
#                     score *= 10

#         if not ones_used:
#             score += counts.get(1, 0) * 100

#         if not fives_used:
#             score += counts.get(5, 0) * 50

#         return score

#     @staticmethod
#     def validate_keepers(roll, keepers):
#         # version_3

#         return not Counter(keepers) - Counter(roll)

#     @staticmethod
#     def get_scorers(dice):
#         # version_3

#         all_dice_score = GameLogic.calculate_score(dice)

#         if all_dice_score == 0:
#             return tuple()

#         scorers = []

#         for i in range(len(dice)):
#             sub_roll = dice[:i] + dice[i + 1 :]
#             sub_score = GameLogic.calculate_score(sub_roll)

#             if sub_score != all_dice_score:
#                 scorers.append(dice[i])

#         return tuple(scorers)


