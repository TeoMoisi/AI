from particle import Particle
from swarm import Swarm
from controller import Controller
from problem import Problem
import matplotlib.pyplot as plt

def main():
    pr = Problem().readFromFile()
    noOfParticles = pr[0]
    noOfNeighbours = pr[1]
    w = pr[2]
    c1 = pr[3]
    c2 = pr[4]
    noOfIterations = pr[5]
    #swarm = Swarm(noOfParticles, noOfNeighbours)
    ctrl = Controller(noOfParticles, noOfNeighbours, c1, c2, w)
    for i in range(noOfIterations):
        #print(i)
        P = ctrl.iteration()
        ctrl = Controller(P.noOfParticles, P.nSize, c1, c2, w/(i+1))
        if i % 30 == 0:
            plt.plot(ctrl.population.getBestNeighbourParticle())
            plt.show()

    # print the best individual
    best = 0
    bests = []
    for i in range(len(P.getBestParticles())):
        bests.append(P.getParticles()[i].fitness)
        print(i, "fitness", P.getParticles()[i].fitness)
        if i % 30 == 0 and i != 0:
            plt.plot(bests)
            plt.show()
        if (P.getParticles()[i].fitness < P.getParticles()[best].fitness):
            print("Best fitness until now: ", i, P.getParticles()[i].fitness)
            best = i

    fitnessOptim = P.getParticles()[best].fitness
    individualOptim = P.getParticles()[best].position
    print(fitnessOptim)
    print(individualOptim)
    ctrl.statistics(bests)


if __name__ == '__main__':
    main()