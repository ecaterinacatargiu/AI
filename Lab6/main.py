# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:28:23 2020

@author: Cati
"""

from random import shuffle
from math import floor
from collections import Counter
import numpy as np



#Read data from file
def readFromFile(fileName):
    dataSet = []
    with open(fileName, 'r') as f:
        for line in f.readlines():
            row = line.split(',')
            label = row.pop(0)
            row = [int(val) for val in row]
            row.append(label)

            dataSet.append(row)
    return dataSet

#r = readFromFile("balance-scale.txt")
#print(r)


#Splitting the entire data  for training the decision tree with given percent of 80%
def splitForTraining(dataSet, p: float = 0.8):
    lenDataSet = len(dataSet)
    trainingSplit = floor(p * lenDataSet)
    shuffle(dataSet)
    
    return dataSet[:trainingSplit], dataSet[trainingSplit:]


#tr = splitForTraining(readFromFile("balance-scale.txt"), 0.85)
#print(tr)
    

#Getting every columns in each list, so that we can compute the gini impurity
def divideColumns():
    listt = readFromFile("balance-scale.txt")
    col = list(zip(*listt))
    print(col)
    
    for newList in col:
        print(newList)
        print(len(newList))
    return col

#Counts attributes for each class(R,L,B)
def countAttributes(ds):
    return Counter([row[-1] for row in ds])

#Test if a certain value is numeric or not
def checkNumeric(value):
    return isinstance(value, int) or isinstance(value, float)
    

#A question used to partionate a dataset
class Question:
    
    header = None
    
    def __init__(self, column, value):
        self.column = column
        self.value = value
        
    #Compare the feature value in the exemple to the deature value in this exact question
    def isMatch(self, randomValue):
        var = randomValue[self.column]
        if checkNumeric(var):
            return var>self.value
        else:
            return var==self.value
    
    #Method used to print the question in a readable format
    def __repr__(self):
        condition = "=="
        if checkNumeric(self.value):
            condition = ">=";
        return "Is %s %s %s?" (
            Question.header[self.column], condition, str(self.value))
        

#Create a partition in out dataset
def partition(rows, question):
    trueR, falseR = [], []
    for row in rows:
        if question.isMatch(row):
            trueR.append(row)
        else:
            falseR.append(row)
            
    return trueR, falseR


#Computing the gini impurity for the given dataset
def gini(columns):
    count = countAttributes(columns)
    imp = 1
    for key in count:
        keyCount = count[key]/float(len(columns))
        imp -= keyCount**2
    return imp


#ginii = gini(readFromFile("balance-scale.txt"))
#print(ginii)

#Get the information gain: The uncertainty of the starting node, minus the weighted impurity of two child nodes.
def getGain(left, right, uncertainty):
    p = float(len(left))/(len(left) + len(right))
    return uncertainty - p*gini(left) - (1-p)*gini(right)    
    

#Find the best question to ask using the information gain ^
def getBestSplit(rows):
    bestG = 0
    bestQ = None
    uncertainty = gini(rows)
    feature = len(rows[0])-1
    for col in range(feature):
        values = set([row[col] for row in rows])
        for val in values:
            q = Question(col, val)
            trueR, falseR = partition(rows, q)
            if len(trueR) == 0 or len(falseR) == 0:
                continue
            gain = getGain(trueR, falseR, uncertainty)
            if gain>bestG:
                bestG, bestQ = gain, q        
    return bestG, bestQ


#Clasifyng data. Represented as a dictionary
class Leaf:
    def __init__(self, rows):
        self.info = countAttributes(rows)
        
        
#Decision Node - this will ask the question      
class Node:
    
    def __init__(self, question, trueBranch, falseBranch):
        self.question = question
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch
    

#Classify recursively the given data on branches 
def classification(row, node):
    if isinstance(node, Leaf):
        return node.info.most_common(1)[0][0]
    
    if node.question.isMatch(row):
        return classification(row, node.trueBranch)
    else:
        return classification(row, node.falseBranch)
        
    
#Build the tree recursively
def buildTree(rows):
    gain, question = getBestSplit(rows)
    #No questions remained to ask
    if gain==0:
        return Leaf(rows)
    #We found a useful value
    trueR, falseR = partition(rows, question)
    #Build the true and false branch
    trueBranch = buildTree(trueR)
    falseBranch = buildTree(falseR)
    
    #We return a question node
    return Node(question, trueBranch, falseBranch)

def printTree(node, spacing=""):
    if isinstance(node, Leaf):
        print("spacing" + "Info", node.info)
        return
    print(spacing+str(node.question))
    
    print(spacing+ '--> True: ')
    printTree(node.trueBranch, spacing + " ")
    
    print(spacing+ '--> False')
    printTree(node.falseBranch, spacing + " ")

def printLeaf(counts):
    total = sum(counts.values()) * 1.0
    prob ={}
    for key in counts.keys():
        prob[key] = str(int(counts[key]/total*100)) + "%"
        
    return prob
    

if __name__=='__main__':
    
    dataSet = readFromFile("balance-scale.txt")

    runs = 1000
    p = 0.9
    accuracy = []
    
    #for _ in range(runs):
    train, test = splitForTraining(dataSet, p)
    decisionTree = buildTree(train)
    
    correct = 0
    total = 0
    
    for row in test:
        info = classification(row, decisionTree)
        now = row[-1]
        correct += 1 if info == now else 0
        total +=1
        
        accuracy.append(correct/total)
        
    print(f"Mean accuracy for {runs} runs, p={p}: {np.mean(accuracy)}")
            
    


















