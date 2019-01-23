import sys
import utils

def Decoder(root , inputStr):
    #
    # Please write code here
    #
    pass

# Read input
n = int(sys.stdin.readline().strip('\n'))
codeDictionary = {}
for i in xrange(n):
    character, code = sys.stdin.readline().strip('\n').split()
    codeDictionary[character] = code
codedString = sys.stdin.readline().strip('\n')
huffmanTreeRoot = utils.ConstructHuffmanTree(codeDictionary)
decodedString = Decoder(huffmanTreeRoot, codedString)
print decodedString