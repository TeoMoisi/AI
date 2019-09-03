from random import random, randint, shuffle, uniform
import secrets

class Individ:

    def __init__(self, problem=None):
        self.problem = problem
        if (self.problem.isEmpty() == True):
            #print("True")
            self.positions = [[randint(0, 8),randint(0, 8)]]
        else:
            #print("False")
            self.positions = []
        self.size = len(self.positions)



    def mutate(self, probMut):
        value = 0
        for i in range(8):
            for j in range(8):
                if self.problem.getBoard()[i][j] != 0:
                    value +=1

        if probMut > random():
            if self.size > 1:
                self.positions.pop(-1)
            last_pos = self.positions[-1]
            #print("last", last_pos)
            arr = [-2, -1, 1, 2]
            #random.seed()
            i = secrets.choice(arr)
            #random.seed()
            j = None
            if i == 1 or i == -1:
                j = secrets.choice([-2, 2])
            else :
                j = secrets.choice([-1, 1])

            #print("i", last_pos[0] + i)
            #print("j", last_pos[1] + j)
            if (last_pos[0] + i) < 8:
                if (last_pos[1] + j) < 8:
                    if (last_pos[0] + i) >= 0:
                        if(last_pos[1] + j) >= 0:
                            new_pos = [last_pos[0] + i, last_pos[1] + j]
                            self.positions.append(new_pos)
                            #print(self.positions)
                            #print("new", new_pos)
                            if (self.problem.getBoard()[new_pos[0]][new_pos[1]] == 0):
                                self.problem.update(new_pos, value+1)
                            #print(self.problem.printBoard())
        return Individ(self.problem)

    def fitness(self):
        return self.size

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness > other.fitness

    def crossover(self, ind1, ind2, prob):
        new_ind = Individ(self.problem)
        # print("ind1", ind1.positions)
        # print("ind2", ind2.positions)
        for i in range(ind1.size):
            if prob < random():
                new_ind.positions.append(ind1.positions[i])
            else:
                new_ind.positions.append(ind2.positions[i])
        #new_ind.positions = [ind1.positions[i] if prob < random() else ind2.positions[i] for i in range(ind1.size)]
        new_ind.size = len(new_ind.positions)
        #print("newind pos", new_ind.positions)
        return new_ind

