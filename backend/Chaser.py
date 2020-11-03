import random


class Chaser:

    skill = 0.75
    init_location = 0

    # generate random num from 1 to 100 and return true 75% of the time
    @staticmethod
    def try_to_answer():
        num = random.randint(1, 101)
        if num > 26:
            return True
        else:
            return False

    def __init__(self, location='0'):
        self.location = location

# return the location value of the chaser
    def get_location(self):
        return self.location

# inc the location of the chaser if try_to_answer returned True
    def inc_location(self):
        if self.try_to_answer():
            self.location = self.location + 1
