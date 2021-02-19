# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:11:22 2020

@author: Cati
"""

from state import State
from problem import Problem

class Controller:
    
    def __init__(self, problem:Problem):
        self.problem = problem
        
    
    
    def setIt(self,problem:Problem):
        self.problem = problem
        
    
    
    def dfs(self, state: State):
        
        stk = [state]
        visited = []

        while len(stk) > 0:
            node = stk.pop(0)
            if self.problem.checkCondFinal():
                print("Solution")
                print(node)
                return
            visited.append(node)
            if self.problem.checkCond():
                lst = []
                newStates = self.problem.expand(node)
                for newState in newStates:
                    if newState not in visited:
                        lst.append(newState)
                stk += lst

        print("No solution")

    
    
    
    def greedy(self, root: State):
        
        visited = []
        toVisit = [root]

        while len(toVisit) > 0:
            state = toVisit.pop(0)
            visited.append(state)
            if self.problem.checkCondFinal():
                print("Solution")
                print(str(state))
                return
            elif self.problem.checkCond():
                values = []
                children = self.problem.expand(state)

                for i  in children:
                    if i not in visited:
                        values.append(i)
                        print(i)
                        
                        
                values = [[kid,self.problem.heuristicFunction(kid)] for kid in values]
                values.sort(key=lambda v:v[-1])
                values = [kid[0] for kid in values]
                toVisit = values[:] + toVisit

        print("No Solution!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    