
class Problem:

    def __init__(self):
        self.__dimPopulation = 0
        self.__noOfIterations = 0
        self.__probability = 0

    def readFromFile(self):
        f = open("file.txt", "r")
        self.__noOfIterations = int(f.read())
        self.__dimPopulation = int(f.read())
        self.__probability = int(f.read())
        f.close()
