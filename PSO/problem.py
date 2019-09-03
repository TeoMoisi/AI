

class Problem:

    def __init__(self):
        self.noOfParticles = 0
        self.noOfNeighbours = 0
        self.w = 0
        self.c1 = 0
        self.c2 = 0
        self.noOfIterations = 0

    def readFromFile(self):

        try:

            arr = []

            with open("data.txt") as f:
                for line in f:
                    line.strip("\n")
                    arr.append(line.split())


        except IOError:
            raise Exception("File is missing")

        self.noOfParticles = int(arr[0][0])
        self.noOfNeighbours = int(arr[1][0])
        self.w = float(arr[2][0])
        self.c1 = float(arr[3][0])
        self.c2 = float(arr[4][0])
        self.noOfIterations = int(arr[5][0])

        return [self.noOfParticles, self.noOfNeighbours, self.w, self.c1, self.c2, self.noOfIterations]
