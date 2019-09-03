from random import randint
import matplotlib.pyplot as plt
import numpy as np

from algorithm import Algorithm
from problem import Problem
#
# if __name__ == '__main__':
#
#
#     problem = Problem()
#     algo = Algorithm(problem)
#     for i in range(1000):
#         population = algo.iteration()
#     print(algo.problem.printBoard())

class Application:
    def __init__(self, fileName):
        self.fileName = fileName



    def main(self):
        self.algorithm = Algorithm(self.fileName)
        best = self.algorithm.run()
        best.problem.printBoard()

    def runStat(self):
        bsts = []
        for i in range(30):
            print("Running test #" + str(i))
            self.algorithm = Algorithm(self.fileName)
            res = self.algorithm.run(False)
            bsts.append(res.bestOf(10)[0])
            res.problem.printBoard()
            arr = []
            for i in range(len(bsts)):
                arr.append(bsts[i].fitness())

            stddev = np.std(arr)
            average = np.average(arr)
            best = min(arr)
            print("Stddev: " + str(stddev))
            print("Average: " + str(average))
            print("Best: " + str(best))
        print("Done!")


app = Application("params.txt")
app.main()
#app.runStat()