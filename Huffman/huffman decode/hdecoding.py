import sys
import utils


def Decoder(root, inputStr):
    # root : is of type TreeNode and is the root of the Huffman Code tree
    # inputStr : a sequence of 0s and 1s
    #
    # Please write code here
    # The function should return a structure of the following form:
    # decodedString = "abbbdaace"

    result = ""
    curnode = root
    for i in inputStr:
        if i == '1':
            if curnode.right.character != '-':
                result += curnode.right.character
                curnode = root
            else:
                curnode = curnode.right

        else:  # i == '0'
            if curnode.left.character != '-':
                result += curnode.left.character
                curnode = root
            else:
                curnode = curnode.left
    return result



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
