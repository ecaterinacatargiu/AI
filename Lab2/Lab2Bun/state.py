# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:55:35 2020

@author: Cati
"""





class State:
    
    def __init__(self,  n):
        self.values = [[0 for y in range(n)] for x in range(n)]
        self.size = n
        
    def getInitialState(self):
        return self.values
    
    def getSize(self):
        return self.size
    
    def getValues(self):
        return [line[:] for line in self.values]
    
    
    def putOne(self, line, column, values=1):
        self.values[line][column] = 1
    
    def __str__(self):
        s=""
        for i in self.values:
            for j in i:
                s=s+"" +str(j)
            s+="\n"
        return s
    
    
    def __eq__(self, other):
        if not isinstance(other,State):
            return False
        vals = other.getValues()

        if len(vals) != self.size:
            return False

        for ind1 in range(self.size):
            for ind2 in range(self.size):
                if vals[ind1][ind2] != self.values[ind1][ind2]:
                    return False
        return True
    
