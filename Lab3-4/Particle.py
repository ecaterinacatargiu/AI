# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:26:47 2020

@author: Cati
"""
from random import randint

class Particle:
    
    def __init__(self, n):
        self.n = n #n will be the size of the particle
        self.particle = self.generateMatrix(n)
        self.evaluateParticle(self.particle)
        self._fitness = None
        self.bestFitness = self.fitness
        self.velocity = [[(0,0) for y in range(n)] for x in range(n)]
        self.position = random()
        self.bestPosition = self.position()
        
    
    def velocity(self,best,w,c1,c2):
        #v = w*currentPos+c1*random*bestN-currentPos+c2*random*bestPos-currentPos
        v=Particle(self.n)
        for i in range(self.n):
            for j in range(self.n): 
                v1 = w * self.velocity[i][j][0]
                v1 += c1 * random() * (best.velocity[i][j][0] - self.velocity[i][j][0]
                v1 += c2 * random() * (self.velocity[i][j][0] - self.velocity[i][j][0]
                
                v2 = w * self.velocity[i][j][1]
                v2 += c1 * random() * (best.velocity[i][j][1] - self.velocity[i][j][1]
                v2 += c2 * random() * (self.velocity[i][j][1] - self.velocity[i][j][1]
                
    
                v.setCell(i,j,(int(v1), int(v2)))
                
        return v
    
    def setCell(self,i,j,e):
        self.velocity[i][j] = e
        
        
    def generateMatrix(self, n):
        matrix = []
        for i in range(n):
            line = []
            for j in range(n):
                line.append((randint(1,n),randint(1,n)))
            matrix.append(line)
            
        return matrix
    
    
    #applies the fitnes function on that particle 
    def evaluateParticle(self, particle):
        self._fitness = self.fitness(particle)
        
        
    def fitness(self, chr):
        if chr == [[],[]]:
            return maxsize
        errors = 0
        indS = chr[0]
        indT = chr[1]

        for i in range(self.n):
            lstS = []
            lstT = []
            for j in range(self.n):
                lstS.append(indS[j][i])
                lstT.append(indT[j][i])
            lstS.sort()
            lstT.sort()
            for i in range(self.n):
                if lstS[i] != i+1:
                    errors = errors + 1
                if lstT[i] != i+1:
                    errors = errors + 1
                  
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    for l in range(self.n):
                        if i != k or j != l:
                            if indS[i][j] == indS[k][l] and indT[i][j] == indT[k][l]:
                                errors = errors + 1
        return errors
    
    
    def updateFitness(self):
        if self._fitness < self.bestFitness:
            self._fitness = self.bestFitness
            
    def getFitness(self):
        return self._fitness
        
        
    def getBestFitness(self):
        return self.bestFitness
    
    def getVelocity(self):
        return self.velocity
    
    def setPosition(self, newPosition):
        self.position = newPosition.copy()
        self.evaluate()
        if self._fitness < self.bestFitness:
            self.bestFitness = self._fitness
            self.bestPosition = self.position
        
            
    def __str__(self):
        stringg =""
        for i in self.particle:
            for j in i:
                stringg=stringg+"" +str(j)
            stringg+="\n"
        return stringg
    

        
         