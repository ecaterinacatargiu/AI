# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:11:41 2020

@author: Cati
"""
from random import randint

from Patrticle import Particle

class Swarm:
    
    def __init__(self, sizeParticle, sizeSwarm):
        self.sizeSwarm = sizeSwarm #n will be the size of the swarm, the size of the population of particles
        self.sizeParticle = sizeParticle #m will be the size of a particle
        self.swarm = getPopulation(self.sizeParticle, self.sizeSwarm)
        


    def getPopulation(self, n, m):#n = size of particle, m = size of swarm
        return [Particle(n) for x in range(m)]
    
    def getSizeSwarm(self):
        reuturn self.sizeSwarm
        
    def getSizeParticle(self):
        return self.sizeParticle
    
    def getNeighbours(self, population, nSize): #nSize = the number of neighbours of my particle
       
        if nSize > len(pop):
            nSize = len(pop)
        neighbours = []
        
        for i in range(len(pop)):
            localNeighbor = []
            for j in range(nSize):
                x = randint(0, len(pop) - 1)
                while x in localNeighbor:
                    x = randint(0, len(pop) - 1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    