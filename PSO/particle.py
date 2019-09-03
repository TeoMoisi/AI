from random import randint, random
from operator import add
from math import sin, pow
import math
e = 2.718

class Particle:
    def __init__(self):
        self._pozition = [randint(-5,5), randint(-5,5)]
        self.evaluate()
        self.velocity = [ 0 for i in range(2)]
        self._bestPozition =self._pozition.copy()
        self._bestFitness = self._fitness

    def fit(self):
        n=len(self._pozition)
        f=0
        for i in range(n-1):
            f=f+ (-20*e**(-0.2*math.sqrt(0.5*(self._pozition[i]**2+self._pozition[i+1]**2)))-e**(0.5*(math.cos(2*math.pi*self._pozition[i])+math.cos(2*math.pi*self._pozition[i+1])))+e+20)
        return f

    def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fit()

    @property
    def position(self):
        return self._pozition

    @property
    def fitness(self):
        return self._fitness

    @property
    def bestPosition(self):
        return self._bestPozition

    @property
    def bestFitness(self):
        if self._fitness < self._bestFitness:
            return self._fitness
        return self._bestFitness

    def pozition(self, newPozition):
        self._pozition=newPozition.copy()

        self.evaluate()

        if (self._fitness<self._bestFitness):
            self._bestPozition = self._pozition
            self._bestFitness  = self._fitness