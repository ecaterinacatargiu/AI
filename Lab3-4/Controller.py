# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:39:34 2020

@author: Cati
"""

from Particle import Particle
from Swarm import Swarm 

class Controller:
    
    def __init__(self, n):
        self.n = n
        self.swarm = Swarm(n)
        
        
    def iteration(self, population, neighbours, w, c1, c2):
        
        # first we have to determine the best neighbor for each particle
        bestNeighbors = []
        for i in range(len(population)):
            bestNeighbours.append(swarm.getNeighbours(population, 20))
            
        #update the velocity
        for i in range(len(population)):
            swarm.getParticle().velocity(bestNeighbours[i],w,c1,c2)
            
        #update position
        for i in range(len(population)):
            newPosition = []
            for j in range(len(population[0].velocity)):
                newPosition = swarm.getParticle()[i] + velocity(bestNeighbours[i],w,c1,c2)
                population[i].setPosition(newPosition)
                population[i].evaluate()
                population[i].update()
                
        return population
            
    
            
    def runPSO(self):
        
        nrIterations = 100
        w=1.0
        c1=1.0
        c2=2.5
        sizeOfNeighborhood = 20
        dimensionParticle = 3
        p = Particle(dimensionParticle)
        dimensionSwarm = 1000
        s = Swarm(dimensionParticle, dimensionSwarm)
        
        for i in range(nrIterations):
            pop = self.iteration(s, sizeOfNeighbours, w, c1, c2)
            
            
        best = []
        for i in range(0, len(pop)):
            if pop[i].fitness() < pop[best].fitness():
                best = i
                
        return pop[best]
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
