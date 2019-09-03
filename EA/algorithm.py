from random import randint
import matplotlib.pyplot as plt

import numpy as np

from individ import Individ
from population import Population
from problem import Problem


class Algorithm:

    def __init__(self, fileName):
        self.fileParams = fileName
        self.problem = Problem()
        self.probability_mutate, self.probability_crossover, self.nrInd, self.nrGen = self.__readParameters()
        self.population = Population(self.nrInd, self.problem)
        #Population(self.nrInd, self.problem).evaluate()
        self.std = []
        self.average = []
        self.bestf = []

    def __readParameters(self):
        with open(self.fileParams, 'r') as f:
            nrInd = int(f.readline())
            nrGen = int(f.readline())
            probability_mutate = float(f.readline())
            probability_crossover = float(f.readline())
            return probability_mutate, probability_crossover, nrInd, nrGen
    #
    #
    # def iteration(self):
    #     # while not self.problem.isFull():
    #     #     self.population.evaluate(self.probability_mutate)
    #     #     self.population.selection(1/4)
    #     # return self.population.population.sort(key=lambda x:x.fitness(), reverse=True)
    #
    #     i1 = randint(0, len(self.population) - 1)
    #     i2 = randint(0, len(self.population) - 1)
    #     print("indeices", i1, i2)
    #     if (i1 != i2):
    #         ind = Individ(self.problem)
    #         c = ind.crossover(self.population[i1], self.population[i2], self.probability_crossover)
    #         nou = c.mutate(self.probability_mutate)
    #         f1 = self.population[i1].fitness()
    #         f2 = self.population[i2].fitness()
    #         fc = nou.fitness()
    #         if (f1 > f2) and (f1 > fc):
    #             self.population[i1] = c
    #         if (f2 > f1) and (f2 > fc):
    #             self.population[i2] = c
    #     return self.population


    def iteration(self):
        parents = range(self.nrInd)
        nrChilds = len(parents) // 2
        offspring = Population(nrChilds, self.problem)
        for i in range(nrChilds):
            ind = Individ(self.problem)
            offspring.population[i] = ind.crossover(self.population.population[i << 1], self.population.population[(i << 1) | 1],
                                                    self.probability_crossover)
            offspring.population[i].mutate(self.probability_mutate)
        offspring.evaluate()
        self.population.reunion(offspring)
        self.population.selection(self.nrInd)

    def drawPlot(self):
        arr = []
        for i in range(len(self.population.population)):
            arr.append(self.population.population[i].fitness())
        arr = np.array(arr)
        m = np.mean(arr, axis=0)
        std = np.std(arr, axis=0)
        avg = np.average(arr, axis=0)
        means = []
        stddev = []
        average = []
        for i in range(30):
            means.append(m)
            stddev.append(std)
            average.append(avg)

        plt.plot(range(1, len(stddev) + 1), stddev, label="stddev")
        plt.plot(range(1, len(average) + 1),average, label="average")
        plt.plot(range(1, len(means) + 1),means, label="mean")
        # plt.plot(range(30), means)
        # plt.plot(range(30), stddev)
        # plt.plot(range(30), average)
        plt.show()


    def run(self, shouldShow=True):
        if shouldShow:
            plt.figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')
        for nowIter in range(self.nrGen):
            if nowIter % 30 == 0:
                print("Running iteration: " + str(nowIter))
                self.drawPlot()
                self.population.problem.plotBoard()
            self.iteration()
        return self.population





