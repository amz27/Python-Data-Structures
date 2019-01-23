import sys 
import numbergenerator

class AugmentedBinaryHeap(object):
    def __init__(self):
        self.heap_array = []
        pass

    def insert(self, key, value):
        self.heap_array.insert(0,key)
        self.heap_array.insert(1,value)
        print self.heap_array

    def removeMin(self):
        # Remove minimum key in the data structure
        pass

    def printMin(self):
        # return the minimum key value pair in the data structure
        return (-1,-1)
        pass

    def find(self, key):
        # finding the value associated with the given key
        return -1
        pass

    def changeKey(self, fromKey, toKey):
        # Changes the key of a pair in the data structure
        pass

    def printHeap(self):
        # returns the array of the internal heap
        return self.heap_array


n,s,m= [9, 5, 10]
ng = numbergenerator.NumberGenerator(5, 10)
ds = AugmentedBinaryHeap()
for i in xrange(n):
    line = ['Insert', 2, 5]
    if line[0] == "Insert":
        rep = int(line[1])
        for j in xrange(rep):
            key = ng.GetNumber()
            value = ng.GetNumber()
            ds.insert(key, value)
    elif line[0] == "RemoveMin":
        rep = int(line[1])
        for j in xrange(rep):
            ds.removeMin()
    elif line[0] == "PrintMin":
        print ' '.join(str(x) for x in ds.printMin())
    elif line[0] == "Find":
        key = int(line[1])
        print ds.find(key)
    elif line[0] == "ChangeKey":
        fromKey = int(line[1])
        toKey = int(line[2])
        ds.changeKey(int(line[1]), int(line[2]))
    elif line[0] == "PrintHeap":
        heapArray = ds.printHeap()
        print ' '.join(str(x[0])+" "+str(x[1]) for x in heapArray)
