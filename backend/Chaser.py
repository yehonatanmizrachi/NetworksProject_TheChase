import random
class Chaser():

    skill = 0.75

    def __init__(self):
        pass


    def tryToAnswer(self):
        num=random.randint(1, 101)
        if num > 26:
            return True
        else:
            return False