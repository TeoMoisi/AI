from random import shuffle
from sklearn.model_selection import train_test_split

from Chromosome import Chromosome
from Population import Population
import matplotlib.pyplot as plt


class Algorithm:
    def __init__(self, filename, nrInd, iterations, depht, train_size, test_size):
        self.n = 0
        self.x = []
        self.y = []
        self.xTest = []
        self.yTest = []
        self.xTrain = []
        self.yTrain = []
        self.filename = filename
        self.nrInd = nrInd
        self.pop = Population(nrInd, depht)
        self.probability_mutate = 0.5
        self.probability_crossover = 0.5
        self.iter_no = iterations
        self.depht = depht
        self.train_size = train_size
        self.test_size = test_size
        self.header = []

    def iteration(self, i):
        parents = range(self.nrInd)
        nrChilds = len(parents) // 2
        offspring = Population(nrChilds, self.depht // 2)
        for i in range(nrChilds):
            ch = Chromosome(self.depht)
            offspring.arr[i] = ch.crossover(self.pop.arr[i << 1], self.pop.arr[(i << 1) | 1])
            offspring.arr[i].mutate(self.probability_mutate)
        offspring.fitness_eval(self.xTrain, self.yTrain)
        self.pop.reunion(offspring)
        self.pop.selection(self.nrInd)

    def run(self):
        self.loadDataSet()

        self.pop.fitness_eval(self.xTrain, self.yTrain)
        bests = []
        for i in range(self.iter_no):
            print("Iter no.: " + str(i))
            self.iteration(i)
            self.pop.fitness_eval(self.xTrain, self.yTrain)
            self.pop.selection(self.nrInd)
            best = self.pop.best(1)[0]
            print("Best fitness: " + str(best.fitness))
            bests.append(best.fitness)

        plt.plot(range(0, 100), bests, label='best fitness per iteration')
        plt.xlabel('Iterations')
        plt.ylabel('best fitness')
        plt.legend()
        plt.show()



    def loadDataSet(self):
        '''
        function to load data from file and divise it into train and test data
        :return:
        '''
        with open(self.filename, "r") as f:
            self.header = f.readline().split(',')[1:-1]
            for line in f.readlines():
                values = line.split(',')
                self.x.append(values[1:-1])
                self.y.append(values[-1])
                self.n += 1

        shuffle(self.x)
        shuffle(self.y)
        self.xTrain = self.x[int(self.n * self.test_size):self.n]
        self.yTrain = self.y[int(self.n * self.test_size):self.n]
        self.xTest = self.x[0:int(self.n * self.test_size)]
        self.yTest = self.y[0:int(self.n * self.test_size)]

        print("Training size: " + str(len(self.xTrain)))
        print("Testing size: " + str(len(self.xTest)))