# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:53:21 2020

@author: Cati
"""


from Ant import Ant

class Problem:
    
    def __init__(self):
        self.n = None
        self.nrEpoc = None
        self.nrAnts = None
        self.alpha = None
        self.beta = 0
        self.rho = None
        self.q0 = None
        
    #read from file data that will be snet to the controller
    def loadProblem(self):
        
        f = open("problem.txt", "r")
        self.n = int(f.readline())
        self.nrEpoc = int(f.readline())
        self.nrAnts = int(f.readline())
        self.alpha = float(f.readline())
        self.beta = float(f.readline())
        self.rho = float(f.readline())
        self.q0 = float(f.readline())
        