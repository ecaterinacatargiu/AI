# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:30:48 2020

@author: Cati
"""

import numpy
from random import randint, random
from sys import maxsize
from copy import deepcopy


class Population :
    
    def __init__(self, n, popSize, prM, prC):
        self.squareSize = n
        self.popSize = popSize
        self.prM = prM
        self.prC = prC
        self.population = self.getPopulation()
        
    def getPopulation(self):
        population = []
        for x in range(self.popSize):
            indS = self.getIndividual()
            indT = self.getIndividual()
            population.append([indS, indT])
        return population
            
        
    def getIndividual(self):
        el = (numpy.random.permutation(self.squareSize)+1 for x in range(self.squareSize))
        listP = []
        for i in el:
            a = list(j for j in i)
            listP.append(a)
        return listP
            
    def getPopSize(self):
        return self.popSize
    
    #crossover function: from 2 parent matrices, we change some elements so that it will result their child
    def crossover(self, parent1, parent2):
        cross = random()
        indS = []
        indT = []
        if self.prC > cross:
            t1 = randint(0,self.squareSize-1)
            t2 = randint(0,self.squareSize-1)
            while t2 < t1:
                t2 = randint(0,self.squareSize-1)
            for i in range(t1+1):
                indS.append(parent1[0][i])
                indT.append(parent1[1][i])
            for i in range(t1+1, t2+1):
                indS.append(parent2[0][i])
                indT.append(parent2[1][i])
            for i in range(t2+1, self.squareSize):
                indS.append(parent1[0][i])
                indT.append(parent1[1][i])
        kid = [indS, indT]
        return kid
    
    
    #mutation function: changing an element from an individ with another random permutation
    def mutate(self, chr):
        mutate = random()
        if self.prM > mutate and chr != [[],[]]:
            t = randint(0,self.squareSize-1)
            pS = list(numpy.random.permutation(self.squareSize)+1)
            pT = list(numpy.random.permutation(self.squareSize)+1)
            chr[0][t] = pS
            chr[1][t] = pT
        return chr
    
    #fitness function that checks if there are as little comom elements as possible on rows and columns
    def fitness(self, chr):
        if chr == [[],[]]:
            return maxsize
        errors = 0
        indS = chr[0]
        indT = chr[1]

        for i in range(self.squareSize):
            lstS = []
            lstT = []
            for j in range(self.squareSize):
                lstS.append(indS[j][i])
                lstT.append(indT[j][i])
            lstS.sort()
            lstT.sort()
            for i in range(self.squareSize):
                if lstS[i] != i+1:
                    errors = errors + 1
                if lstT[i] != i+1:
                    errors = errors + 1
                  
        for i in range(self.squareSize):
            for j in range(self.squareSize):
                for k in range(self.squareSize):
                    for l in range(self.squareSize):
                        if i != k or j != l:
                            if indS[i][j] == indS[k][l] and indT[i][j] == indT[k][l]:
                                errors = errors + 1
        return errors
                
    def getPopulationn(self):
        return self.population
        
    def getSquare(self, chr):
        indS = chr[0]
        indT = chr[1]
        s = ""
        for i in range(self.squareSize):
            for j in range(self.squareSize):
                s += "("+str(indS[i][j])+", "+str(indT[i][j])+")"+" "
            s+="\n"
        return s
    
    
    def iteration(self):
        kids = []
        ind1 = randint(0, self.popSize-1)
        ind2 = randint(0, self.popSize-1)
        if ind1 != ind2:
            parent1 = self.population[ind1]
            parent2 = self.population[ind2]
            chr = self.crossover(parent1, parent2)
            chr = self.mutate(chr)
            f1 = self.fitness(parent1)
            f2 = self.fitness(parent2)
            fc = self.fitness(chr)
            if f1>f2 and f1>fc:
                self.population[ind1]=chr
            if f2>f1 and f2>fc:
                self.population[ind2]=chr
               
        return self.population
                
                
    




                
                
            
            
            
            
            
            
            