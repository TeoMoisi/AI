from Chromosome import Chromosome


class Population:
    def __init__(self, nrInd, depht):
        self.nrInd = nrInd
        self.arr = [Chromosome(depht) for _ in range(nrInd)]

    def fitness_eval(self, X, Y):
        for ch in self.arr:
            ch.fitness_eval(X, Y)

    def selection(self, maxInd):
        if maxInd < self.nrInd:
            self.nrInd = maxInd
            self.arr = sorted(self.arr, key = lambda x: x.fitness)
            self.arr = self.arr[:maxInd]

    def reunion(self, other):
        self.nrInd += other.nrInd
        self.arr = self.arr + other.arr

    def best(self, maxInd):
        pop_sorted = sorted(self.arr, key = lambda x: x.fitness)
        return pop_sorted[:maxInd]