import sys
import RBTree
import exercise
import numbergenerator

#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE

#Read input
ds = RBTree.RBTree()
header = [int(x) for x in sys.stdin.readline().split()]
numInstructs = header[0]
randomSeed = header[1]
generator = numbergenerator.NumberGenerator(randomSeed)
for i in range(0, numInstructs):
    lineSplit = sys.stdin.readline().strip('\n').split(' ')
    if lineSplit[0] == "Insert":
        numInserts = int(lineSplit[1]) # number of inserts
        for j in range(0, numInserts):
            time, amount = generator.getTransaction()
            ds.insertNode(time, amount)
    elif lineSplit[0] == "Trans":
        timeA = int(lineSplit[1])
        timeB = int(lineSplit[2])
        ansTrans = exercise.Trans(ds, timeA, timeB)
        print ansTrans
    elif lineSplit[0] == "Subtotal":
        timeA = int(lineSplit[1])
        timeB = int(lineSplit[2])
        ansSub = exercise.Subtotal(ds, timeA, timeB)
        print ansSub
