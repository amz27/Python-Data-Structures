import random

class NumberGenerator(object):
    def __init__(self, seed):
        self.seed = seed
        self.maxValueUnique = 100000000  # 10^8 for time
        self.maxValue = 1000  # 10^3 for amounts
        self.count = 200000  # 2*10^5
        random.seed(seed)
        uniqueNum = set()
        self.randValuesUnique = []
        for i in xrange(self.count):
            randNum = random.randint(1, self.maxValueUnique)
            while randNum in uniqueNum:
                randNum = random.randint(1, self.maxValueUnique)
            self.randValuesUnique.append(randNum)
            uniqueNum.add(randNum)
        del uniqueNum

        #self.randValuesUnique = random.sample(range(1, self.maxValueUnique), self.count)
        self.randValues = [random.randint(1, self.maxValue) for i in xrange(self.count)]
        self.randCounter = 0

    def getTransaction(self):
        time = self.randValuesUnique[self.randCounter]
        amount = self.randValues[self.randCounter]
        self.randCounter += 1
        return time, amount
