class Player:

    def __init__(self, money=0, location=3):
        self.__money = money
        self.__location = location
        self.__used_life_line = False  # galgal hazala

    def get_location(self):
        return self.__location

    def inc_location(self):
        self.__location = self.__location + 1

    def dec_location(self):
        self.__location = self.__location - 1

    def add_money(self, money):
        self.__money += money

    # divide the player's money by 2
    def div_money(self):
        self.__money /= 2

    # double the player's money
    def mul_money(self):
        self.__money *= 2

    def get_money(self):
        return self.__money

    def get_life_line_status(self):
        return self.__used_life_line

    def use_life_line(self):
        if self.__used_life_line:
            return False
        self.__used_life_line = True
        return True
