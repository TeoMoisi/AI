import math
import random
e = 2.718


class Particle:
    velocity = 0
    fitness = 0
    bestFitness = 0
    bestX = 0
    bestY = 0
    x = 0
    y = 0
    def __init__(self):
        self.x = random.uniform(-5,5)
        self.y = random.uniform(-5,5)
        self.velocityX = 0
        self.velocityY = 0
        self.fitness = 0
        self.bestX = 0
        self.bestY = 0
        self.bestFitness = 2000


#   Get closest distance to target
    def calFitness(self):
        self.fitness = -20*e**(-0.2*math.sqrt(0.5*(self.x**2+self.y**2)))-e**(0.5*(math.cos(2*math.pi*self.x)+math.cos(2*math.pi*self.y)))+e+20
        if(self.fitness < self.bestFitness):
            self.bestFitness = self.fitness
            self.bestX = self.x
            self.bestY = self.y


#       Formula for velocity
#       v[] = v[] + c1 * rand() * (pbest[] - present[]) + c2 * rand() * (gbest[] - present[])(a)
#       present[] = persent[] + v[]
#       Move the Particle closer to the target
    def evaluate(self,bestGlobalX,bestGlobalY,c1,c2):
        self.velocityX = self.velocityX + c1 * random.random() * (self.bestX - self.x) + c2 * random.random() * (bestGlobalX - self.x)
        if self.velocityX > 5:
            self.velocityX = 5
        elif self.velocityX < -5:
            self.velocityX = -5

        self.velocityY = self.velocityY + c1 * random.random() * (self.bestY - self.y ) + c2 * random.random() * (bestGlobalY - self.y)
        if self.velocityY > 5:
            self.velocityY = 5
        elif self.velocityY < -5:
            self.velocityY = -5

        if self.x + self.velocityX > 5:
            self.x = 5
        elif self.x + self.velocityX < -5:
            self.x = -5
        else:
            self.x += self.velocityX


        if self.y + self.velocityY > 5:
            self.y = 5
        elif self.y + self.velocityY < -5:
            self.y = -5
        else:
            self.y += self.velocityY

