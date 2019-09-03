
import matplotlib.pyplot as plt

from Problem import Problem
from Population import Population
import numpy as np

class Algorithm:
    
    def __init__(self):
        self.__problem = Problem()
        self.__dimPopulation = 0
        self.__noOfIterations = 0
        self.readFromFile()
        self.__population = Population(self.__dimPopulation)
        self.__best = []

    def readFromFile(self):
        f = open("file.txt", "r")
        lines = f.readlines()
        self.__noOfIterations = int(lines[0])
        self.__dimPopulation = int(lines[1])
        f.close()

    def iteration(self):
        self.__population.evaluate()
        self.__population.selection()
        return self.__population

    def run(self):

        for i in range(self.__noOfIterations):
            self.__population = self.iteration()
            self.__best.append(self.__population.best().fitness())

        values = sorted(self.__population.getValues(), key=lambda individ: individ.fitness(), reverse=True)
        #print(values[0])
        print("The fitness is:", values[0].fitness())
        
        table = values[0].printSolution()
        for i in range(0, 8):
            for j in range(0, 8):
                if table[i][j] < 10:
                    print(' ', end='')
                print(table[i][j], end=' ')
            print(" ")

        plt.plot(self.__best)
        plt.show()
        return self.__population.best().fitness()

    def statistics(self, list):
        arr = np.array(list)
        print('mean ', np.mean(arr))
        print('std dev ', np.std(arr))