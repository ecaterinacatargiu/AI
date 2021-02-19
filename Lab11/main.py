# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:40:49 2020

@author: Cati
"""


from controller import Population
from operations import *

epsilon = 0.9

if __name__ == '__main__':
    (trainingData,output) = readTrainingData()
    population=Population(trainingData,output)
    i=1
    while True:
        error = population.train()
        print(error)
        i+=1
        if error<epsilon:
            break
    testData = readTestData()
    allOutput=[]
    for i in range(len(testData)):
        output = population.predict(testData[i])
        print(output)
        allOutput.append(output)
