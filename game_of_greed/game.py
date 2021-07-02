from random import gammavariate, shuffle
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker 


class Game:
    # balance = 0 
    # shelved = 0
    # self.cur_round = 1
    def __init__(self):
        self.cur_round = 0
        self.bank = Banker()
        # self.remaining_dice = 6


        

    def play(self, roller):
        score = 0
        # cur_round = 0
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n" or response == "no":

            print("OK. Maybe another time")
        else:
            running = True
            while running:
                self.play_round()

                turn = True
                while turn is True:
                    answer = input("> ")
                    if answer.isnumeric():
                        self.answer_numeric(answer)
                    elif answer == 'b':
                        self.bank_it(score, self.cur_round)
                        turn = False
                    elif answer == 'r':
                        self.roll_again()
                    elif answer == 'q':
                        print(f'Thanks for playing. You earned {self.bank.balance} points')
                        running = False
                        turn = False
                    
    def roll_again(self):
        print(f'Rolling {self.remaining_dice} dice...')
        dice = self.roller(self.remaining_dice)
        to_print = self.print_dice(dice)
        print(f'*** {to_print}***')
        print("Enter dice to keep, or (q)uit:")

    def bank_it(self, shelved, balance):
        print(f'You banked {self.bank.shelved} points in round {self.cur_round}')
        self.bank.bank()
        print(f'Total score is {self.bank.balance} points')

    def answer_numeric(self, answer):
        lnDice = len(answer)
        numbers = tuple(map(int, answer))
        self.remaining_dice = self.remaining_dice - lnDice
        score = GameLogic.calculate_score(numbers)
        self.bank.shelf(score)
        print(f'You have {score} unbanked points and {self.remaining_dice} dice remaining')
        print("(r)oll again, (b)ank your points or (q)uit:")

    def play_round(self):
        self.remaining_dice = 6
        self.cur_round += 1
        print(f'Starting round {self.cur_round}')
        self.roll_again()

    def bankrupt(self):
        self.bank.clear_shelf
        print("""
            ****************************************
            **        Zilch!!! Round over         **
            ****************************************
        """)

    def print_dice(self, tuple):
        string = ""
        for dice in tuple:
            string += f'{str(dice)} '
        string += ""
        return string
    
if __name__ == '__main__':
    game1 = Game()
    game1.play()
              