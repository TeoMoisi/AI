from particle import Particle
from random import randint

import copy

class Swarm:

    def __init__(self, noOfPaticles, nSize):
        self.noOfParticles = noOfPaticles
        self.particles = self.create()
        self.nSize = nSize #neighbour size

    def getParticles(self):
        return self.particles

    def getSize(self):
        return len(self.particles)

    def create(self):
        particles = []
        for i in range(self.noOfParticles):
            p = Particle()
            particles.append(p)
        return particles

    def getBestNeighbourParticle(self):
        bestNeighbor = []
        bestnow = 0
        neighbors = self.getBestParticles()
        for particle in range(self.noOfParticles):
            bestNeighbor.append(neighbors[particle][0])
            for i in range(0, len(neighbors[particle])):
                if (self.particles[bestNeighbor[particle]].fitness > self.particles[neighbors[particle][i]].fitness):
                    bestNeighbor[particle] = neighbors[particle][i]
            #     if (neighbors[particle][i].fitness < neighbors[particle][bestnow].fitness):
            #         bestnow = i
            # bestNeighbor.append(neighbors[particle][bestnow])

        return bestNeighbor


    def getBestParticles(self):
        #selecting random neighbours for each particle
        if self.nSize > len(self.particles):
            self.nSize = len(self.particles)
        neighbors = []
        for i in range(len(self.particles)):
            localNeighbor = []
            for j in range(self.nSize):
                x = randint(0, len(self.particles) - 1)
                while x in localNeighbor:
                    x = randint(0, len(self.particles) - 1)
                # localNeighbor.append(self.particles[x])
                localNeighbor.append(x)
            neighbors.append(copy.deepcopy(localNeighbor))
        return neighbors


