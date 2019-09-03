
from Individ import Individ

from random import randint

class Population:
    """
        Creates the population
        :param count: the number of individuals in the population
        :param length: the number of values per individual
        :return: a list containing the individuals
        """
    
    def __init__(self, size):
        self.__size = size
        self.__values = []
        self.__crossoverProbability = 0.8
        self.__mutateProbability = 0.2
        for x in range(self.__size):
            self.__values.append(Individ())

    def __str__(self):
        s = ""
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def selectParent(self):
        i = randint(0, self.__size - 1)
        parent = self.__values[i]
        return parent
    
    def evaluate(self):
        for i in range(self.__size):
            parent1 = self.selectParent()
            parent2 = self.selectParent()
            
            child = parent1.crossover(parent1, parent2)
            self.__values.append(child)

        for i in range(0, self.__size):
            self.__values[i].mutate(self.__mutateProbability)


    def selection(self):
        nr = int(self.__crossoverProbability * self.__size)

        values = sorted(self.__values, key=lambda individ: individ.fitness(), reverse=True)
        self.__values = values[:nr]
        rest = values[nr:]

        for i in range(self.__size - nr):
            r = randint(0, len(rest) - 1)
            self.__values.append(rest[r])
            
    def getValues(self):
        return self.__values

    def best(self):
        return sorted(self.__values, key=lambda x: x.fitness(), reverse=True)[0]