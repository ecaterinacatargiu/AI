# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:13:11 2020

@author: Cati
"""
from random import choice
from copy import deepcopy

class State:
    
    def __init__(self,  n):
        self.initialState = [[-1]*n]*n
        self.size = n
        
    def getInitialStateValues(self):
        return self.initialState
    
    def getSize(self):
        return self.size
    
    def __str__(self):
        s=""
        for i in self.initialState:
            for j in i:
                s=s+"" +str(j)
            s+="\n"
        return s
    
        
#x=State(3)
#print(x.getInitialState())

class Problem:
    
    def __init__(self, n):
        self.initialState = State(n)
        
        
    def getInitialState(self):
        return self.initialState


    def getRoot(self):
        return deepcopy(self.initialState)
    
    
    def getEmptyCells(self, emptyM:list):
        empty = []
        for i in range(len(emptyM)):
            for j in range(len(emptyM)):
                if emptyM[i][j] == 0:
                    empty.append((i,j))
                    
        return empty
    
    
    def checkRow(self):
         
        n = self.finalState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.finalState.getInitialStateValues()[i][j] == 1:
                    count = count + 1     
            if count > 1:
                return False
        return True
        
        
    def checkColumn(self):
        
        n = self.finalState.getSize()
        for i in range(n):
            count = 0
            for j in range(n):
                if self.finalState.getInitialStateValues()[i][j] == 1:
                    count = count + 1        
            if count > 1:
                return False
        return True
    
    
    def checkAbs(self):
        n = self.finalState.getSize()
        for i1 in range(0,n):
          for i2 in range(i1,n):
              for j1 in range(0,n):
                  for j2 in range(j1, n):
                      if abs(i1-i2)-abs(j1-j2) !=0 and not self.finalState.getInitialStateValues()[i1][j1] == 1 and not self.finalState.getInitialStateValues()[i2][j2] == 1:
                          return False
        return True
    
    
    def isValid(self):
        if self.isFinal():
            return self.checkRow() and self.checkColumn() and self.checkAbs()
    
    
    def expand(self):
        
        values = [0,1]
        n = self.initialState.getSize()
        
        for i in range(n):
            l = []
            for j in range(n):
                k= choice(values)
                l.append(k)
            self.initialState.getInitialStateValues()[i] = l
            
            
    def isFinal(self):
        for i in self.initialState.getInitialStateValues():
            for j in self.initialState.getInitialStateValues():
                if j==-1:
                    return False 
        return True
            
        
                
        
#x=Problem(2)
#x.expand()
#print(x.initialState.getInitialState())
#print(x.isValid())

class Controller:
    
    def __init__(self, problem):
        self.problem = problem
    
    
    def dfs(self,state):
        
        stk = [state]
        visited = []

        while len(stk) > 0:
            node = stk.pop()
            if self.problem.isFinal():
                print("Solution")
                print(node)
                return
            visited.append(node)
            if self.problem.isValid():
                lst = []
                for newState in self.problem.expand():
                    if newState not in visited:
                        lst.append(newState)
                stk += lst

        print("No solution")
    
    
    
    def gbfs(self, state):
        pass
    
  
#p=Problem(3)
#c = Controller(p)
#print(c.dfs(p.getInitialState()))
 
    
class UI:
    
    def __init__(self, controller):
        self.controller = controller
        
        
    def printMenu(self):
        print()
        print("1 - DFS style")
        print("2 - Greedy style")
        print()
        
        
    def start(self):
        self.printMenu()
        command = int(input("Enter your command: "))
        while command !=0:
            if command == 1:
                state = self.controller.problem.initialState
                self.controller.dfs(state)
            else:
                if command == 2:
                    self.controller.gbfs()
                else:
                    if command  == 0:
                        break
                    
                    else:
                        print("No command")
                        
        self.printMenu()
        command = int(input("Enter your command: "))



def main():
    size=int(input("Enter the size of the table: "))
    p=Problem(size)
    c = Controller(p)
    ui = UI(c)
    ui.start()
    
    
main()
                        
        
    
    
    
    

            
        
        
    
    
    
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               