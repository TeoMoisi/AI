
from random import randint, random, shuffle, seed


class Individ:

    def __init__(self):
        self.__size = 64
        self.__values = [i for i in range(0, 64)]
        seed()
        shuffle(self.__values)

    def __len__(self):
        return self.__size

    def validPos(self, currentPosition, nextPosition):
        moves = [[1,2],[2,1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

        yCurrent = currentPosition % 8
        xCurrent = int(currentPosition / 8)

        nextY = nextPosition % 8
        nextX = int(nextPosition / 8)
        valid = False
        for i in range(8):
            if nextX == xCurrent + moves[i][0] and nextY == yCurrent + moves[i][1]:
                valid = True
        return valid

    def fitness(self):
        f = 0

        for i in range(self.__size - 1):
            currentPos = self.__values[i]
            nextPos = self.__values[i + 1]

            if self.validPos(currentPos, nextPos):
                f += 1
        return f

    def mutate(self, probability):

        if probability > random():
            p1 = randint(0, self.__size - 1)
            p2 = randint(0, self.__size - 1)
            aux = self.__values[p1]
            self.__values[p1] = self.__values[p2]
            self.__values[p2] = aux
        return self

    def crossover(self, parent1, parent2):

        child = []
        childP1 = []

        geneA = int(random() * len(parent1.__values))
        geneB = int(random() * len(parent2.__values))

        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        for i in range(startGene, endGene + 1):
            childP1.append(parent1.__values[i])

        childP2 = [item for item in parent2.__values if item not in childP1]

        child = childP1 + childP2

        ind = Individ()
        ind.__values = child
        return ind


    def printSolution(self):
        table = []
        for i in range(0, 8):
            row = []
            for j in range(0, 8):
                row.append(0)
            table.append(row)

        count = 1
        for i in self.__values:
            y = i % 8
            x = int(i / 8)
            table[x][y] = count
            count += 1
        return table
