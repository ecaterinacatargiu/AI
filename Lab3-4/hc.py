# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:21 2020

@author: Cati
"""

from copy import deepcopy
from Population import Population


#Hill Climbing wanna be
def getNeighbour(self, s, n):
    neighbour = []
    for i in range(2):
        for j in range(n):
            for k in range(n):
                state = deepcopy(s)
                state[i][j][k] = state[i][j][k] + 1
                if state[i][j][k] in [1,2,3]:
                    neighbour.append(state) 
                state = deepcopy(s)
                state[i][j][k] = state[i][j][k] - 1
                if state[i][j][k] in [1,2,3]:
                    neighbour.append(state)
    return neighbour
            
    
def runHillClimbing(self, state, n):
    population = Population(n,1,1,1)
    fitState = population.fitness(state)
    neighbours = self.getNeighbour(state, n)
    neighbours = [(population.fitness(x), x) for x in neighbours]
    neighbours.sort(key = lambda x : x[0])
    fitN = neighbours[0][0]
    bestN = neighbours[0][1]
    if fitN < fitState:
        fitState = fitN
        state = bestN
        return (state, fitState, False)
    elif fitState == 0:
        return (state, fitState,True)
    elif fitState!=0:
        state = [population.getIndividual(n),population.getIndividual(n)] 
        return(state,population.fitness(state), False)