import numpy as np


class NeuralNetwork:

    def __init__(self, inputs, outputs):
        self.input = inputs
        self.weights1 = np.random.rand(self.input.shape[1], 5)
        self.weights2 = np.random.rand(5, 1)
        self.y = outputs
        self.output = np.zeros(self.y.shape)
        self.loss = []

    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1.0 - x)

    # computes the output of the network based on the input
    def feedforward(self):
        self.layer1 = self.sigmoid(np.dot(self.input, self.weights1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))

    # the backpropagation algorithm
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) *
                                            self.sigmoid_derivative(self.output)))

        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y -
                                                       self.output) * self.sigmoid_derivative(self.output),
                                                  self.weights2.T) *
                                           self.sigmoid_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.loss.append(sum((self.y - self.output) ** 2))