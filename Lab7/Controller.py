# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:56:20 2020

@author: Cati
"""

from Repository import Repository

class Controller:
    
    def __init__(self, repo: Repository):
        self.repository = repo
        self.iterations =0 
        self.rate =0
        
        
    def setAttributes(self, iterations, rate):
        self.iterations = iterations
        self.rate = rate
        
        
    def run(self):
        
        rate = self.rate
        epoch = self.iterations
        data = self.repository.info
        n = len(data)
        
        x = [[], [], [], [], [], []]
        y = []
        
        for i in range(len(data)):
            x[0].append(data[i][0])
            x[1].append(data[i][1])
            x[2].append(data[i][2])
            x[3].append(data[i][3])
            x[4].append(data[i][4])
            y.append(data[i][5])
            
        m = [0, 0, 0, 0, 0]
        c = 0
        
        for k in range(epoch):
            solution = [[], [], [], [], [], []]
            dc = []
            error = []
            for i in range(n):
                f = m[0] * x[0][i] + m[1] * x[1][i] + m[2] * x[2][i] + m[3] * x[3][i] + m[4] * x[4][i] + c
                for j in range(5):
                    solution[j].append(x[j][i] * (y[i] - f))
                dc.append(y[i]-f)
                error.append(round(y[i] - f, 2) ** 2)
            for j in range(5):
                solution[j] = -2 / n * sum(solution[j])
                m[j] = m[j] - rate * solution[j]
                
            dc = -2 / n * sum(dc)
            c = c - rate * dc
            error = 1 / n * sum(error)
        print(m, round(c, 2))
        print(error)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        