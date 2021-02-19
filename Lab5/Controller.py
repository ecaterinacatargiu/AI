# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:53:33 2020

@author: Cati
"""

from copy import deepcopy

from Ant import Ant
from Problem import Problem

class Controller:
    
    def __init__(self):
        self.n = None
        self.nrEpoc = None
        self.nrAnts = None
        self.alpha = None
        self.beta = 0
        self.rho = None
        self.q0 = None
        
        
    def loadParams(self, p:Problem):
        self.n = p.n
        self.nrEpoc = p.nrEpoc
        self.nrAnts = p.nrAnts
        self.alpha = p.alpha
        self.beta = p.beta
        self.rho = p.rho
        self.q0 = p.q0
        
        
    #fitness function, the less errros, the better
    def fitness(self, matrix):
        
        if matrix == []:
            return 1000
        errors = 0
        for line in matrix:
            indS = [0] * self.n
            indT = [0] * self.n
            for [i, j] in line:
                if i > 0:
                    indS[i - 1] = 1
                if j > 0:
                    indT[j - 1] = 1
            for i in range(len(indS)):
                if indS[i] == 0:
                    errors = errors + 1
                if indT[i] == 0:
                    errors = errors + 1
        for i in range(self.n):
            indS = [0] * self.n
            indT = [0] * self.n
            for j in range(self.n):
                if matrix[j][i][0] > 0:
                    indS[matrix[j][i][0] - 1] = 1
                if matrix[j][i][1] > 0:
                    indT[matrix[j][i][1] - 1] = 1
            for ii in range(len(indS)):
                if indS[ii] == 0:
                    errors = errors + 1
                if indT[ii] == 0:
                    errors = errors + 1
        return errors
        
    
    #~epoch
    def iteration(self, nrAnts, n, trace, alpha, beta, q0, rho):
        
        antSet = [Ant(n) for i in range(nrAnts)]
        for i in range(nrAnts):
            for ant in antSet:
                ant.update(q0, trace, alpha, beta)
        dTrace = [ [1.0 / antSet[i].evaluate(),1.0 / antSet[i].evaluate()]  for i in range(nrAnts)]
        for i in range(self.n):
            for j in range(self.n):
                trace[i][j][0] = (1-rho) * trace[i][j][0]
                trace[i][j][1] = (1 - rho) * trace[i][j][1]
        for x in range(self.n):
            for y in range(self.n):
                trace[x][y][0] = trace[x][y][0] + dTrace[x][0]
                trace[x][y][1] = trace[x][y][1] + dTrace[x][1]
        lista = [[antSet[i].evaluate(), i] for i in range(nrAnts)]
        lista.sort(key = lambda x : x[0])
        
        return antSet[lista[0][1]].antsPath
    
    
    
    def run(self):
        
        sol = []
        bestSol = []
        bestFit = 100
        trace = [[[1,1] for i in range(self.n)] for j in range(self.n)]
        print("START!!!!")
        for i in range(self.nrEpoc):
            sol = deepcopy(self.iteration(self.nrAnts, self.n, trace, self.alpha, self.beta, self.q0, self.rho))
            if self.fitness(sol) < self.fitness(bestSol):
                bestSol = deepcopy(sol)
                bestFit = self.fitness(bestSol)
        return (bestFit, bestSol)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    