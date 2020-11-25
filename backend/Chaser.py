import random

class Chaser:
    def __init__(self, location=0):
        self.location = location
        self.skill = 0.75
        self.init_location = 0

    # generate random num from 1 to 100 and return true 75% of the time
    def try_to_answer(self):
        num = random.randint(1, 101)
        if num <= 100 * self.skill:
            return True
        else:
            return False

    # return the location value of the chaser
    def get_location(self):
        return self.location

    # inc the location of the chaser if try_to_answer returned True
    def play(self):
        if self.try_to_answer():
            self.location = self.location + 1
