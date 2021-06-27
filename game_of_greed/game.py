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
        response = input("> ")

        if response == "n" or response == "no":

            print("OK. Maybe another time")
        else:
            running = True
            while running:
                # round = 1
                print(f'Starting round {self.round}')
                print("Rolling 6 dice...")
                dice = self.roller(self.remaining_dice)
                to_print = print_dice(dice)
                print(f'*** {to_print}***')
                print("Enter dice to keep, or (q)uit:")
                answer = input("> ")
                # checking to see if the answer is an integer
                if answer.isnumeric():
                    # remaining dice is being properly calculated
                    self.remaining_dice = int(answer)
                    # unable to properly access unbanked points/shelved?  Are we pushing the points into the shelf? 
                    print(f'You have {self.bank.shelved} unbanked points and {self.remaining_dice} dice remaining')
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    # was still writing things figuring these out.
                    # roll_again = input("> ")
                    # if roll_again == "b":
                    #     self.bank.bank()
                    # elif roll_again == "r":
                    #     continue
                    # elif roll_again =="q":

                    print(f'You banked {self.bank.balance} points in round {self.round}')
                    print(f'Total score is {self.bank.balance} points')
                    self.round += 1
                elif answer == "q":
                    running = False
                    print(f'Thanks for playing. You earned {self.bank.balance} points')


def print_dice(tuple):
    string = ""
    for dice in tuple:
        string += f'{str(dice)} '
    string += ""
    return string