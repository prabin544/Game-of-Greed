from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker 

def print_dice(tuple):
    string = ""
    for dice in tuple:
        string += f'{dice}'
    string += ""
    return string


class Game():
    def __init__(self):
        self.round = 0
        self.remaining_dice = 6


    def play(self, roller):
        bank = Banker()
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        roller = input("> ")
        
        if roller == "n" or roller == "no":
            print("OK. Maybe another time")
        else:
            running = True
            while running:
                # round = 1
                print(f'Starting Round {self.round}')
                self.round += 1
                print("Rolling 6 dice")
                print("")
                dice = GameLogic.roll_dice(6)
                print("Enter dice to keep, or (q)uit:")
                answer = input("> ")
                # round += 1
                if answer == "q":
                    running = False
                    print(f'Thanks for playing. You earned {bank.balance} points')

