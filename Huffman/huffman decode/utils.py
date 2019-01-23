class TreeNode(object):
    def __init__(self, left, right, frequency, character):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.character = character

def ConstructHuffmanTree(codeDictionary):
    huffmanTreeRoot = TreeNode(None, None, 0, '-')
    incompleteNodes = 0
    for character, code in codeDictionary.iteritems():
        curNode = huffmanTreeRoot
        for i in xrange(len(code)):
            if code[i] == '0':
                if curNode.left == None:
                    if curNode.right == None:
                        incompleteNodes += 1
                    else:
                        incompleteNodes -= 1
                    curNode.left = TreeNode(None, None, 0, '-')
                curNode = curNode.left
            else:
                if curNode.right == None:
                    if curNode.left == None:
                        incompleteNodes += 1
                    else:
                        incompleteNodes -= 1
                    curNode.right = TreeNode(None, None, 0, '-')
                curNode = curNode.right
        curNode.character = character

    if (len(codeDictionary) == 1 and incompleteNodes == 1) or (len(codeDictionary) > 1 and incompleteNodes == 0):
        return huffmanTreeRoot
    else:
        return None # This means that the resulting tree was invalid