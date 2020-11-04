class Player:

    def __init__(self, money=0, location=3):
        self.money = money
        self.location = location

    def get_location(self):
        return self.location

    def inc_location(self):
        self.location = self.location + 1

    def dec_location(self):
        self.location = self.location - 1

    def add_money(self, money):
        self.money += money

    # divide the player's money by 2
    def div_money(self):
        self.money /= 2

    # double the player's money
    def mul_money(self):
        self.money *= 2

    def get_money(self):
        return self.money
