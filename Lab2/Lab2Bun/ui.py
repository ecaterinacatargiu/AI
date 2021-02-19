# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:11:51 2020

@author: Cati
"""


from state import State
from problem import Problem
from controller import Controller

class UI:
    
    def __init__(self, controller: Controller):
        self.controller = controller
        
        
    def printMenu(self):
        print()
        print("1 - DFS style")
        print("2 - Greedy style")
        print()
        
        
        
    
    def dsfStyle(self):
        self.controller.dfs(self.problem.getRoot())
        
    def greedyStyle(self):
        pass
    
    
    def start(self):
        self.printMenu()
        command = int(input("Enter your command: "))
        while command !=0:
            if command == 1:
                state = self.controller.problem.initialState
                print(state)
                self.controller.dfs(state)
            else:
                if command == 2:
                    state = self.controller.problem.initialState
                    print(state)
                    self.controller.greedy(state)
                else:
                    if command  == 0:
                        return
                    
                    else:
                        print("No command")
                        
            self.printMenu()
            command = int(input("Enter your command: "))



def main():
    size=int(input("Enter the size of the table: "))
    s = State(size)
    p=Problem(s)
    c = Controller(p)
    ui = UI(c)
    ui.start()
    
    
main()