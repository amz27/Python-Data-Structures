#!/usr/bin/env python
#
# This code adapted from C source from
# Thomas Niemann's Sorting and Searching Algorithms: A Cookbook
#
# From the title page:
#   Permission to reproduce this document, in whole or in part, is
#   given provided the original web site listed below is referenced,
#   and no additional restrictions apply. Source code, when part of
#   a software project, may be used freely without reference to the
#   author.
#
# Adapted by Chris Gonnerman <chris.gonnerman@newcenturycomputers.net>
#        and Graham Breed
#
# Updated by Charles Tolman <ct@acm.org>
#        inheritance from object class
#        added RBTreeIter class
#        added lastNode and prevNode routines to RBTree
#        added RBList class and associated tests
#
# Updated by Stefan Fruhner <marycue@gmx.de>
#        Added item count to RBNode, which counts the occurence
#        of objects. The tree is kept unique, but insertions 
#        of the same object are counted
#        changed RBList.count():  returns the number of occurences of 
#                                 an item
#        Renamed RBList.count to RBList.elements, because of a name 
#        mismatch with RBList.count()
#        changed RBTree.insertNode to count insertions of the same item
#        changed RBList.insert(): uncommented some superfluid code
#        changed RBList.remove(): If called with all=True, then all instances
#                                 of the node are deleted from the tree;
#                                 else only node.count is decremented,
#                                 if finally node.count is 1 the node 
#                                 is deleted.  all is True by default.
#        changed RBTree.deleteNode : same changes as for RBList.remove()
#        finally I've changed the __version__ string to '1.6'

__version__ = "1.6"

import string

BLACK = 0
RED = 1

class RBNode(object):

    def __init__(self, key, value):
        self.left = self.right = self.parent = None
        self.color = RED
        self.key = key
        self.value = value
        self.nonzero = 1
        self.count = 1
        self.numTrans = 1 # number of transactions field
        self.subtotal = self.value
        if key == None:
            # sentinel doesn't count
            self.numTrans = 0
            self.subtotal = 0

    def __str__(self):
        return repr(self.key) + ': ' + repr(self.value)

    def __nonzero__(self):
        return self.nonzero

    def __len__(self):
        """imitate sequence"""
        return 2

    def __getitem__(self, index):
        """imitate sequence"""
        if index==0:
            return self.key
        if index==1:
            return self.value
        raise IndexError('only key and value as sequence')

    def update(self): # update function for number of transactions field
        if self.key != None:
            # ignore sentinel
            self.numTrans = 1 + self.left.numTrans + self.right.numTrans
            self.subtotal = self.value + self.left.subtotal + self.right.subtotal

    def num_rank(self, x):
        if self.key == None:
            return 0
        elif x == self.key:
            return 1 + self.left.numTrans
        elif x < self.key:
            return self.left.num_rank(x)
        else:
            return 1 + self.right.num_rank(x) + self.left.numTrans

    def val_rank(self, x):
        if self.key == None:
            return 0
        elif x == self.key:
            return self.value + self.left.subtotal
        elif x < self.key:
            return self.left.val_rank(x)
        else:
            return self.right.val_rank(x) + self.value + self.left.subtotal


class RBTree(object):

    def __init__(self, cmpfn=cmp, unique=True):
        self.sentinel = RBNode(None,None)
        #self.sentinel.key = None
        self.sentinel.left = self.sentinel.right = self.sentinel
        self.sentinel.color = BLACK
        self.sentinel.nonzero = 0
        self.root = self.sentinel
        self.elements = 0
        
        #SF: If self.unique is True, all elements in the tree have 
       	#SF  to be unique and an exception is raised for multiple 
       	#SF insertions of a node
       	#SF If self.unique is set to False, nodes can be added multiple 
       	#SF times. There is still only one node, but all insertions are
       	#SF counted in the variable node.count
        self.unique = unique
        # changing the comparison function for an existing tree is dangerous!
        self.__cmp = cmpfn

    def __len__(self):
        return self.elements

    def __del__(self):
        # unlink the whole tree

        s = [ self.root ]

        if self.root is not self.sentinel:
            while s:
                cur = s[0]
                if cur.left and cur.left != self.sentinel:
                    s.append(cur.left)
                if cur.right and cur.right != self.sentinel:
                    s.append(cur.right)
                cur.right = cur.left = cur.parent = None
                cur.key = cur.value = None
                s = s[1:]

        self.root = None
        self.sentinel = None

    def __str__(self):
        return "<RBTree object>"

    def __repr__(self):
        return "<RBTree object>"

    def rotateLeft(self, x):

        y = x.right

        # establish x.right link
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y

        # link x and y
        y.left = x
        if x != self.sentinel:
            x.parent = y

        x.update()
        y.update()

    def rotateRight(self, x):

        #***************************
        #  rotate node x to right
        #***************************

        y = x.left

        # establish x.left link
        x.left = y.right
        if y.right != self.sentinel:
            y.right.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        else:
            self.root = y

        # link x and y
        y.right = x
        if x != self.sentinel:
            x.parent = y

        x.update()
        y.update()
    def insertFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after inserting node x           *
        #************************************

        # check Red-Black properties

        while x != self.root and x.parent.color == RED:

            # we have a violation

            if x.parent == x.parent.parent.left:

                y = x.parent.parent.right

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.right:
                        # make x a left child
                        x = x.parent
                        self.rotateLeft(x)

                    # recolor and rotate
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateRight(x.parent.parent)
            else:

                # mirror image of above code

                y = x.parent.parent.left

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.left:
                        x = x.parent
                        self.rotateRight(x)

                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateLeft(x.parent.parent)

        self.root.color = BLACK

    def insertNode(self, key, value):
        #**********************************************
        #  allocate node for data and insert in tree  *
        #**********************************************

        # we aren't interested in the value, we just
        # want the TypeError raised if appropriate
        hash(key)

        # find where node belongs
        current = self.root
        parent = None
        while current != self.sentinel:
            # GJB added comparison function feature
            # slightly improved by JCG: don't assume that ==
            # is the same as self.__cmp(..) == 0
            rc = self.__cmp(key, current.key)
            if rc == 0:
                #SF This item is inserted for the second, 
                #SF third, ... time, so we have to increment 
                #SF the count
                if self.unique == False: 
                    current.count += 1
                else: # raise an Error
                    pass
                    #print "Warning: This element is already in the list ... ignored!"
                    #SF I don't want to raise an error because I want to keep 
                    #SF the code compatible to previous versions
                    #SF But here would be the right place to do this
                    #raise IndexError ("This item is already in the tree.")
                return current
            parent = current
            if rc < 0:
                current = current.left
            else:
                current = current.right

        # setup new node
        x = RBNode(key, value)
        x.left = x.right = self.sentinel
        x.parent = parent

        self.elements = self.elements + 1

        # insert node in tree
        if parent:
            if self.__cmp(key, parent.key) < 0:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x

        self.insertFixup(x)
        print x
        temp = x
        while temp.parent != None:

            temp.parent.update()
            temp = temp.parent
            #print temp

        #return x

    def deleteFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after deleting node x            *
        #************************************

        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateLeft(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.rotateRight(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.rotateLeft(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateRight(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.rotateLeft(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.rotateRight(x.parent)
                    x = self.root

        x.color = BLACK

    def deleteNode(self, z, all=True):
        #****************************
        #  delete node z from tree  *
        #****************************

        if not z or z == self.sentinel:
            return
            
        #SF If the object is in this tree more than once the node 
        #SF has not to be deleted. We just have to decrement the 
        #SF count variable
        #SF we don't have to check for uniquness because this was
        #SF already captured in insertNode() and for this reason 
        #SF z.count cannot be greater than 1
        #SF If all=True then the complete node has to be deleted
        if z.count > 1 and not all: 
            z.count -= 1
            return          

        if z.left == self.sentinel or z.right == self.sentinel:
            # y has a self.sentinel node as a child
            y = z
        else:
            # find tree successor with a self.sentinel node as a child
            y = z.right
            while y.left != self.sentinel:
                y = y.left

        # x is y's only child
        if y.left != self.sentinel:
            x = y.left
        else:
            x = y.right

        # remove y from the parent chain
        x.parent = y.parent
        if y.parent:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x

        if y != z:
            z.key = y.key
            z.value = y.value

        if y.color == BLACK:
            self.deleteFixup(x)

        del y
        self.elements = self.elements - 1

    def findNode(self, key):
        #******************************
        #  find node containing data
        #******************************

        # we aren't interested in the value, we just
        # want the TypeError raised if appropriate
        hash(key)

        current = self.root

        while current != self.sentinel:
            # GJB added comparison function feature
            # slightly improved by JCG: don't assume that ==
            # is the same as self.__cmp(..) == 0
            rc = self.__cmp(key, current.key)
            if rc == 0:
                return current
            else:
                if rc < 0:
                    current = current.left
                else:
                    current = current.right

        return None

# end of file.
