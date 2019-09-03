import random

from individ import Individ


class Population:

    def __init__(self, nrInd, problem):
        self.nrInd = nrInd
        self.problem = problem
        self.population = []
        for ind in range(nrInd):
            self.population.append(Individ(self.problem))
        self.size = len(self.population)

    def evaluate(self):
        for individ in self.population:
            return individ.fitness()

    # def evaluate(self, prob_mutate):
    #     self.crossover_population()
    #     self.mutation_population(prob_mutate)

    def select_parent(self):
        turnir = []
        turnir_size = 10
        for i in range(0, turnir_size):
            p = random.randint(0, self.size - 1)
            print("p", p)
            print(self.population)
            print(self.size)
            turnir.append(self.population[p])
        turnir.sort(key=lambda x:x.fitness(), reverse=True)
        return turnir[0]

    # def selection(self, popFactor):
    #     elitePopulation = []
    #     self.population.sort(key=lambda x:x.fitness(), reverse=True) #order by fitness
    #     self.population.reverse()
    #     for i in range(int(popFactor * self.nrInd)):
    #         elitePopulation.append(self.population[i])

        # self.population = elitePopulation

    def selection(self, maxInd):
        if maxInd < self.nrInd:
            self.nrInd = maxInd
            self.population = sorted(self.population, key=lambda ind: ind.fitness())
            self.population = self.population[:maxInd]

    def reunion(self, other):
        self.nrInd += other.nrInd
        self.population = self.population + other.population

    def bestOf(self, maxInd):
        arrSorted = sorted(self.population, key=lambda ind: ind.fitness())
        return arrSorted[:maxInd]

    # def crossover_population(self):
    #     pop = self.population[:]
    #     for i in range(0, self.size):
    #         parent1 = self.select_parent()
    #         parent2 = self.select_parent()
    #         child = parent1.crossover(parent2)
    #         pop.append(child)
    #     self.population = pop
    #
    # def mutation_population(self, prob_mutate):
    #     for i in range(0, self.size):
    #         if random.random() < prob_mutate:
    #             self.population[i].mutation(prob_mutate)

