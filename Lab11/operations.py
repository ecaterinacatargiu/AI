# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:40:23 2020

@author: Cati
"""


import csv

def readTrainingData():
    trainingData = []
    output = []
    with open('training.data') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            trainingData.append([float(row[i]) for i in range(24)])
            output.append(row[24])
    return trainingData, output

def readTestData():
    testingData = []
    output = []
    with open('input.in') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            testingData.append([float(row[i]) for i in range(24)])
            output.append(row[24])
    return testingData