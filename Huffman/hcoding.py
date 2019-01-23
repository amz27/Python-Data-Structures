import sys
from heapq import heappush, heappop, heapify
import utils
import operator


def AssignCode(inputStr):

    # Count frequencies
    freq = {}
    for i in inputStr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print freq


    pq = []
    for symbol in freq:
        pq.append(utils.TreeNode(None, None, freq[symbol], symbol))
    heapify(pq)
    n1 = heappop(pq)
    n2 = heappop(pq)
    print n1.character
    print n2.character



    if len(pq) == 1:
        root = utils.TreeNode(None, None, freq[symbol], symbol)
        root.left = pq[0]
        encoding = {symbol: '0'}
        return encoding

    # Huffman Encoding Algorithm
    while len(pq) > 1:
        n1 = heappop(pq)
        n2 = heappop(pq)
        #n3 = utils.TreeNode(None, None, freq[n1], symbol)
        #n3.left = n1
        #n3.right = n2
        #heappush(pq, n3)
        #print n1.character
        #print n2.character

    root = pq[0]
    prefix = ''
    encoding = utils.TraverseTree(root, prefix, freq)

    #return encoding



# Read input
plainString = sys.stdin.readline().strip('\n')
codeDictionary = AssignCode(plainString)
#print len(codeDictionary)
#for character, code in codeDictionary.iteritems():
    #print character, code