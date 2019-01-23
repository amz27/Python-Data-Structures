class TreeNode(object):
    def __init__(self, left, right, frequency, character):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.character = character

def TraverseTree(root, prefix, codeList):
    if root.character != '-':
        if prefix == "": # The case where there is only one character
            prefix = "0"
        codeList[root.character] = prefix
    else:
        TraverseTree(root.left, prefix+"0", codeList)
        TraverseTree(root.right, prefix+"1", codeList)