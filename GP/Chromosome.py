from random import choice, randint
from math import sin, cos, sqrt
from cmath import sqrt
from copy import deepcopy

from Leaf import Leaf

class Chromosome:
    def __init__(self, d):
        # d is the max depht for the tree
        self.maxDepth = d
        self.fitness = 0
        self.root = Leaf() #root is of type Leaf
        self.root.init(d)
        self.header = ['val1', 'val2', 'val3', 'val4', 'val4', 'val5', 'val6', 'val7', 'val8']

    def fitness_eval(self, X, Y):
        self.fitness = 0
        exp = str(self.root)
        cnt = 0
        for (x, y) in zip(X, Y):
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            for i in range(len(x)):
                exec("{} = {}".format(self.header[i], x[i]))
            res = eval(exp)
            self.fitness += abs(res - float(y))
        self.fitness = self.fitness / len(X)
        return self.fitness

    def crossover(self, ch1, ch2):
        node1 = choice(ch1.root.getLeafs())
        node2 = choice(ch2.root.getLeafs())
        c = Chromosome(self.maxDepth)

        if ch1.root == node1:
            c.root = node2.deepcopy()
        else:
            c.root = Leaf()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)