from swarm import Swarm

#For each particle
#    Initialize particle
#END
#
#Do
#    For each particle
#        Calculate fitness value
#        If the fitness value is better than the best fitness value (pBest) in history
#            set current value as the new pBest
#    End
#
#    Choose the particle with the best fitness value of all the particles as the gBest
#    For each particle
#        Calculate particle velocity according equation (a)
#        Update particle position according equation (b)
#    End
class Controller:

    def runAlg(self):
        count = 0
        s = Swarm(40,5,5)
        while s.bestGlobal > 0.000000001:
            count += 1
            for particle in s.particles:
                particle.calFitness()
            s.getBestParticle()
            for particle in s.particles:
                particle.evaluate(s.bestGlobalX,s.bestGlobalY,s.c1,s.c2)
        print ("Fount in " + str(count) + " moves")
