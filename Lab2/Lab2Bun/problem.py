# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:58:01 2020

@author: Cati
"""
from state import State
from copy import deepcopy
from sys import maxsize


class Problem:
    
    def __init__(self, initialState:State):
        self.initialState = initialState
        
        
    def getInitialState(self):
        return self.initialState


    def getRoot(self):
        return deepcopy(self.initialState)
    
    
    def getEmptyCells(self, emptyM):
        empty = []
        for i in range(len(emptyM)):
            for j in range(len(emptyM)):
                if emptyM[i][j] == 0:
                    empty.append((i,j))
                    
        return empty
    
    
    def getNumberEl(self, matrix,elem=1):
        nr1 = 0
        for line in matrix:
            for el in line:
                if el == elem:
                    nr1 +=1
        return nr1
    
    
    def expand(self, currentState: State):
        
        values = currentState.getInitialState()
        positions = self.getEmptyCells(values)
        noOnes = self.getNumberEl(values)

        if noOnes >= len(values):
            return []

        result = []
        for t in positions:
            auxiState = deepcopy(currentState)
            auxiState.putOne(t[0]-1,t[1]-1,1)
            result.append(auxiState)
            print(auxiState)

        return  result
    
    
    
    
    def checkRow(self):
         
        n = self.initialState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.initialState.getInitialState()[i][j] == 1:
                    count = count + 1     
            if count > 1:
                return False
        return True
        
        
    def checkColumn(self):
        
        n = self.initialState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.initialState.getInitialState()[j][i] == 1:
                    count = count + 1        
            if count > 1:
                return False
        return True
    
    
    def checkCond(self):
        if self.isFinal():
            return self.checkRow() and self.checkColumn() #and self.checkAbs()
    
    
    def checkAbs(self):
        n = self.finalState.getSize()
        for i1 in range(0,n):
          for i2 in range(i1,n):
              for j1 in range(0,n):
                  for j2 in range(j1, n):
                      if abs(i1-i2)-abs(j1-j2) !=0 and not self.finalState.getInitialState()[i1][j1] == 1 and not self.finalState.getInitialState()[i2][j2] == 1:
                          return False
        return True
    
    
    def checkRowFinal(self):
         
        n = self.initialState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.initialState.getInitialState()[i][j] == 1:
                    count = count + 1     
            if count == 1:
                return True
        return False
        
        
    def checkColumnFinal(self):
        
        n = self.initialState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.initialState.getInitialState()[j][i] == 1:
                    count = count + 1        
            if count == 1:
                return True
        return False
    
    
    def checkCondFinal(self):
        return self.checkColumnFinal() and self.checkRowFinal() and self.checkAbs()
    
        
    def isFinal(self):
        for i in self.initialState.getInitialState():
            for j in self.initialState.getInitialState():
                if j==-1:
                    return False 
        return True
    
    
    #number of zeros in a matrix
    def heuristicFunction(self,state):
        if not self.checkCond():
            return maxsize
        return self.getNumberEl(state.getInitialState(),0)
    
  

    
    