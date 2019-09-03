from math import exp
from random import random, seed
import matplotlib.pyplot as plt
import numpy as np

from swarm import Swarm


class Controller:
    def __init__(self, noOfParticles, noOfNeighbours, c1, c2, w):
        self.population = Swarm(noOfParticles, noOfNeighbours)
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def iteration(self):

        neighbors = self.population.getBestParticles()
        bestNeighbors = self.population.getBestNeighbourParticle()

        for i in range(self.population.getSize()):

            for j in range(len(self.population.getParticles()[0].velocity)):
                seed()
                newVelocity = self.w * self.population.getParticles()[i].velocity[j]

                newVelocity = newVelocity + self.c1 * random() * (
                        self.population.getParticles()[i].position[j] - self.population.getParticles()[i].position[j])
                newVelocity = newVelocity + self.c2 * random() * (
                        self.population.getParticles()[i].bestPosition[j] - self.population.getParticles()[i].position[j])
                self.population.getParticles()[i].velocity[j] = newVelocity

        for i in range(self.population.getSize()):
            newPosition = []
            for j in range(len(self.population.getParticles()[0].velocity)):
                newPosition.append((self.population.getParticles()[i].position[j] + self.population.getParticles()[i].velocity[j])%2)
            # self.population.getParticles()[i].position[0] = newPosition[0]
            # self.population.getParticles()[i].position[1] = newPosition[1]
            self.population.getParticles()[i].pozition(newPosition)

        return self.population


    def statistics(self, list):
        arr = np.array(list)
        print('mean ', np.mean(arr))
        print('std dev ', np.std(arr))
