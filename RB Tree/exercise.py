import RBTree

            
def Trans(theTree, a, b):
    # Please fill in the code here
    #
    return theTree.root.num_rank(b) - theTree.root.num_rank(a-1)


def Subtotal(theTree, a, b):
    # Please fill in the code here
    #
    print theTree.root.val_rank(b)
    print theTree.root.val_rank(a-1)
    return theTree.root.val_rank(b) - theTree.root.val_rank(a-1)