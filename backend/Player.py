class Player:

    def __init__(self, money=0, location=0):
        self.money = money
        self.location = location

    def get_location(self):
        return self.location

    def inc_location(self):
        self.location = self.location + 1

    def dec_location(self):
        self.location = self.location - 1

    def set_money(self, money):
        self.money = money

    def get_money(self):
        return self.money
