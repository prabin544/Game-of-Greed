from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker 



class Game():
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6
        self.bank = Banker()

    def play(self, roller):

        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        # print("> y")
        # print("Starting round 1")
        # print("Rolling 6 dice...")
        # print("*** 4 4 5 2 3 1 ***")
        # print("")
        # print("> q")
        # print("Thanks for playing. You earned 0 points")
        response = input("> ")
        
        if response == "n" or response == "no":

            print("OK. Maybe another time")
        else:
            running = True
            while running:
                # round = 1
                print(f'Starting round {self.round}')
                print("Rolling 6 dice...")
                self.round += 1
                dice = self.roller(self.remaining_dice)
                to_print = print_dice(dice)
                print(f'*** {to_print}***')
                print("Enter dice to keep, or (q)uit:")
                answer = input("> ")
                if answer == "q":
                    running = False
                    print(f'Thanks for playing. You earned {self.bank.balance} points')


def print_dice(tuple):
    string = ""
    for dice in tuple:
        string += f'{str(dice)} '
    string += ""
    return string

