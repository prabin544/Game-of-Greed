from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker 


class Game:
    balance = 0 
    shelved = 0 
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6
        self.bank = Banker()
        


    def play(self, roller=GameLogic.roll_dice):
        # bank = Banker()
        score = 0
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
                    lnDice = len(answer)
                    numbers = tuple(map(int, answer))

                    remaining_dice = self.remaining_dice - lnDice
                    score = GameLogic.calculate_score(numbers)
                    self.shelved = self.shelved + score                  
                    print(f'You have {score} unbanked points and {remaining_dice} dice remaining')
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    answer = input("> ")
                    if answer == 'b':  
                        bank_value = self.bank.bank()                
                        bank_point = self.shelved
                        
                    print(f'You banked {bank_point} points in round {self.round}')
                    print(f'Total score is {score} points')
                    self.round += 1
                elif answer == "q":
                    running = False
                    print(f'Thanks for playing. You earned {score} points')


def print_dice(tuple):
    string = ""
    for dice in tuple:
        string += f'{str(dice)} '
    string += ""
    return string
    
if __name__ == '__main__':
    game1 = Game()
    game1.play()
              