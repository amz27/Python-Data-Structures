import sys
import RBTree
import exercise

#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE

#Read input
ds = RBTree.RBTree()
for line in sys.stdin:
    lineSplit = line.strip('\n').split(' ')
    if lineSplit[0] == "Insert":
        key = int(lineSplit[1])
        value = int(lineSplit[2])
        ds.insertNode(key, value)
    elif lineSplit[0] == "Delete":
        key = int(lineSplit[1])
        delNode = ds.findNode(key)
        ds.deleteNode(delNode)
    elif lineSplit[0] == "GetSize":
        size = exercise.getSize(ds)
        print size
        pass
    elif lineSplit[0] == "GetHeight":
        # height = exercise.getHeight(ds)
        # print height
        pass
    elif lineSplit[0] == "FindSuccessor":
        # key = int(lineSplit[1])
        # keyNode = ds.findNode(key)
        # keyValue = exercise.findSuccessor(ds, keyNode)
        # print str(keyValue[0]) + " " + str(keyValue[1])
        pass
    elif lineSplit[0] == "CountKeysBetween":
        # keyA = int(lineSplit[1])
        # keyB = int(lineSplit[2])
        # numBetween = exercise.countKeysBetween(ds, keyA, keyB)
        # print numBetween
        pass