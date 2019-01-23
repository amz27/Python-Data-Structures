
def getSize(self, theTree):
    if theTree is None:
        return 0

    if theTree is not None:
        return 1 + self.treeSize(theTree.left) + self.treeSize(theTree.right)