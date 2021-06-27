class Banker():
    def __init__(self, shelved = 0, balance = 0):
        self.shelved = shelved
        self.balance = balance


    def shelf(self, pointDeposit = 100):
        self.shelved += pointDeposit

    def bank(self):
        temp_shelved = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return temp_shelved

    def clear_shelf(self):
        self.shelved = 0



# a = Banker()
# print(Banker.bank(self))