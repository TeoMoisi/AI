from particle import Particle


class Swarm:
    particles = []
    nrofparticles = 0
    bestGlobal = 30
    bestGlobalX = 0
    bestGlobalY = 0
    c1 = 0
    c2 = 0
    def __init__(self,nrofparticles,c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.nrofparticles = nrofparticles
        for x in range (nrofparticles):
            p = Particle()
            self.particles.append(p)

    def getBestParticle(self):
        for x in self.particles:
            if x.fitness < self.bestGlobal:
                self.bestGlobal = x.fitness
                self.bestGlobalX = x.x
                self.bestGlobalY = x.y
        print("Best Global: ", self.bestGlobal)