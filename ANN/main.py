from math import *

import numpy as np
import matplotlib.pyplot as plt

from NeuralNetwork import NeuralNetwork


def readData(fileName):

    outputs = {"DH\n" : 0,
            "SL\n": 1,
               "NO\n" : 2}

    inData= []
    outData = []
    noFeatures = 0
    noExamples = 0
    noOutputs = 1
    with open(fileName) as f:
        lines = f.readlines()
        noExamples = len(lines)
        for line in lines:
            data = line.split(' ')
            noFeatures = len(data) - 1
            if len(data) < 7:
                continue
            inp = []
            for i in range(len(data) - 1):
                inp.append(float(data[i]))
            inData.append(inp)

            outData.append([outputs[data[len(data) - 1]]])
    return noExamples, noFeatures, noOutputs, inData, outData


def normaliseData(noExamples, noFeatures, trainData, noTestExamples, testData):
    # statistical normalisation
    for j in range(noFeatures):
        summ = 0.0
        for i in range(noExamples):
            summ += trainData[i][j]
        mean = summ / noExamples
        squareSum = 0.0
        for i in range(noExamples):
            squareSum += (trainData[i][j] - mean) ** 2
        deviation = sqrt(squareSum / noExamples)
        for i in range(noExamples):
            trainData[i][j] = (trainData[i][j] - mean) / deviation
        for i in range(noTestExamples):
            testData[i][j] = (testData[i][j] - mean) / deviation
    # min-max normalization
    """
    for j in range(noFeatures):
        minn=min([trainData[i][j] for i in range(noExamples)])
        maxx=max([trainData[i][j] for i in range(noExamples)])
        for i in range(noExamples):
            trainData[i][j]=LIM_MIN+trainData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
         for i in range(noTestExamples):
            testData[i][j]=LIM_MIN+testData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
    """


def devise_data():
    res1 = readData("trainData.txt")

    inTestData = []
    outTestData = []

    inTrainData = []
    outTrainData = []
    for i in range(len(res1[3])):
        if i % 10 == 0:
            inTestData.append(res1[3][i])
            outTestData.append(res1[4][i])
        else:
            inTrainData.append(res1[3][i])
            outTrainData.append(res1[4][i])

    normaliseData(len(inTrainData), res1[1], inTrainData, len(inTestData), inTestData)

    return inTrainData, outTrainData, inTestData, outTestData


if __name__ == "__main__":

    result = devise_data()

    inTrain = np.array(result[0])
    outTrain = np.array(result[1])

    inTest = np.array(result[2])
    outTest = np.array(result[3])


    nn = NeuralNetwork(inTrain, outTrain)


    nn.loss=[]
    iterations =[]
    for i in range(3000):
        nn.feedforward()
        nn.backprop()
        iterations.append(i)

    #print(nn.output)

    plt.plot(iterations, nn.loss, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()

    test = NeuralNetwork(inTest, outTest)

    test.loss = []
    iterations = []
    for i in range(3000):
        test.feedforward()
        test.backprop()
        iterations.append(i)

    print(test.output)

    plt.plot(iterations, test.loss, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()

