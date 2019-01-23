import random

class NumberGenerator(object):
    def __init__(self, seed, maxNumber):
        self.seed = seed
        self.maxNumber = maxNumber
        random.seed(seed)

    def GetNumber(self):
        return random.randint(1,self.maxNumber)
