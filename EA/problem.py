from random import randint
import matplotlib.pyplot as plt
import numpy as np

class Problem:

    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        #self.board[randint(0, 8)][randint(0, 8)] = 1

    def getBoard(self):
        return self.board

    def update(self, pos, move):
        self.board[pos[0]][pos[1]] = move

    def printBoard(self):
        for i in range(8):
            print(self.getBoard()[i])

    def isEmpty(self):
        count = 0
        for i in range(8):
            for j in range(8):
                if (self.getBoard()[i][j] != 0):
                    count += 1

        if (count == 0):
            return True #is empty
        else:
            return False #is not empty

    def isFull(self):
        count = 0
        for i in range(8):
            for j in range(8):
                if (self.getBoard()[i][j] != 0):
                    count += 1

        if (count == 64):
            return True #is full
        else:
            return False #is not full

    def plotBoard(self):
        plt.matshow(self.getBoard())

        plt.show()