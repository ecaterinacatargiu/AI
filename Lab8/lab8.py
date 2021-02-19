# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:45:33 2020

@author: Cati
"""

import numpy as np
import matplotlib as mpl


#the activation function:
def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return 1

def readFromDataBase(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()[4:]
        lines = [line.split() for line in lines]
        lines = [line for line in lines if len(line) != 0]
        return [[float(x) for x in line] for line in lines]

class NeuralNetwork:
   
    def __init__(self, x, y,hidden):
        self.input      = x
        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self.loss       = []
        self.weights1   = np.random.rand(self.input.shape[1],hidden) 
        self.weights2   = np.random.rand(hidden,1)          


    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))/497
        

    # the backpropagation algorithm 
    def backprop(self,l_rate):

           d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) *
                            sigmoid_derivative(self.output)))
           
           d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y -
                            self.output) * sigmoid_derivative(self.output),
                            self.weights2.T) *
                             sigmoid_derivative(self.layer1)))
           # update the weights with the derivative (slope) of the loss function
           
           self.weights1 += l_rate * d_weights1
           self.weights2 += l_rate * d_weights2
           self.loss.append(sum((self.y - self.output)**2))


if __name__ == "__main__":
    data = readFromDataBase('database.txt')
    xList = []
    yList = []
    for elem in data:
        xList.append(elem[:-1])
        yList.append([elem[-1]])
    X = np.array(xList)
    y = np.array(yList)
    nn = NeuralNetwork(X,y,2)

    nn.loss=[]
    iterations =[]
    for i in range(4000):
        nn.feedforward()
        nn.backprop(1)
        iterations.append(i)

    print(nn.output)
    mpl.pyplot.plot(iterations, nn.loss, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()
    
