from random import shuffle, random, randint
from numpy.random import choice
from math import floor, ceil, sin, cos, sqrt
from copy import deepcopy
from cmath import sqrt


functions = ['+', '-', '*', 'sin', 'cos']
#functions = ['+', '-', '*']
terminals = ["val" + str(x) for x in range(1,9)]

class Leaf:
    #class for leaf
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.size = 1

    def deepcopy(self):
        copy = Leaf()
        copy.val = self.val
        copy.size = self.size
        if self.left:
            copy.left = self.left.deepcopy()
        if self.right:
            copy.right = self.right.deepcopy()
        return copy

    def change(self, root, node1, node2):
        self.val = root.val
        if root.left:
            if root.left == node1:
                self.left = node2.deepcopy()
            else:
                self.left = Leaf()
                self.left.change(root.left, node1, node2)
        if root.right:
            if root.right == node1:
                self.right = node2.deepcopy()
            else:
                self.right = Leaf()
                self.right.change(root.right, node1, node2)
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def init(self, d):
        if d == 0:
            self.val = choice(terminals)
            return
        self.val = choice(functions)
        self.left = Leaf()
        self.left.init(d - 1)
        self.size += self.left.size
        if self.val != 'sin' and self.val != 'cos':
            self.right = Leaf()
            self.right.init(d - 1)
            self.size += self.right.size

    def getLeafs(self):
        ret = []
        if self.left:
            ret += self.left.getLeafs()
        ret.append(self)
        if self.right:
            ret += self.right.getLeafs()
        return ret

    def getLeaf(self, pos):
        if pos <= 0:
            return None
        if pos > self.size:
            return None
        if self.left and pos <= self.left.size:
            return self.left.getLeaf(pos)
        else:
            leftSize = 0
            if self.left:
                leftSize = self.left.size
            if leftSize + 1 == pos:
                return self
            else:
                return self.right.getLeaf(pos - leftSize - 1)

    def mutate(self, pos, prob):
        if pos <= 0:
            assert(False)
        if pos > self.size:
            assert(False)
        if self.left and pos <= self.left.size:
            self.left.mutate(pos, prob)
        else:
            leftSize = 0
            if self.left:
                leftSize = self.left.size
            if leftSize + 1 == pos:
                if random() < prob:
                    if self.val in terminals:
                        self.val = choice(terminals)
                    else:
                        if self.val == 'sin':
                            self.val = 'cos'
                        elif self.val == 'cos':
                            self.val = 'sin'
                        else:
                            self.val = choice(functions[:3])
            else:
                self.right.mutate(pos - leftSize - 1, prob)

    def __str__(self):
        if self.val in terminals:
            return str(self.val)
        if self.val == "sin" or self.val == "cos" or self.val == "sqrt":
            return self.val + "(" + str(self.left) + ")"
        return str(self.left) + self.val + str(self.right)
