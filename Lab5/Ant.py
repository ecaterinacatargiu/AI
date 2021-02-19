# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:52:48 2020

@author: Cati
"""

from random import random, randint

class Ant:
    
    def __init__(self, n):
        self.n = n
        self.antsPath = self.getAnt()
        
    def getSize(self):
        return self.n
    
    def getAnts(self):
        return self.ants
    
    def getAnt(self):
        ants = []
        for i in range(self.n):
            ants.append([])
            for j in range(self.n):
                ants[i].append([randint(1,self.n), randint(1,self.n)])
                
        return ants
    
    #kind of fitness function; the fewer errors, the better
    def evaluate(self):
        errors = 0
        for line in self.antsPath:
            indS = [0] * self.n
            indT = [0] * self.n
            for [i,j] in line:
                if 0 < i < self.n:
                    indS[i - 1] = 1
                if 0 < j < self.n:
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
                if 0< self.antsPath[j][i][0] < self.n:
                    indS[self.antsPath[j][i][0]-1] = 1
                if 0< self.antsPath[j][i][1] < self.n:
                    indT[self.antsPath[j][i][1] - 1] = 1
            for ii in range(len(indS)):
                if indS[ii] == 0:
                    errors = errors + 1
                if indT[ii] == 0:
                    errors = errors + 1
                    
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    for l in range(self.n):
                        if i!=k or j!=l:
                            if self.antsPath[i][j]==self.antsPath[k][l]:
                                errors = errors+1
        return errors
    
    
    
    def update(self,q0, trace, alpha, beta):
        
        x = randint(0,self.n-1)
        y = randint(0,self.n-1)
        p = [[randint(1,self.n), randint(1,self.n)] for i in range(self.n)]
        l = []
        p=[[int((p[i][0]**beta)*(trace[self.antsPath[x][y][0]-1][self.antsPath[x][y][0]-1][0]**alpha)),
            int((p[i][1]**beta)*(trace[self.antsPath[x][y][0]-1][self.antsPath[x][y][0]-1][0]**alpha))] for i in range(len(p))]
        if(random() < q0):
            r = [[i, p[i]] for i in range(len(p))]
            r = max(r, key=lambda a: a[1])

            self.antsPath[x][y]=p[r[0]]
        else:
            r = randint(0,len(p)-1)
            self.antsPath[x][y]=p[r]

    
    def __str__(self):
        s=""
        for i in range(self.n):
            for j in range(i):
                s=s+"" +str(j)
            s+="\n"
        return s


#a = Ant(3)

    