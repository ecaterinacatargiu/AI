# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:44:05 2020

@author: Cati
"""

from Controller import Controller
from Population import Population
from hc import *

class UI:
    
    def __init__(self, ea:Population, controller: Controller):
        self.ea = ea
        self.controller = controller
    
    
    
    def printMenu(self):
        print()
        print("Choose one: ")
        print("1. EA")
        print("2. Hill Climbing")
        print("3. PSO")
        
    
    def getEa(self):
        return self.ea.iteration()
        
    def getHc(self):
        return self.hc.runHillClimbing(ea, ea.getPopSize())
            
    def getPso(self):
        return self.controller.runPSO()
        
    def start(self):
        self.printMenu()
        command = int(input("Enter your command: "))
        while command !=0:
            if command == 1:
                self.getEA()
            else:
                if command == 2:
                    self.getHC()
                else:
                    if command == 3:
                        self.getPso()
                    else:
                        if command  == 0:
                            return
                        
                        else:
                            print("No command")
                        
            self.printMenu()
            command = int(input("Enter your command: "))
        
        
def main():
    size=int(input("Enter the size of the individual: "))
    popSize=int(input("Enter the size of the population: "))
    pM=int(input("Enter the probability of mutation: "))
    pC=int(input("Enter the probability of crossover: "))
    pop = Population(size,popSize, pM, pC)
    ui = UI(pop)
    ui.start()
    
    
main()
    